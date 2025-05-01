# Watcher Script

This program checks & links source & target Data Element with a Business Asset.

## Steps for running the program

Step 1: Create a community where the database domains will be created.

Step 2: Create or update the `.json` config file:
```json
{
    "collibraDomain": "<collibra-domain-name>",
    "username": "<username>",
    "password": "<password>",
    "connectionName": "<connection-name>",
    "initialDomainId": "<initial-domain-id>",
    "targetCommunityId": "<target-community-id>",
    "startDate": "<yyyy-MM-ddThh:mm:ss+Z>",
    "endDate": "<yyyy-MM-ddThh:mm:ss+Z>"
}
```

- `<collibra-domain-name>`: This is the domain name of the collibra environment we will be using. Ex: `vertex-dev.collibra.com`.
- `<connection-name>`: This is the edge connection name given to the Snowflake connection.
- `<initial-domain-id>`: This is the id of the domain where the Snowflake assets were originally getting ingested.
- `<target-community-id>`: This is the id of the community where the Snowflake database domains will be created before moving the assets to their respective domains.

Step 3: Use the following command to run the program from the directory where `moveAssets.py` is located.
```bash
python main.py -c .json
```
