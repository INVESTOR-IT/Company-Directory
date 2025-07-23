from pydantic import BaseModel


class Organization(BaseModel):
    id: int
    name: str
    phones: list[str]
    houses_id: int
    activities_id: int
