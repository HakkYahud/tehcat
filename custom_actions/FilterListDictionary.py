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
    message: Annotated[Any, Field(..., description="Message target to find the character to replace")],
    char: Annotated[str, Field(..., description="Character to replace")],
    newChar: Annotated[str, Field(..., description="New character")]
    ) -> str:

    message = str(message)
    return message
