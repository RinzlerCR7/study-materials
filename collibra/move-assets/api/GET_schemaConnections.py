import requests
from requests.auth import HTTPBasicAuth
import logging

# GET/schemaConnections
def GET_schemaConnections(clbraDomain, usr, psswrd, schemaId):
    # Example base URL: https://vertex-dev.collibra.com/rest/catalogDatabase/v1/schemaConnections
    baseUrl = 'https://' + clbraDomain + '/rest/catalogDatabase/v1/schemaConnections'

    # Create the query parameters dictionary
    params = {
        'schemaId': schemaId
    }

    # params = {
    #     'dataConnectionId': dataConnectionId,
    #     'schemaId': schemaId,
    #     'limit': limit
    # }

    # Make the GET request
    return requests.get(baseUrl, params=params, auth=HTTPBasicAuth(usr, psswrd))
