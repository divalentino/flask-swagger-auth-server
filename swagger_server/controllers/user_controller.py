import json

import connexion
import requests
import six

from flask import request,Response

import base64
import sqlite3

from swagger_server.models.new_password import NewPassword  # noqa: E501
from swagger_server import util


def reset_password_put(body=None):  # noqa: E501
    """Reset a user password

    Reset a user password # noqa: E501

    :param body: New password
    :type body: dict | bytes

    :rtype: None
    """
    
    # Necessarily have to assume that passwords CAN contain colons,
    # but usernames CANNOT
    user_pw = base64.b64decode(connexion.request.headers['Authorization'].split("Basic ")[1])
    user    = str(user_pw.decode()).split(":")[0]
    
    if connexion.request.is_json:
        body = NewPassword.from_dict(connexion.request.get_json())  # noqa: E501

    new_pw = body.new_password
    if new_pw is None:
        return Response("No new password specified",status=400)

    # Reset password in SQLite database, take username from header
    with sqlite3.connect("users.db") as con:      
        cmd = """
                    UPDATE users
                    SET password='%s'
                    WHERE
                    username='%s'
                    """%(new_pw,user)
        cur = con.cursor()
        cur.execute(cmd)
        con.commit()
        
    return Response("Password updated",status=200) #'do some magic!'


def token_get():  # noqa: E501
    """Retrieve a Bearer token

    Retrieve a Bearer token # noqa: E501


    :rtype: None
    """
   
    # Necessarily have to assume that passwords CAN contain colons,
    # but usernames CANNOT
    user_pw = base64.b64decode(request.headers['Authorization'].split("Basic ")[1])
    user    = str(user_pw.decode()).split(":")[0]
    pw      = "".join(str(user_pw.decode()).split(":")[1:])
    
    # print(user,pw)
    
    # Send request to JWT /auth endpoint.
    r = requests.post("http://localhost:8080/auth",json={"username":user,"password":pw},headers={"Content-Type":"application/json"})
    
    return Response(r.text,status=r.status_code)
    
    return 'do some magic!'
