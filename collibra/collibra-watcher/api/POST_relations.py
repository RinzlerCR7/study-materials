import requests
from requests.auth import HTTPBasicAuth
import logging

# POST/relations
def POST_relations(clbraDomain, usr, psswrd, sourceId, targetId, typePublicId):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/relations
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/relations'

    # Create the json parameters dictionary
    json = {
        'sourceId': sourceId,
        'targetId': targetId,
        'typePublicId': typePublicId
    }

    # Make the POST request
    return requests.post(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
