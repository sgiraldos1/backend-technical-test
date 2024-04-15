# backend-technical-test
# Microservicios de Consulta y "Me Gusta" de Inmuebles

Este proyecto implementa dos microservicios para la plataforma Habi, que permite a los usuarios consultar propiedades disponibles para la venta y dar "Me gusta" a propiedades específicas.

## Tecnologías Utilizadas

- Python 3
- Bibliotecas de Python: `http.server`, `json`, `unittest`, `mock`,`docker`,`postman`
- Base de datos mySQL


## Descripción del Proyecto

Habi desea proporcionar una herramienta donde los usuarios puedan consultar propiedades disponibles para la venta, aplicando varios filtros como año de construcción, ciudad y estado. Además, los usuarios pueden dar "Me gusta" a propiedades específicas para mantener un ranking interno de propiedades más llamativas.

## Requerimientos Funcionales

### Microservicio de Consulta

- Los usuarios pueden consultar propiedades con los estados: "pre_venta", "en_venta" y "vendido", mas no pueden ver los estados comprado y comprando.
- Los usuarios pueden filtrar propiedades por año de construcción, ciudad y estado.
- Los usuarios pueden aplicar múltiples filtros en la misma consulta.
- Los usuarios pueden ver la dirección, ciudad, estado, precio de venta y descripción de las propiedades.


### Microservicio de "Me Gusta"

Este microservicio es conceptual

- Los usuarios pueden dar "Me gusta" a una propiedad específica.
- Los "Me gusta" son de usuarios registrados y se registran en la base de datos.

## Estructura del Proyecto

<p>Estructura del proyecto, mostrando los archivos y carpetas principales:</p>

- `src/`: Directorio principal que contiene el código fuente del proyecto.
    - `controllers/`: Controladores para manejar solicitudes HTTP.
    - `services/`: Servicios de consulta de inmuebles.
    - `config/`: Configuración del proyecto, incluyendo la conexión a la base de datos.
- `tests/`: Directorio que contiene pruebas unitarias para el código.
- `assets/`: carpeta que contiene el diagrama ENTIDAD-RELACION del servicio de me gusta 
- `scripts/`: carpeta que contiene el codigo sql para extender el modelo generado a partir del diagrama ENTIDAD-RELACION
- `README.md`: Este archivo contiene la documentacion y pasos de ejecucion del proyecto.
-`requirements`: Archivo de requerimientos para instalar las dependencias


<pre>
BACKEND-TECHNICAL-TEST
├── Dockerfile
├── README.md
├── assets
│   └── like service.png
├── main.py
├── requirements.txt
├── scripts
│   └── database.sql
├── src
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── database.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── property_controller.py
│   ├── server.py
│   └── services
│       ├── __init__.py
│       └── consulting_service.py
├── test_main.py
└── tests
    ├── __init__.py
    └── services
        ├── __init__.py
        └── test_consulting_service.py
</pre>

## Desarrollo

Se aborda el desarrollo de la prueba tecnica creando un endpoint de tipo GET el cual permite la obtencion de datos como un producto o lista de productos usando la libreria de python http.server,Luego se procede a ejecutarse en un servidor web para proseguir con la conexion a la base de datos en el adminitrador de bases de datos Mysql, como resultado, se obtiene la generacion de inmuebles con el uso de postman para el ingreso de las variables de estado, ciudad y año del inmueble.

Se agrega el diagrama de ENTIDAD-RELACION para el servicio de me gusta en los inmuebles y su codigo correspondiente.


### Pasos para la ejecucion

1. Se instalan los requerimientos con el archivo de requirement.txt

```bash
pip install --upgrade -r requirements.txt
```


2. Se ejecuta el servidor con el siguiente comando 

```bash
python3 main.py
```

2. se ingresa a postman y se ingresan las variables de city, year y status proseguido del boton send 

![postman](https://raw.githubusercontent.com/sgiraldos1/backend-technical-test/main/assets/postman.jpeg)


3. Para ver la ejecucion del codigo sin necesidad de postman, se usa  curl, un manejador de peticion de http, se usa el siguiente link


curl http://localhost:8000/properties?status=en_venta&construction_year=2011&city=medellin


## Diagrama de Entidad-Relación (ER)

Se crea el diagrama de ENTIDAD-RELACION del servicio de me gusta donde se muestra la estructura de la base de datos extendida para soportar la funcionalidad de "Me Gusta" en el servicio correspondiente.

se puede ver tanto en el codigo de sql cargado en la carpeta scripts, como en forma de diagrama cargado en la carpeta assets. 

se creo de esta forma basado en la logica de que un inmueble puede tener 1 o mas likes dados y un usuario tiene la potestad de dar 1 o mas likes.

![likes_service](https://raw.githubusercontent.com/sgiraldos1/backend-technical-test/main/assets/like_service.png)


## Ejecución de las Pruebas Unitarias

las pruebas unitarias se encuentran contenidas en la carpeta tests- services y el script test-consulting_service.py.

Para ejecutar las pruebas  Se ejecuta el siguiente comando en la raiz del proyecto

```bash
python3 -m unittest tests/**/*.py --verbose
```

se desarrollaron estas pruebas usando mock como representacion de un objeto que permite simular el comportamiento de una clase o funciones dentro de un modulo de python, se usa el framework unittest para realizar la prueba automatizada.

![pruebas_unitarias](https://raw.githubusercontent.com/sgiraldos1/backend-technical-test/main/assets/pruebas_unitarias.jpeg)

## Extra 

Se dockeriza el sistema usando el archivo dockerfile.Para ejecutarlo se realiza con los siguientes comandos:

1. 
```bash
docker build -T properties_test .
``` 
2. 
```bash
docker run -p 8000:8000 properties_test
```

como un ejemplo de este luego de ejecutarlo, puedes dirigirte  al siguiente enlace:

http://localhost:8000/properties?status=en_venta

## Autor

- Nombre: [Sofia Giraldo Sanchez]
- Correo Electrónico: [sgiraldos1@eafit.edu.co]
