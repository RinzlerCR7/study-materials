import requests
from requests.auth import HTTPBasicAuth
import logging

# POST/domains
def POST_domains(clbraDomain, usr, psswrd, name, communityId):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/domains
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/domains'

    # Create the json parameters dictionary
    json = {
        'name': name,
        'communityId': communityId,
        'typePublicId': 'PhysicalDataDictionary'
    }

    # Make the POST request
    return requests.post(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
