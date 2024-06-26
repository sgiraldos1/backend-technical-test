import json
from http.server import BaseHTTPRequestHandler

from src.services.consulting_service import get_properties


class PropertyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/properties"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            # Get the query params
            if self.path.__contains__("?"):
                query_params = self.path.split("?")[1].split("&")
                construction_year = [
                    int(param.split("=")[1])
                    for param in query_params
                    if param.startswith("construction_year")
                ] 
                construction_year= construction_year[0] if construction_year else None
                city = [
                    param.split("=")[1]
                    for param in query_params
                    if param.startswith("city")
                ]
                city= city[0] if city else None
                status = [
                    param.split("=")[1]
                    for param in query_params
                    if param.startswith("status")
                ]
                status= status[0] if status else None
                
            else:
             construction_year,city,status =None, None, None
          
            # Call the function to get the properties
            properties = get_properties(construction_year, city, status)
            self.wfile.write(json.dumps(properties).encode())
        
        else:
            self.send_response(404)
            self.end_headers()
