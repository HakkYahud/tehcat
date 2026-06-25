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

def cleanHTML(
    message: Annotated[str, Field(..., description="Message to clean")],
    ) -> str:

    message = re.sub("\[\'", "", message)
    message = re.sub("\'\]", "", message)
    message = re.sub(r"<[^>]+>", "", message)
    message = re.sub(r"</[^>]+>", "", message)
    return message
