import random

known_weather_data = {'berlin': 20.0}

def get_weather(city: str) -> float:
    """Retrieves the temperature for a specified city."""
    city = city.strip().lower()
    return known_weather_data.get(city, round(random.uniform(-5, 35), 1)

def set_weather(city: str, temp: float) -> str:
    """Sets the temperature for a specified city."""
    city = city.strip().lower()
    known_weather_data[city] = temp
    return 'OK'