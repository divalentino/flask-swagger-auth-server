#!/usr/bin/env python3                                   

import connexion
import sqlite3
from swagger_server import encoder

from swagger_server.security_util import User,authenticate,identity

from flask_jwt import JWT           

#def main():
app = connexion.App(__name__, specification_dir='./swagger/')
app.debug = True                                     
app.app.json_encoder = encoder.JSONEncoder           
app.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore - OpenAPI 3.0'}, pythonic_params=True)

app.app.config['SECRET_KEY'] = 'super-secret'        
app.app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'  

jwt = JWT(app.app, authenticate, identity)           

    # app.run(port=8080)

# if __name__ == '__main__':
#     main()
