# Homework Answers

## Q1
Parameter name: `city`

## Q2
```json
{
    "type": "function",
    "name": "set_weather",
    "description": "Sets the temperature for a specified city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "The city name"},
            "temp": {"type": "number", "description": "Temperature value"}
        },
        "required": ["city", "temp"]
    }
}