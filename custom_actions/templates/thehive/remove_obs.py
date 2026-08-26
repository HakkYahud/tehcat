from typing import Annotated, Any
from pydantic import Field
from tracecat_registry import RegistrySecret, registry, secrets
import requests
import json
import re

thehive_secret = RegistrySecret(
    name="thehive4",
    keys=["apikey", "url"],
)

@registry.register(
    default_title="Clean Observables",
    description="Remove irrelevant observables of the alert on TheHive",
    display_group="TheHive",
    namespace="integration.thehive",
    secrets=[thehive_secret],
)

async def clean_observable(
    alert_id: Annotated[
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
    data = {"query":[{"_name":"getAlert","idOrName":alert_id},{"_name":"observables"},{"_name":"sort","_fields":[{"startDate":"desc"}]},{"_name":"page","from":0,"to":15,"extraData":["seen"]}]}
    r = requests.post(url, headers=headers, json=data)
    r.raise_for_status()
    
    for obs in r.json():
      apiPathObs = f"/api/alert/artifact/{obs['_id']}"
      if re.search(r"\{\{.*?\}\}", obs["data"]):
          print(f'Data removed: {obs["data"]}')
          resp = requests.delete(url + apiPathObs, headers=headers)
          resp.raise_for_status()
      elif obs["data"] == "": 
          print(f'Data removed: {obs["data"]}')
          resp = requests.delete(url + apiPathObs, headers=headers)
          resp.raise_for_status()
      elif obs["dataType"] == "filepath":
          print(f'Ignoring Similarities on {obs["data"]}')
          data = {"ignoreSimilarity":True}
          resp = requests.patch(url + apiPathObs, json=data, headers=headers)
          resp.raise_for_status()
