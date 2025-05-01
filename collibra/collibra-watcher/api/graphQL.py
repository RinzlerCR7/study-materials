import requests
from requests.auth import HTTPBasicAuth
import logging

# Takes a data element id & returns it's related assets.
def getDataElementAndRelations(clbraDomain, usr, psswrd, assetId):
    # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
    baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

    # Create the json parameters dictionary
    query = f'''
    {{
        assets(where: {{ id: {{ eq: "{assetId}" }} }}) {{
            id
            displayName
            incomingRelations {{
                id
                type {{
                    publicId
                }}
                source {{
                    id
                    displayName
                    domain {{
                        id
                        name
                    }}
                }}
            }}
            outgoingRelations {{
                id
                type {{
                    publicId
                }}
                target {{
                    id
                    displayName
                }}
            }}
        }}
    }}
    '''

    # Make the POST request
    return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))


# Takes a start date & end date & returns the assets satisfying the condition in that timeframe.
def getDataElementsAndRelations(clbraDomain, usr, psswrd, startDate, endDate):
    # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
    baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

    # Create the json parameters dictionary
    query = f'''
    {{
        assets(
            where: {{
                incomingRelations: {{
                    any: {{
                        createdOn: {{
                            gte: "{startDate}"
                            lt: "{endDate}"
                        }}
                        type: {{ publicId: {{ eq: "BusinessAssetRepresentsDataAsset" }} }}
                    }}
                }}
                _or: [
                    {{
                        outgoingRelations: {{
                            typePublicId: "DataElementTargetsDataElement"
                            empty: false
                        }}
                    }}
                    {{
                        incomingRelations: {{
                            typePublicId: "DataElementTargetsDataElement"
                            empty: false
                        }}
                    }}
                ]
            }}
        ) {{
            id
            displayName
            incomingRelations {{
                id
                type {{
                    publicId
                }}
                source {{
                    id
                    displayName
                    domain {{
                        id
                        name
                    }}
                }}
            }}
            outgoingRelations {{
                id
                type {{
                    publicId
                }}
                target {{
                    id
                    displayName
                }}
            }}
        }}
    }}
    '''

    # Make the POST request
    return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))


# Get the roles assigned to a particular domain.
def getDomainRoles(clbraDomain, usr, psswrd, id, roleName):
    # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
    baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

    # Create the json parameters dictionary
    query = f'''
    {{
        domains(where: {{ id: {{ eq: "{id}" }} }}) {{
            id
            name
            responsibilities(where: {{ role: {{ name: {{ eq: "{roleName}" }} }} }}) {{
                id
                role {{
                    name
                }}
                user {{
                    id
                    fullName
                    email
                }}
            }}
        }}
    }}
    '''

    # Make the POST request
    return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))

# ***ARCHIVE***

# def getBArepresentsDE(clbraDomain, usr, psswrd, startDate, endDate, limit=5):
#     # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
#     baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

#     # Create the json parameters dictionary
#     query = f'''
#     {{
#         assets(
#             limit: {limit}
#             where: {{
#                 type: {{ publicId: {{ eq: "BusinessTerm" }}}}
#                 outgoingRelations: {{
#                     any: {{
#                         createdOn: {{
#                             gte: "{startDate}"
#                             lt: "{endDate}"
#                         }}
#                         type: {{ publicId: {{ eq: "BusinessAssetRepresentsDataAsset" }}}}
#                     }}
#                 }}
#             }}
#         ) {{
#             id
#             displayName
#             outgoingRelations {{
#                 id
#                 type {{
#                     publicId
#                 }}
#                 target {{
#                     id
#                     displayName
#                 }}
#             }}
#         }}
#     }}
#     '''

#     # Make the POST request
#     return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))

# def getIncomingRelationAssets(clbraDomain, usr, psswrd, id, publicId):
#     # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
#     baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

#     # Create the json parameters dictionary
#     query = f'''
#     {{
#         assets(where: {{ id: {{ eq: "{id}" }} }}) {{
#             id
#             displayName
#             incomingRelations(
#                 where: {{ type: {{ publicId: {{ eq: "{publicId}" }} }} }}
#             ) {{
#                 type {{
#                     publicId
#                 }}
#                 source {{
#                     id
#                     displayName
#                 }}
#             }}
#         }}
#     }}
#     '''

#     # Make the POST request
#     return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))

# def getOutgoingRelationAssets(clbraDomain, usr, psswrd, id, publicId):
#     # Example base URL: https://vertex-dev.collibra.com/graphql/knowledgeGraph/v1
#     baseUrl = 'https://' + clbraDomain + '/graphql/knowledgeGraph/v1'

#     # Create the json parameters dictionary
#     query = f'''
#     {{
#         assets(where: {{ id: {{ eq: "{id}" }} }}) {{
#             id
#             displayName
#             outgoingRelations(
#                 where: {{ type: {{ publicId: {{ eq: "{publicId}" }} }} }}
#             ) {{
#                 type {{
#                     publicId
#                 }}
#                 target {{
#                     id
#                     displayName
#                 }}
#             }}
#         }}
#     }}
#     '''

#     # Make the POST request
#     return requests.post(baseUrl, json={"query": query}, auth=HTTPBasicAuth(usr, psswrd))
