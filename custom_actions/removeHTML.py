from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
import re

@registry.register(
    default_title="Remove HTML",
    description="Remove HTML elements in the message",
    display_group="Utils",
    namespace="integrations.utils",
)

def remove_html(
    message: Annotated[Any, Field(..., description="message to clean html elements")],
    ) -> str:

    content = str(message)
    content = re.sub("\[\'", "", content)
    content = re.sub("\'\]", "", content)
    content = re.sub(r"<[^>]+>", "", content)
    content = re.sub(r"</[^>]+>", chr(10)+chr(10), content)

    return content
