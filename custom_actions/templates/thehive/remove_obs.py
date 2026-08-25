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
    default_title="Clean Observables",
    description="Remove irrelevant observables of a case on TheHive",
    display_group="TheHive",
    namespace="integration.thehive",
    secrets=[thehive_secret],
)

async def clean_observable(
    case_id: Annotated[
        str,
        Field(
            ...,
            description="Case ID from TheHive",
        ),
    ],
) -> dict[str, Any]:
    baseUrl=secrets.get("url")
    apikey=secrets.get("apikey")
    headers = {"Content-Type":"application/json", "Authorization":f"Bearer {apikey}"}
    apiPath = "/api/v1/query"
    url = baseUrl + apiPath
    # Get Observable
    data = {"query":[{"_name":"getCase","idOrName":"~214036664"},{"_name":"observables"},{"_name":"sort","_fields":[{"startDate":"desc"}]}]}
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    
    for obs in r.json():
      apiPathObs = f"/api/case/artifact/{obs['_id']}"
      if re.search(r"\{\{.*?\}\}", i["data"]):
          print(f'Data removed: {i["data"]}')
          resp = requests.delete(url + apiPathObs, headers=headers)
          resp.raise_for_status()
      elif i["data"] == "": 
          print(f'Data removed: {i["data"]}')
          resp = requests.delete(url + apiPathObs, headers=headers)
          resp.raise_for_status()
      elif i["dataType"] == "filepath":
          print(f'Ignoring Similarities on {i["data"]}')
          data = {"ignoreSimilarity":True}
          resp = requests.patch(url + apiPathObs, json=data, headers=headers)
          resp.raise_for_status()
