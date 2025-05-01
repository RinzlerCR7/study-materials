# Moving Assets to separate Database Domains

This program moves the Snowflake assets (which are ingested in a single domain) into separate domains based on the database the assets belong to.

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
    "targetCommunityId": "<target-community-id>"
}
```

- `<collibra-domain-name>`: This is the domain name of the collibra environment we will be using. Ex: `vertex-dev.collibra.com`.
- `<connection-name>`: This is the edge connection name given to the Snowflake connection.
- `<initial-domain-id>`: This is the id of the domain where the Snowflake assets were originally getting ingested.
- `<target-community-id>`: This is the id of the community where the Snowflake database domains will be created before moving the assets to their respective domains.

Step 3: Use the following command to run the program from the directory where `moveAssets.py` is located.
```bash
python moveAssets.py -c .json
```
