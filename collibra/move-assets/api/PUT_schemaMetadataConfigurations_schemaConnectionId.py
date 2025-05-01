import requests
from requests.auth import HTTPBasicAuth
import logging

# PUT/schemaMetadataConfigurations/{schemaConnectionId}
def PUT_schemaMetadataConfigurations_schemaConnectionId(clbraDomain, usr, psswrd, schemaConnectionId, targetDomainId):
    # Example base URL: https://vertex-dev.collibra.com/rest/catalogDatabase/v1/schemaMetadataConfigurations/
    # 3fa85f64-5717-4562-b3fc-2c963f66afa6
    baseUrl = 'https://' + clbraDomain + '/rest/catalogDatabase/v1/schemaMetadataConfigurations/' + schemaConnectionId

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

    # Make the PUT request
    return requests.put(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
