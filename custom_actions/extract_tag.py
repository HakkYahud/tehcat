from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry

@registry.register(
    default_title="Extract Trigram",
    description="Extract Trigram from TAG",
    display_group="Utils",
    namespace="integrations.utils",
)

def extract_tag(
    tag: Annotated[str, Field(..., description="TAG of the affected system")],
    ) -> str:
    if len(tag) > 3:
        trigram = tag.split("_")[0]
        return trigram
    else: 
        return tag
