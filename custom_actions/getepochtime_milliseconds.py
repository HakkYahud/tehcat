from typing import Annotated, Any, Literal
from pydantic import Field
from datetime import datetime, timedelta
from tracecat_registry import registry


@registry.register(
    default_title="Get Epoch time in milliseconds",
    description="Convert date to a specific epoch time in milliseconds",
    display_group="Tehtris",
    namespace="integrations.tehtris",
)

def get_epoch_time(
    timetosub: Annotated[int, Field(...,description="amount of time to substract")], unit: Annotated[str, Field(...,description="unit to substract (hours / minutes)")]
    ) -> int:
    if unit == "hours":
        return int((datetime.now() - timedelta(hours=timetosub)).timestamp()*1000)
    elif unit == "minutes":
        return int((datetime.now() - timedelta(minutes=timetosub)).timestamp()*1000)
