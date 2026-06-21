from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
import re


@registry.register(
    default_title="Find and Replace",
    description="Replace some character by another character",
    display_group="Utils",
    namespace="integrations.utils",
)

def find_and_replace(
    message: Annotated[Any, Field(..., description="Message target to find the character to replace")],
    char: Annotated[str, Field(..., description="Character to replace")],
    newChar: Annotated[str, Field(..., description="New character")]
    ) -> str:

    message = str(message)
    message = re.sub(char, newChar, message)
    return message
