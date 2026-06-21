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

def sleep(
    message: Annotated[str, Field(..., description="Message target to find the character to replace")],
    char: Annotated[str, Field(..., description="Character to replace")],
    newChar: Annotated[str, Field(..., description="New character")]
    ) -> str:
    
    return message
