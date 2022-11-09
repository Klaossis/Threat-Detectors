#  Threat Detectors Mercado Libre 🐱‍💻
En el equipo de seguridad informatica de mercado libre necesitabamos administrar las alertas de seguridad de todo el entorno de la compañía, por lo que desarrollamos una API REST que detecta la actividad maliciosa de la red interna de computadores y las almacena para su posterior consulta y analisis.
## Stack tecnológico
Lenguaje de programación: Python. \
Framework: Flask. \
Persistencia de datos: Instancia de MongoDB. \
Framework de testing: Pytest. \
Despliegue con Docker y Docker-compose 🐋.

## Instalación y ejecución
Es necesario tener instalado Docker, para ello dirijase al siguiente link y siga las instrucciones de instalación dependiendo su SO: https://www.docker.com.

## Estructuración



Copiar el repositorio a su equipo local y estando ubicado en la carpeta principal del protecto (*ThreatDetector*) ejecutar el siguiente comando de docker compose:

```bash docker-compose up```

Esto creara la imagen de la bases de datos y del servidor (basado en Alpine y python), terminada la creación ambos contenedores se ejecutarán, podrá acceder al servidor desde *localhost:3000* y si desea interactuar con la base de datos puede acceder a ella ejecutando el siguiente comando el cual le abrirá una terminal interactica sobre la instancia que se esté ejecutando:

```bash docker-compose exec -it database bash```

En caso que quiera correr los test unitarios, estando sobre el directorio principal ejecute el siguiente comando:

```bash docker-compose exec -it web pytest test_file.py```

Mas adelanta se tratará mas a detalle la ejecución de las pruebas unitarias.

Este comando ejecutara todas las pruebas unitarias y en caso que quiera ver el informe detallado agregar el tag -v después de *pytest*.
En este punto ambos servicios se deberían encontrar funcionando correctamente.
(*Antes de empezar a ejecutar requests de consulta sobre la bd de datos se recomienda crear un primer registro haciendo uso del endpoint /alert o agregandolo manualmente, esto ya que como supondrá la primera vez que inicie el contenedor la bd estará vacía.*)
## Funcionalidades

En construcción
