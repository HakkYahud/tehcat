from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry

@registry.register(
    default_title="Print a message",
    description="Display the message",
    display_group="Utils",
    namespace="integrations.utils",
)

def printMessage(
    mymessage: Annotated[str, Field(..., description="message to display")],
    ) -> str:

    return mymessage
