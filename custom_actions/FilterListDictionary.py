from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry


@registry.register(
    default_title="Filter List Dictionaries",
    description="Filter on a list of dictionaries",
    display_group="Utils",
    namespace="integrations.utils",
)

def filter_list_dict(
    listDic: Annotated[list, Field(..., description="List of dict")],
    key: Annotated[str, Field(..., description="Key to target")],
    value: Annotated[str, Field(..., description="Value to search")]
    ) -> Any:

    for item in listDic:
        if item.get(key) == value:
            return item

    return []
