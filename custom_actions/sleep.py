from typing import Annotated, Any, Literal
from pydantic import Field
from tracecat_registry import registry
from time import sleep


@registry.register(
    default_title="Sleep",
    description="Pause the program for X seconds",
    display_group="Utils",
    namespace="integrations.utils",
)

def sleep(
    time: Annotated[float, Field(..., description="Time to pause the program")],
    ) -> float:
    wakeup = False
    while wakeup is False:
        sleep(time)
        wakeup = True
    
    return time
