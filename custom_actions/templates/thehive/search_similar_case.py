from typing import Annotated, Any
from pydantic import Field
from tracecat_registry import RegistrySecret, registry, secrets
import requests
import json

thehive_secret = RegistrySecret(
    name="thehive4",
    keys=["apikey", "url"],
)

@registry.register(
    default_title="Search similar case",
    description="Search for the most recent similar case from an alert on TheHive",
    display_group="TheHive",
    namespace="integration.",
    secrets=[thehive_secret],
)

baseUrl=secrets.get("url")
apikey=secrets.get("apikey")
headers = {"Content-Type":"application/json", "Authorization":f"Bearer {apikey}"}

async def search_similar_case(
    alert_id: Annotated[
        str,
        Field(
            ...,
            description="Alert ID from TheHive",
        ),
    ],
      search_time: Annotated[
        int,
        Field(
            ...,
            description="Search time on created case",
        ),
    ],
) -> dict[str, Any]:
    apiPath = "/api/v1/query"
    url = baseUrl + apiPath
    caseToMerge = None
    query = {"query":[{"_name":"getAlert","idOrName":alert_id},{"_name":"similarCases","caseFilter":{"_and":[{"_field":"status","_value":"Open"},{"_gt":{"_createdAt":search_time}}]}}]}
    query_string = json.dumps(query)
    similar_cases = requests.post(url, headers=headers, data=query_string)
    similar_cases = similar_cases.json()
    for case in similar_cases:
      if case['observableTypes']['cmdline'] == 1
        caseToMerge = case
        break

    return caseToMerge
