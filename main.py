# Copyright 2023
# Author: Anirban Barua
# Project: Voice Integrated Weather App
import os
import time
from weatherapp import get_weather, recommend_music, speak_text
import subprocess

api_key = 'de901437bd009d91f922818bb7c77285'
# A while loop to continuously prompt the user for input (city and units) until the user types 'exit'.
while True:
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        break

    units = input("Select units (metric/imperial): ")

    try:
        weather = get_weather(city, api_key, units) # Calls the get_weather function to obtain weather information 
        playlist_recommendation = recommend_music(weather) # Calls the recommend_music function for music recommendations based on the weather.

        print(weather)

        speak_text(weather)
        speak_text(f"Based on the weather, I recommend the '{playlist_recommendation}' music.\n"
                   f"Would you like me to play it for you?")
        play = input("Y/n ?")
        # If the user chooses to play the music, it uses the subprocess module to execute the mpv command, 
        # a media player, to play the recommended music.
        if play == "Y":
            M = f"mpv {playlist_recommendation}.mp3"
            #os.system(M)
            subprocess.run(M, shell=True)
            time.sleep(3)
        speak_text("Thank you for using our weather app. \n Have a great day")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
