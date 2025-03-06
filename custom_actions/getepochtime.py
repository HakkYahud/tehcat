from typing import Annotated, Any, Literal
from pydantic import Field
from datetime import datetime, timedelta
from tracecat_registry import registry


@registry.register(
    default_title="Get Epoch time",
    description="Convert date to a specific epoch time",
    display_group="Tehtris",
    namespace="integrations.tehtris",
)

def get_epoch_time(
    hourtosub: Annotated[int, Field(default=1)],
    ) -> int:
    return int((datetime.now() - timedelta(hours=hourtosub)).timestamp())

