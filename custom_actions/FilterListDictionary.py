from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry

@registry.register(
    default_title="Filter list of dictionaries",
    description="Get an item in the list of dictionaries",
    display_group="Utils",
    namespace="integrations.utils",
)

def filter_listDict(
    list: Annotated[list, Field(..., description="list to filter")],
    key: Annotated[str, Field(..., description="value to search")],
    value: Annotated[str, Field(..., description="value to search")],
    ) -> dict:

    for item in list:
      if item.get(key) == value

    return item
