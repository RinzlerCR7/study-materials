import json
import logging
from argparse import ArgumentParser
from datetime import date

from module.dataElement import DataElement
from module.mailer import sendMail
from api.graphQL import getBArepresentsDE
from api.graphQL import getDataElementAndRelations
from api.graphQL import getDataElementsAndRelations
from api.graphQL import getDomainRoles
from api.POST_relations import POST_relations

from module.idValidation import idValidation

def main():
    logFile = 'logs/db_assets_creation_' + str(date.today()) + '.log'
    logging.basicConfig(filename=logFile, format='%(asctime)s %(message)s', filemode='a', level=logging.INFO)

    # Logging start
    logging.info('Logging start.')

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
    startDate = str()
    endDate = str()

    # Id validation
    idValidation(clbraDomain, usr, psswrd)

    # Find startDate & endDate.
    if ('startDate' in data and 'endDate' in data) and (data['startDate'] != '' and data['endDate'] != ''):
        startDate = data['startDate']
        endDate = data['endDate']
    else:
        dayMinus1 = datetime.now() - timedelta(days=1)
        dayMinus2 = datetime.now() - timedelta(days=2)
        # now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S%z')

        endDate = dayMinus1.strftime('%Y-%m-%dT00:00:00+00:00')
        startDate = dayMinus2.strftime('%Y-%m-%dT00:00:00+00:00')

    response = getDataElementsAndRelations(clbraDomain, usr, psswrd, startDate, endDate).json()

    # Make a set of DataElement(s) that recently got a "Business Asset represents Data Asset" relation.
    dataElements = set()

    for asset in response["data"]["assets"]:
        dataElement = DataElement(asset)
        dataElements.add(dataElement)

    # Issue tracker will collect all the conflicts. Format of storing issues is as following:
    # {"Domain id": set( ( ("Data Element id", "Data Element name"), "Issue") )}
    issueTracker = dict()

    for dataElement in dataElements:
        print("DE: " + str(dataElement.getDE()))
        print("DE targets DEs: " + str(dataElement.getTargetsDEs()))
        print("DE sources DEs: " + str(dataElement.getSourcesDEs()))
        print("DE is represented by BAs: " + str(dataElement.getRepresentedByBAs()))

        # headDE & tailDE will store ("Asset id", "Asset name").
        # headBA & tailBA will store ("Asset id", "Asset name", "Domain id").
        headDE = headBA = tailDE = tailBA = None

        # Path will decide the direction in which the "while" loop will go in the lineage.
        # "" --> Not set.
        # "back" --> loop will go back in the lineage.
        # "frwd" --> loop will go frwd in the lineage.
        path = ""

        while True:
            if len(dataElement.getRepresentedByBAs()) > 1:
                logging.warning("More than one Business Asset assigned to one Data Element.")
                break
            elif len(dataElement.getRepresentedByBAs()) == 1:
                if len(dataElement.getTargetsDEs()) > 1 or len(dataElement.getSourcesDEs()) > 1:
                    logging.warning("One Data Element either sources or targets multiple Data Elements.")
                    break
                elif len(dataElement.getTargetsDEs()) == 1 and len(dataElement.getSourcesDEs()) == 1:
                    logging.warning((
                        "Business Asset is linked to a Data Element that is neither a source nor a target Data Element."
                        " Please check if the source & target Data Element have Business Asset linked."
                    ))
                    break
                elif len(dataElement.getTargetsDEs()) == 0 and len(dataElement.getSourcesDEs()) == 1:
                    tailDE = dataElement.getDE()
                    tailBA = next(iter(dataElement.getRepresentedByBAs()))

                    if headDE != None:
                        break

                    nxtSrcDataElementId = next(iter(dataElement.getSourcesDEs()))[0]
                    response = getDataElementAndRelations(clbraDomain, usr, psswrd, nxtSrcDataElementId).json()

                    dataElement = DataElement(response["data"]["assets"][0])
                    path = "back"
                    continue
                elif len(dataElement.getTargetsDEs()) == 1 and len(dataElement.getSourcesDEs()) == 0:
                    headDE = dataElement.getDE()
                    headBA = next(iter(dataElement.getRepresentedByBAs()))

                    if tailDE != None:
                        break

                    nxtTgtDataElementId = next(iter(dataElement.getTargetsDEs()))[0]
                    response = getDataElementAndRelations(clbraDomain, usr, psswrd, nxtTgtDataElementId).json()

                    dataElement = DataElement(response["data"]["assets"][0])
                    path = "frwd"
                    continue
                else:
                    # Not possible to get here.
                    # DE doesn't have any source/target DEs.
                    break
            else:
                if len(dataElement.getTargetsDEs()) > 1 or len(dataElement.getSourcesDEs()) > 1:
                    logging.warning("One Data Element either sources or targets multiple Data Elements.")
                    break
                elif len(dataElement.getTargetsDEs()) == 1 and len(dataElement.getSourcesDEs()) == 1:
                    if path == "frwd":
                        # Go forward.
                        nxtTgtDataElementId = next(iter(dataElement.getTargetsDEs()))[0]
                        response = getDataElementAndRelations(clbraDomain, usr, psswrd, nxtTgtDataElementId).json()

                        dataElement = DataElement(response["data"]["assets"][0])
                        continue
                    else:
                        # Go back.
                        nxtSrcDataElementId = next(iter(dataElement.getSourcesDEs()))[0]
                        response = getDataElementAndRelations(clbraDomain, usr, psswrd, nxtSrcDataElementId).json()

                        dataElement = DataElement(response["data"]["assets"][0])
                        continue
                elif len(dataElement.getTargetsDEs()) == 0 and len(dataElement.getSourcesDEs()) == 1:
                    # Found tail DE.
                    tailDE = dataElement.getDE()
                    break
                elif len(dataElement.getTargetsDEs()) == 1 and len(dataElement.getSourcesDEs()) == 0:
                    # Found head DE.
                    headDE = dataElement.getDE()
                    break
                else:
                    # Not possible to reach here.
                    # DE doesn't have any source/target DEs. DE doesn't even has a BA.
                    break

        # Setting up messages for each type of issue.
        if len(dataElement.getRepresentedByBAs()) > 1:
            for businessAsset in dataElement.getRepresentedByBAs():
                businessAssetDomainId = businessAsset[2]

                if businessAssetDomainId not in issueTracker:
                    issueTracker.update({businessAssetDomainId: set()})

                issueTracker[businessAssetDomainId].add((dataElement.getDE(),
                "More than one Business Asset assigned to one Data Element."))
        else:
            if len(dataElement.getTargetsDEs()) > 1 or len(dataElement.getSourcesDEs()) > 1:
                logging.warning("One Data Element either sources or targets multiple Data Elements.")
            elif len(dataElement.getTargetsDEs()) == 1 and len(dataElement.getSourcesDEs()) == 1:
                businessAsset = next(iter(dataElement.getRepresentedByBAs()))
                businessAssetDomainId = businessAsset[2]

                if businessAssetDomainId not in issueTracker:
                    issueTracker.update({businessAssetDomainId: set()})

                issueTracker[businessAssetDomainId].add((dataElement.getDE(), (
                    "Business Asset is linked to a Data Element that is neither a source nor a target Data Element. "
                    "Please check if the source Data Element & target Data Element have Business Asset linked."
                )))
            elif (headDE != None) and (headBA != None) and (tailDE != None) and (tailBA != None):
                if headBA == tailBA:
                    logging.info("Business Asset is linked correctly.")
                else:
                    headBADomainId = headBA[2]
                    tailBADomainId = tailBA[2]

                    if headBADomainId not in issueTracker:
                        issueTracker.update({headBADomainId: set()})

                    if tailBADomainId not in issueTracker:
                        issueTracker.update({tailBADomainId: set()})

                    issueTracker[headBADomainId].add((headDE, "Source & target Business Assets are conflicting"))
                    issueTracker[tailBADomainId].add((tailDE, "Source & target Business Assets are conflicting"))
            elif (headDE != None) and (headBA != None) and (tailDE != None):
                logging.info("Create relation: headBA represents tailDE.")

                response = POST_relations(clbraDomain, usr, psswrd, headBA[0], tailDE[0],
                "BusinessAssetRepresentsDataAsset").json()
                logging.info(response)
            elif (headDE != None) and (tailDE != None) and (tailBA != None):
                tailBADomainId = tailBA[2]

                if tailBADomainId not in issueTracker:
                    issueTracker.update({tailBADomainId: set()})

                issueTracker[tailBADomainId].add((headDE, "Source Data Element is missing a Business Asset."))
            elif (headDE != None) and (headBA != None):
                logging.warning("***NOT REACHABLE***")
            elif (tailDE != None) and (tailBA != None):
                logging.warning("***NOT REACHABLE***")
            else:
                logging.warning("DE either doesn't have any source/target DEs or have multiple source/target DEs.")

    # Sending email to the required Data Stewards.
    for domainId in issueTracker:
        response = getDomainRoles(clbraDomain, usr, psswrd, domainId, "Data Steward").json()
        dataStewardMailIds = list()

        for role in response["data"]["domains"][0]["responsibilities"]:
            dataStewardMailIds.append(role["user"]["email"])

        sendMail(clbraDomain, dataStewardMailIds, issueTracker[domainId])

    # Logging end
    logging.info("Logging end.")

if __name__ == "__main__":
    main()
