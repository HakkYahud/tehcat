from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
import re


@registry.register(
    default_title="Remove HTML",
    description="Remove HTML bracket",
    display_group="Utils",
    namespace="integrations.utils",
)

def removeHTML(
    content: Annotated[Any, Field(..., description="HTML content to clean")],
    chartoremove: Annotated[str, Field(..., description="Character to replace")],
    replacementchar: Annotated[str, Field(..., description="New character")]
    ) -> str:

    content = str(content)
    content = re.sub("<p>", "\n", content)
    return content
