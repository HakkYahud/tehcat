from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
import re


@registry.register(
    default_title="Clean HTML",
    description="Replace some HTML bracket of a message",
    display_group="Utils",
    namespace="integrations.utils",
)

def cleanHTML3(
    message: Annotated[Any, Field(..., description="Message to clean")]
    ) -> str:

    message = str(message)
    message = re.sub(r"a", "", message)
    return message
