# backend-technical-test
# Microservicios de Consulta y "Me Gusta" de Inmuebles

Este proyecto implementa dos microservicios para la plataforma Habi, que permite a los usuarios consultar propiedades disponibles para la venta y dar "Me gusta" a propiedades específicas.

## Tecnologías Utilizadas

- Python 3
- Bibliotecas de Python: `http.server`, `json`, `unittest`, `mock`
- Base de datos PostgreSQL

## Descripción del Proyecto

Habi desea proporcionar una herramienta donde los usuarios puedan consultar propiedades disponibles para la venta, aplicando varios filtros como año de construcción, ciudad y estado. Además, los usuarios pueden dar "Me gusta" a propiedades específicas para mantener un ranking interno de propiedades más llamativas.

## Requerimientos Funcionales

### Microservicio de Consulta

- Los usuarios pueden consultar propiedades con los estados: "pre_venta", "en_venta" y "vendido".
- Los usuarios pueden filtrar propiedades por año de construcción, ciudad y estado.
- Los usuarios pueden aplicar múltiples filtros en la misma consulta.
- Los usuarios pueden ver la dirección, ciudad, estado, precio de venta y descripción de las propiedades.

### Microservicio de "Me Gusta"

- Los usuarios pueden dar "Me gusta" a una propiedad específica.
- Los "Me gusta" son de usuarios registrados y se registran en la base de datos.

## Estructura del Proyecto

- `src/`: Directorio principal que contiene el código fuente del proyecto.
    - `controllers/`: Controladores para manejar solicitudes HTTP.
    - `services/`: Servicios para la lógica de negocio.
    - `config/`: Configuración del proyecto, incluyendo la conexión a la base de datos.
- `tests/`: Directorio que contiene pruebas unitarias para el código.
- `README.md`: Este archivo.

## Ejecución de las Pruebas Unitarias

Para ejecutar las pruebas unitarias, asegúrate de tener Python 3 instalado y las dependencias necesarias. Luego, puedes ejecutar el siguiente comando en la terminal:

python -m unittest discover

csharp
Copy code

Esto buscará automáticamente todos los archivos de pruebas en el proyecto y los ejecutará, mostrando los resultados en la terminal.

## Diagrama de Entidad-Relación (ER)

![Diagrama ER](diagrama_er.png)

El diagrama muestra la estructura de la base de datos extendida para soportar la funcionalidad de "Me Gusta" en el servicio correspondiente.

## Autor

- Nombre: [Tu Nombre]
- Correo Electrónico: [tu.email@example.com]
