from app import formar_query
import pytest
import requests

#Endpoint para la consulta de alertas
ENDPOINT_Test1 = "http://localhost:3000/alerts" 

#Test al response code del endpoint /alerts
def test_enpoint_home():
    response = requests.get(ENDPOINT_Test1)
    assert response.status_code == 200

#Test a la función que forma el query para la consulta de la base de datos en el endpoint /alerts
def test_formar_query():
    user = 'prueba user'
    day = None
    ioc_types =' probando probando '
    query_test=formar_query(user,day,ioc_types)
    assert query_test == {'user':'prueba user', 'ioc.type_ioc': ' probando probando ' }
