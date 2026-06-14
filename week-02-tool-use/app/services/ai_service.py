import openai, json
from app.services.job_service import get_current_weather
from app.core.config import settings

defined_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather and temperature for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city we want the temperature for."
                    }
                },
                "required": ["city"]
            }
        }
    }
]

def run_agent(user_message: str):
    openai_client = openai.OpenAI(api_key=settings.openai_api_key)

    response = openai_client.chat.completions.create(
        model=settings.model_name,
        messages=[{"role": "user", "content": user_message}],
        tools=defined_tools
    )

    # get the first choice
    message = response.choices[0].message

    # Check if the model wants to call the defined tool
    if message.tool_calls:
        # Extract the tool call
        tool_call = message.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)
        city = arguments["city"]

        return get_current_weather(city)


    else:
        # We just return the text response
        return message.content
