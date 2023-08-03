from datetime import *
import random
import chat_parameters.archives as c
import requests

now = datetime.now()


class chat_conversation:
    def greeting():
        hour = int(now.hour)
        if hour>=0 and hour<12:
            print("Good Morning!")

        elif hour>=12 and hour<18:
            print("Good Afternoon!")
        else:
            print("Good evening!")

        print(random.choice(c.greeting))

    def day():
        days = now.strftime("%A, %B %d")
        print(f"Today is {days}.")

    def time():
        times = now.strftime("%H:%M:%S")
        print(f"The time is {times}.")

    def news():
        print(random.choice(c.news))

    def get_temperature():
        url = "https://api.openweathermap.org/data/2.5/weather?q=Thankot,Nepal&appid=3023e789298a5e8384e0f5b94cfcc846"
        #This is my API_KEY (Arpan Gautam) get yours for free from "openweathermap.org" and don't overload my free quota
        response = requests.get(url)
        data_temp = response.json()
        temperature = data_temp["main"]["temp"]
        temperature_in_Celsius = temperature - 273.15
        return temperature_in_Celsius
    
    def get_weather():
        url = "https://api.openweathermap.org/data/2.5/weather?q=Thankot,Nepal&appid=3023e789298a5e8384e0f5b94cfcc846"
        #This is my API_KEY (Arpan Gautam) get yours for free from "openweathermap.org" and don't overload my free quota
        response_weather = requests.get(url)
        data_weather = response_weather.json()
        weather = data_weather["weather"][0]["main"]
        return weather

    def Exit():
        print(random.choice(c.close))
        exit()