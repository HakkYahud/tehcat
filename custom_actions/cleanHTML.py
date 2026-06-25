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
    message: Annotated[Any, Field(..., description="Message to clean")],
    ) -> str:

    message = str(message)
    message = re.sub("\[\'", "", message)
    message = re.sub("\'\]", "", message)
    message = re.sub(r"<[^>]+>", "", message)
    message = re.sub(r"</[^>]+>", chr(10)+chr(10), message)
    return message
