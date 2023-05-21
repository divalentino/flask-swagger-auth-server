from typing import List

from swagger_server.security_util import authenticate

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_basicAuth(username, password, required_scopes):
    res = authenticate(username,password)
    if res is None:
        return res
    return {'test_key': 'test_value'}

def check_bearerAuth(token):
    return {'test_key': 'test_value'}


