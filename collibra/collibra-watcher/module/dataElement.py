class DataElement:
    def __init__(self, asset):
        self.__DE, self.__sourcesDEs, self.__targetsDEs, self.__representedByBAs = getDataElementInfo(asset)

    def getDE(self):
        return self.__DE

    def getSourcesDEs(self):
        return self.__sourcesDEs

    def getTargetsDEs(self):
        return self.__targetsDEs

    def getRepresentedByBAs(self):
        return self.__representedByBAs

# Returns incoming relation asset ids their respective domain ids.
def getDataElementInfo(asset):
    # id = asset["id"]
    dataElement = (asset["id"], asset["displayName"])

    # Set will contain the asset info.
    srcDataElements = set()
    tgtDataElements = set()
    srcBusinessAssets = set()

    for relation in asset["incomingRelations"]:
        if relation["type"]["publicId"] == "BusinessAssetRepresentsDataAsset":
            srcBusinessAssets.add((
                relation["source"]["id"],
                relation["source"]["displayName"],
                relation["source"]["domain"]["id"]
            ))
        elif relation["type"]["publicId"] == "DataElementTargetsDataElement":
            srcDataElements.add((
                relation["source"]["id"],
                relation["source"]["displayName"]
            ))

    for relation in asset["outgoingRelations"]:
        if relation["type"]["publicId"] == "DataElementTargetsDataElement":
            tgtDataElements.add((
                relation["target"]["id"],
                relation["target"]["displayName"]
            ))

    return dataElement, srcDataElements, tgtDataElements, srcBusinessAssets

# ***ARCHIVE***

# from api.graphQL import getIncomingRelationAssets
# from api.graphQL import getOutgoingRelationAssets

# # Returns incoming relation asset ids.
# def getIncomingRelationAssetIds(clbraDomain, usr, psswrd, id, publicId):
#     response = getIncomingRelationAssets(clbraDomain, usr, psswrd, id, publicId).json()

#     assetIds = set()

#     for relation in response["data"]["assets"][0]["incomingRelations"]:
#         assetIds.add(relation["source"]["id"])

#     return assetIds

# # Returns outgoing relation asset ids.
# def getOutgoingRelationAssetIds(clbraDomain, usr, psswrd, id, publicId):
#     response = getOutgoingRelationAssets(clbraDomain, usr, psswrd, id, publicId).json()

#     assetIds = set()

#     for relation in response["data"]["assets"][0]["outgoingRelations"]:
#         assetIds.add(relation["target"]["id"])

#     return assetIds
