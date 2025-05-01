import requests
from requests.auth import HTTPBasicAuth
import logging

# DELETE/auth/sessions/current
def DELETE_auth_sessions_current(clbraDomain, usr, psswrd):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/auth/sessions/current
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/auth/sessions/current'

    # Make the DELETE request
    return requests.delete(baseUrl, auth=HTTPBasicAuth(usr, psswrd))
