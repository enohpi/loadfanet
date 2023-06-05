from pydantic import BaseModel


class NetdataApiRequestSerializer(BaseModel):
    chart: str = "services.mem_usage"
    dimension: str = "eltex-videoserver"
    after: int = -480
    points: int = 3
    options: str = "ms|flip|nonzero"
    format: str = "json"
    group: str = "average"
    gtime: int = 0

