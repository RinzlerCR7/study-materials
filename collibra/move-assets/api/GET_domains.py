import requests
from requests.auth import HTTPBasicAuth
import logging

# GET/domains
def GET_domains(clbraDomain, usr, psswrd, name, communityId):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/domains
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/domains'

    # Create the query parameters dictionary
    params = {
        'name': name,
        'nameMatchMode': 'EXACT',
        'communityId': communityId,
        'typePublicId': 'PhysicalDataDictionary'
    }

    # Make the GET request
    return requests.get(baseUrl, params=params, auth=HTTPBasicAuth(usr, psswrd))
