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
    list: Annotated[Any, Field(..., description="list to filter")],
    key: Annotated[Any, Field(..., description="key to target")],
    value: Annotated[Any, Field(..., description="value to search")]
    ) -> dict:

    for item in list:
      if item.get(key) == value:
        return item

    return []
