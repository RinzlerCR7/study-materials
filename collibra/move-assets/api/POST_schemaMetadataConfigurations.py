import requests
from requests.auth import HTTPBasicAuth
import logging

# POST/schemaMetadataConfigurations
def POST_schemaMetadataConfigurations(clbraDomain, usr, psswrd, schemaConnectionId, targetDomainId):
    # Example base URL: https://vertex-dev.collibra.com/rest/catalogDatabase/v1/schemaMetadataConfigurations
    baseUrl = 'https://' + clbraDomain + '/rest/catalogDatabase/v1/schemaMetadataConfigurations'

    # Create the json parameters dictionary
    json = {
        'schemaConnectionId': schemaConnectionId,
        'synchronizationRules': [
            {
                'include': '*',
                'targetDomainId': targetDomainId
            }
        ]
    }

    # Make the POST request
    return requests.post(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
