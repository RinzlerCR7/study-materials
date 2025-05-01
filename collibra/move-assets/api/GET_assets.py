import requests
from requests.auth import HTTPBasicAuth
import logging

# GET/assets
def GET_assets(clbraDomain, usr, psswrd, name, nameMatchMode, domainId, typePublicIds='', limit=0):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/assets
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/assets'

    # Create the query parameters dictionary
    params = {
        'limit': limit,
        'name': name,
        'nameMatchMode': nameMatchMode,
        'domainId': domainId,
        'typePublicIds': typePublicIds
    }

    # Make the GET request
    return requests.get(baseUrl, params=params, auth=HTTPBasicAuth(usr, psswrd))
