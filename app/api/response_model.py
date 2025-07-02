from pydantic import BaseModel


class Organization(BaseModel):
    id: int
    names: str
    phones: str
    houses_id: int
    activities_id: int
