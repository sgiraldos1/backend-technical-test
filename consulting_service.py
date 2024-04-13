# created code by Sofia Giraldo Sanchez- 04/13/24 

#the required libraries are imported 

import http.server
import socketserver
import mysql.connector
import json

#database conection with Mysql 

def db_connection():
    conect = mysql.connector.connect(
        host="<3.138.156.32>",
        port="<3309>",
        database="<habi_db>",
        user="<pruebas>",
        password="<VGbt3Day5R>"
    )
    return conect

# property query function


def get_properties(year, city, status):
    conect= db_connection()
    cursor = conect.cursor()

    # Load filters from JSON file

    with open('property_filters.json', 'r') as f:
        filters = json.load(f)['property_filters']

    # SQL query using filters
    query = """
        SELECT  city,year, status
        FROM property
        WHERE status = %(status)s
        AND city = %(city)s
        AND year = %(year)s
    """
    cursor.execute(query, filters)

    # Mapping the results to objects of the real estate class

    property = [get_properties(*row) for row in cursor]

    conect.close()
    return property


# endpoint REST

class PropertyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/properties'):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Obtain query parameters
            query_params = self.path.split('?')[1].split('&')
            year = [int(param.split('=')[1]) for param in query_params if param.startswith('year')]
            city = [param.split('=')[1] for param in query_params if param.startswith('city')]
            status = [param.split('=')[1] for param in query_params if param.startswith('status')]

            # Calling the function
            property = property(year, city, status)
            response_data = [property.__dict__ for property in property]
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

