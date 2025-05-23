# Example 1

Note: Below are my experiments with Output Module. I've just learned it in past 2 days, so there might be errors.

Note: A lot of the stuff is hardcoded below, so it might not work in future or work very slow if the amount of data it is grabbing has increased.

* Returns upto 5 resources.
* I'm asking for assets as resources.
* Assets will display assetId, assetName (fullname), assetTypeId, createdOn, tgtRelations & srcRelations.
* Assets will get filtered on assetTypeId (00000000-0000-0000-0000-000000031008), createdOn (>= 1742812744673) & tgtRelationTypeId (atleast 1 should be 00000000-0000-0000-0000-000000007038).

## Query

```json
{
    "ViewConfig": {
		"displayLength": "5",
        "Resources": {
            "Asset": {
                "Id": { "name": "assetId" },
				"Signifier": { "name": "assetName" },
				"AssetType": {
					"Id": { "name": "assetTypeId" }
				},
				"Relation": [
					{
						"name": "tgtRelations",
						"type": "TARGET",
						"RelationType": { 
							"Id": { "name": "tgtRelationTypeId" }
						}
					},
					{
						"name": "srcRelations",
						"type": "SOURCE",
						"RelationType": { 
							"Id": { "name": "srcRelationTypeId" }
						}
					}
				],
				"CreatedOn": { "name": "createdOn" },
				"Filter": {
					"AND": [
						{ "Field": { "name": "assetTypeId", "operator": "EQUALS", "value": "00000000-0000-0000-0000-000000031008" } },
						{ "Field": { "name": "createdOn", "operator": "GREATER_OR_EQUALS", "value": "1742812744673" } },
						{ "Field": { "name": "tgtRelationTypeId", "operator": "EQUALS", "value": "00000000-0000-0000-0000-000000007038" } }
					]
				}
            }
        }
    }
}
```

## Output

```json
{
    "view": {
        "Asset0": [{
                "assetId": "0195ccbb-fdb0-79d9-9b6b-3009a7f51239",
                "assetName": "col_2",
                "createdOn": 1742896627120,
                "AssetType1": [{
                        "assetTypeId": "00000000-0000-0000-0000-000000031008"
                    }
                ],
                "tgtRelations": [{
                        "RelationType2": [{
                                "tgtRelationTypeId": "00000000-0000-0000-0000-000000007038"
                            }
                        ]
                    }, {
                        "RelationType2": [{
                                "tgtRelationTypeId": "00000000-0000-0000-0000-000000007069"
                            }
                        ]
                    }
                ]
            }, {
                "assetId": "0195cdcb-ea02-7ed8-ae36-8b2d9b8cb5ba",
                "assetName": "DAVE_TEST1",
                "createdOn": 1742914447874,
                "AssetType1": [{
                        "assetTypeId": "00000000-0000-0000-0000-000000031008"
                    }
                ],
                "tgtRelations": [{
                        "RelationType2": [{
                                "tgtRelationTypeId": "00000000-0000-0000-0000-000000007038"
                            }
                        ]
                    }
                ],
                "srcRelations": [{
                        "RelationType3": [{
                                "srcRelationTypeId": "00000000-0000-0000-0000-000000007069"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```
