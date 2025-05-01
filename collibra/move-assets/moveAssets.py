import requests
import json
from argparse import ArgumentParser

from api.GET_assets import GET_assets
from api.GET_domains import GET_domains
from api.GET_schemaConnections import GET_schemaConnections
from api.POST_domains import POST_domains
# from api.POST_schemaMetadataConfigurations import POST_schemaMetadataConfigurations
from api.POST_databases_databaseId_synchronizeMetadata import POST_databases_databaseId_synchronizeMetadata
from api.PATCH_assets_assetId import PATCH_assets_assetId
from api.PUT_schemaMetadataConfigurations_schemaConnectionId import PUT_schemaMetadataConfigurations_schemaConnectionId
from helper.idValidation import idValidation

if __name__ == "__main__":
    # Set up argument parsing
    parser = ArgumentParser(description='Process a JSON file.')
    parser.add_argument('-c', '--config', type=str, help='Path to the JSON file.')

    # Parse the arguments
    args = parser.parse_args()

    # Read and parse the JSON file
    with open(args.config, 'r') as file:
        data = json.load(file)

    clbraDomain = data['collibraDomain']
    usr = data['username']
    psswrd = data['password']
    connectionName = data['connectionName']
    initialDomainId = data['initialDomainId']
    targetCommunityId = data['targetCommunityId']

    # Id validation
    idValidation(clbraDomain, usr, psswrd)

    # Looking for DBs.
    response = GET_assets(clbraDomain, usr, psswrd, connectionName, 'START', initialDomainId, 'Database')

    while response.json()['total'] > 0:
        dbAssets = response.json()['results']

        for dbAsset in dbAssets:
            dbName = dbAsset['displayName']

            # Check if the DB has corresponding domain in the target community. If not, create it.
            response = GET_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)

            if response.json()['total'] == 0:
                response = POST_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)
                targetDomainId = response.json()['id']
            else:
                targetDomainId = response.json()['results'][0]['id']

            # Find the schemas that were synchronized under the current DB.
            response = GET_assets(clbraDomain, usr, psswrd, dbAsset['name'], 'START', initialDomainId, 'Schema')
            schemaAssets = response.json()['results']

            # If the asset is a schema, update the schema configuration.
            schemaConnectionIds = []

            for schemaAsset in schemaAssets:
                response = GET_schemaConnections(clbraDomain, usr, psswrd, schemaAsset['id'])
                schemaConnection = response.json()['results'][0]
                response = PUT_schemaMetadataConfigurations_schemaConnectionId(clbraDomain, usr, psswrd,
                schemaConnection['id'], targetDomainId)

                schemaConnectionIds.append(schemaConnection['id'])

            # Sync the schemas under the current DB.
            response = POST_databases_databaseId_synchronizeMetadata(clbraDomain, usr, psswrd, dbAsset['id'],
            schemaConnectionIds)

            # Move DB Asset to the target domain.
            response = PATCH_assets_assetId(clbraDomain, usr, psswrd, dbAsset['id'], targetDomainId)

            print('Moving assets of ' + dbName + '.')

        response = GET_assets(clbraDomain, usr, psswrd, connectionName, 'START', initialDomainId, 'Database')

    print('All jobs for moving ' + connectionName + ' assets have been started.')

    # Looking for Schemas.
    # response = GET_assets(clbraDomain, usr, psswrd, connectionName, initialDomainId, 'Schema')

    # while response.json()['total'] > 0:
    #     schemaAssets = response.json()['results']

    #     for schemaAsset in schemaAssets:
    #         nameSplit = schemaAsset['name'].split('>')

    #         if len(nameSplit) > 1:
    #             dbName = nameSplit[1]
    #         else:
    #             continue

    #         # Check if the DB even exists.


    #         # Check if the DB has corresponding domain in the target community. If not, create it.
    #         response = GET_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)

    #         if response.json()['total'] == 0:
    #             response = POST_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)
    #             targetDomainId = response.json()['id']
    #         else:
    #             targetDomainId = response.json()['results'][0]['id']

    #         # Move asset to the target domain.
    #         response = PATCH_assets_assetId(clbraDomain, usr, psswrd, asset['id'], targetDomainId)

    #         # If the asset is a schema, update the schema configuration.
    #         if asset['type']['name'] == 'Schema':
    #             response = GET_schemaConnections(clbraDomain, usr, psswrd, asset['id'])
    #             schemaConnection = response.json()['result'][0]

    #             response = POST_schemaMetadataConfigurations(clbraDomain, usr, psswrd, schemaConnection['id'], targetDomainId)

    #     response = GET_assets(clbraDomain, usr, psswrd, connectionName, initialDomainId)
