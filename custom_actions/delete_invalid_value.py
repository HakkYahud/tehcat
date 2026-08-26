from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
from time import sleep
import re

@registry.register(
    default_title="Delete Invalid Value",
    description="Delete empty or non-correlable value",
    display_group="Utils",
    namespace="integrations.utils",
)

def delete_invalid_value(
    data: Annotated[list, Field(..., description="List of data")],
    dataType: Annotated[list, Field(..., description="List of data type")],
    ) -> list:

    for index, value in enumerate(data):
      if re.search(r"\{\{.*\}\}", value):
        data.pop(index)
        dataType.pop(index)
      elif value == "":
        data.pop(index)
        dataType.pop(index)
    
    return data, dataType
