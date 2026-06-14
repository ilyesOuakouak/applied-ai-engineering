from pydantic import BaseModel, Field


class WeatherRequest(BaseModel):
    city: str = Field(description="The city name. where we want to know the temperature")

class WeatherResult(BaseModel):
    city: str = Field(description="The city name. where we want to know the temperature")
    temperature: int = Field(description="The temperature result")
    condition: str = Field(description="The weather condition")
    unit: str = Field(default="celsius", description="The unit used to measure the temperature")

