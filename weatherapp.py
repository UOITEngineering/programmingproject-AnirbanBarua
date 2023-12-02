# Copyright 2023
# Author: Anirban Barua
# Project: Voice Integrated Weather App
import requests
from geopy.geocoders import Nominatim
import json
from gtts import gTTS
from playsound import playsound
import os

# This function uses the Nominatim geocoder to obtain the latitude and longitude coordinates for a given city.
def get_coordinates(city):
    geolocator = Nominatim(user_agent="weatherapp")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None
# A utility function to convert temperature from Celsius to Fahrenheit.
def C_to_F(temp):
    return (temp*1.8)+32

# This function retrieves weather information for a given city using the OpenWeatherMap API. 
# It includes temperature conversion, clothing and umbrella recommendations, and constructs a weather report.   
def get_weather(city, api_key, units="metric"):
    lat, lon = get_coordinates(city)
    
    if lat is None or lon is None:
        return "Location not found. Please check the city name."
    
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        if units == "metric":
            temperature = data["main"]["temp"]-273.15
            unit = "C"
            clothing_recommendation = "Wear heavy clothing." if temperature < 10 else "Light clothing is sufficient."
            Feels_like = data["main"]["feels_like"]-273.15
        else:
            temperature = C_to_F(data["main"]["temp"]-273.15)
            unit = "F"
            clothing_recommendation = "Wear heavy clothing." if temperature < 50 else "Light clothing is sufficient."
            Feels_like = C_to_F(data["main"]["feels_like"]-273.15)
        humidity= data["main"]["humidity"]
        W=data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        Wind = data["wind"]["speed"]
        windbreaker="I also recommend wearing wind-breaker jacket." if Wind > 5 else ""
        umbrella_recommendation = "You may need an umbrella." if "rain" in description else "No need for an umbrella."
        weather_report = (f"Weather in {city}: {round(temperature)}°{unit.upper()}, "
                          f"Feels Like {round(Feels_like)}°{unit.upper()}, {description.capitalize()}.\n"
                          f"Humidity is {round(humidity)}%.\n"
                          f"Windspeed is {round(Wind)} m/s.\n"
                          f"{umbrella_recommendation}\n{clothing_recommendation}\n{windbreaker}")
           

        
        return weather_report
# This function recommends music based on the weather conditions.
def recommend_music(weather):
    if "rain" in weather:
        music="storm-clouds"
    elif "Clear" in weather:
        music = "SpaceShip-Theme"
    elif "snow" in weather:
        music = "a-new-beginning"
    elif "clouds" in weather:
        music = "uncertainty"
    else :
        music = "midnight-room"
    return music  
# This function converts text to speech and plays the generated audio.
def speak_text(text):
    # Initialize gTTS with the text
    tts = gTTS(text=text, lang='en')

    # Save the text as an audio file
    tts.save("audio.mp3")

    # Play the audio
    #os.system("audio_output.mp3")
    playsound('audio.mp3')
    os.remove('audio.mp3')
