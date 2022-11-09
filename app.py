from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import requests
import base64

app = Flask(__name__) 

#Definición de la base de datos y se ata al servidor
app.config['MONGO_URI'] = 'mongodb://database/pythonmongodb'
mongo = PyMongo(app)

#Funcion que construye un diccionario que será el query para consultar la base de datos (endpoint /alerts)
def formar_query(user,day,ioc_types):
    query1 = { 'user': user } if user != None else {}
    if day != None:
        query2_t = datetime.now() - timedelta(days=(int(day))+1)
        query_time = query2_t.strftime('%Y-%m-%d %H:%M:%S')
        query2 = { 'datetime': {'$gte': query_time}}
    else:
        query2 ={}
    query3 = { 'ioc.type_ioc': ioc_types } if ioc_types != None else {}
    query1.update(query2)
    query1.update(query3)
    return query1

#Endpoint que registra una nueva alerta, se ejecuta solo si llegan todos los datos diferentes de Null
@app.route('/alert', methods=['POST'])
def agregar_alerta():
    source=request.json['source']
    type_ioc=request.json['ioc']['type']
    data_ioc=request.json['ioc']['data']
    user=request.json['user']
    datetime=request.json['datetime']
    if source and type_ioc and data_ioc and user and datetime:
        id = mongo.db.alerts.insert(
            { 'source': source, 'ioc': {'type_ioc': type_ioc, 'data_ioc': data_ioc }, 'user': user, 'datetime': datetime }
        )
        #Se cuenta la cantidad de documentos repetidos en base al usuario que generó la alerta  
        repeated = mongo.db.alerts.find({'user': user }).count()
        response = jsonify({
            #La creación automatica de ID es una caracteristica de MongoDB
            'id': str(id),
            'estatus' : 'Alerta recibida correctamente',
            'Número de alertas repetidas del mismo usuario' : str(repeated)
        })
        #Se modifica el status code
        response.status_code = 201
        return response
    else:
        #Mensaje de error que caso que falente campos en el JSON de entrada
        return { 'Error': 'Alerta no registrada' }

#Endoint que consulta de alertas
@app.route('/alerts')
def consultar_bd():
    user= request.args.get('user')
    day= request.args.get('days')
    ioc_types= request.args.get('ioc_type')
    #Se llama la funcion que formará el Query
    query1 = formar_query(user,day,ioc_types)
    query = mongo.db.alerts.find(query1)
    response= json_util.dumps(query)
    return Response(response, mimetype='application/json')

#Endopint que consume API publica (VirusTotal)
@app.route('/ioc')
def url_ioc():
    url= request.args.get('url')
    #La request a la API publica solo recibe la URL transformada a base64
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    ioc= requests.get('https://www.virustotal.com/api/v3/urls/'+url_id, headers={'x-apikey':'58ee81181e20d513af4239ddd28bd49466b9216d7e5d91d796715a32523195ae'})
    ioc_reputation= ioc.json()
    response = jsonify({
            'Estado': 'IOC consultado correctamente',
            'Nivel de reputación del ioc ' : ioc_reputation['data']['attributes']['reputation']
        })
    return(response)

#Home
@app.route('/home')
def Ping():
    return 'Bienvenido al mejor Threat Detector del mundo!'

if __name__ == "__main__":
    app.run(debug=True)