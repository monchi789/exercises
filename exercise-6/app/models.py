from pydantic import BaseModel


class University(BaseModel):
    name: str
    country: str
    web_pages: list[str]


class Country(BaseModel):
    gdp_per_capita: float
    tertiary_enrollment_rate: float
    region: str
