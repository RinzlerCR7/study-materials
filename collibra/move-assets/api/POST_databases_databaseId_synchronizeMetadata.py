import requests
from requests.auth import HTTPBasicAuth
import logging

# POST/databases/{databaseId}/synchronizeMetadata
def POST_databases_databaseId_synchronizeMetadata(clbraDomain, usr, psswrd, databaseId, schemaConnectionIds):
    # Example base URL: https://vertex-dev.collibra.com/rest/catalogDatabase/v1/databases/
    # 3fa85f64-5717-4562-b3fc-2c963f66afa6/synchronizeMetadata
    baseUrl = 'https://' + clbraDomain + '/rest/catalogDatabase/v1/databases/' + databaseId + '/synchronizeMetadata'

    # Create the json parameters dictionary
    json = {
        'schemaConnectionIds': schemaConnectionIds
    }

    # Make the POST request
    return requests.post(baseUrl, json=json, auth=HTTPBasicAuth(usr, psswrd))
