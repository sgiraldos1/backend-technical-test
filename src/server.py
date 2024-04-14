from http.server import HTTPServer

from src.controllers.property_controller import PropertyHandler


def start():
    PORT = 8000
    server = HTTPServer(("0.0.0.0", PORT), PropertyHandler)
    print(f"App is running at port {PORT}")
    server.serve_forever()
