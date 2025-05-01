import requests
from requests.auth import HTTPBasicAuth
import logging

# POST/auth/sessions
def POST_auth_sessions(clbraDomain, usr, psswrd):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/auth/sessions
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/auth/sessions'

    # Create the json parameters dictionary
    json = {
        'username': usr,
        'password': psswrd
    }

    # Make the POST request
    return requests.post(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
