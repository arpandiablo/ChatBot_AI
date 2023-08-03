import math
from chat_parameters.interaction import chat_conversation as chat

def mapping(data):

    if "day" in data:
        chat.day()
    
    elif "date" in data:
        chat.day()

    elif "time" in data:
        chat.time()

    elif "news" in data:
        chat.news()

    elif "temperature" in data:
        print(f"The current temperature is {math.ceil(chat.get_temperature())} degree celcius.")

    elif "weather" in data:
        print(f"The current weather is {chat.get_weather()}.")

    elif "exit" in data:
        chat.Exit()