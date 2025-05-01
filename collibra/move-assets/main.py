import requests
import json
from argparse import ArgumentParser

from api.GET_assets import GET_assets
from api.GET_domains import GET_domains
from api.GET_schemaConnections import GET_schemaConnections
from api.POST_domains import POST_domains
from api.POST_schemaMetadataConfigurations import POST_schemaMetadataConfigurations
from api.PATCH_assets_assetId import PATCH_assets_assetId
from helper.idValidation import idValidation

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

response = GET_assets(clbraDomain, usr, psswrd, connectionName, initialDomainId)

while response.json()['total'] > 0:
    results = response.json()['results']

    for asset in results:
        nameSplit = asset['name'].split('>')

        if len(nameSplit) > 1:
            dbName = nameSplit[1]
        else:
            continue

        # Check if the DB has corresponding domain in the target community. If not, create it.
        response = GET_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)

        if response.json()['total'] == 0:
            response = POST_domains(clbraDomain, usr, psswrd, dbName, targetCommunityId)
            targetDomainId = response.json()['id']
        else:
            targetDomainId = response.json()['results'][0]['id']

        # Move asset to the target domain.
        response = PATCH_assets_assetId(clbraDomain, usr, psswrd, asset['id'], targetDomainId)

        # If the asset is a schema, update the schema configuration.
        if asset['type']['name'] == 'Schema':
            response = GET_schemaConnections(clbraDomain, usr, psswrd, asset['id'])
            schemaConnection = response.json()['result'][0]

            response = POST_schemaMetadataConfigurations(clbraDomain, usr, psswrd, schemaConnection['id'], targetDomainId)

    response = GET_assets(clbraDomain, usr, psswrd, connectionName, initialDomainId)
