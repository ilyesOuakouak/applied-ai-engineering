from app.schemas.tools import WeatherResult

def get_current_weather(city: str) -> WeatherResult:
    return WeatherResult(
        city=city,
        temperature=23,
        condition="raining",
        unit="celsius"
    )