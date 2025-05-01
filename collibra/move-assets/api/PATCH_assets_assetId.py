import requests
from requests.auth import HTTPBasicAuth
import logging

# PATCH/assets/{assetId}
def PATCH_assets_assetId(clbraDomain, usr, psswrd, assetId, domainId):
    # Example base URL: https://vertex-dev.collibra.com/rest/2.0/assets/72d2f81f-64b5-43e5-b63c-8166d9c84427
    baseUrl = 'https://' + clbraDomain + '/rest/2.0/assets/' + assetId

    # # Create the query parameters dictionary
    # params = {
    #     'dataConnectionId': dataConnectionId,
    #     'schemaId': schemaId,
    #     'limit': limit
    # }

    # Create the json parameters dictionary
    json = {
        'domainId': domainId
    }

    # Make the PATCH request
    return requests.patch(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
