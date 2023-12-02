
# Project Title

Voice Integrated Weather App

## Description

This is a weather app that informs user about the current weather condition using text and voice. It also recommends what type of clothes to wear and suggests what type of music to listen.
This application was developed using Python programming language.
Weather app is an essential application to have, specially during the winter times because it provides a real time weather data which helps users to plan their activites.
This application has a voice integration feature which reads the weather information to the users so that they don't have to read the information by themselves. 

## Architecture Diagram
![arc drawio](https://github.com/UOITEngineering/programmingproject-AnirbanBarua/assets/148647000/49896d56-733a-47d0-b1e2-b26da5a7a806)

* User Input: Accepts input from the user (city name and units).
* Input Processing: Processes user input and initiates the weather retrieval process.
* Coordinates Processing: Uses Geocoding to obtain latitude and longitude based on the city name.
* Weather API Request: Sends a request to the OpenWeatherMap API to retrieve weather data.
* Weather Data Processing: Processes the weather data, including temperature conversion and music recommendation.
* Text-to-Speech & Music Recommendation: Generates text-to-speech for weather information and recommends music based on the weather.

## Executing the Application
### Dependencies

* Windows (Any version)
* WSL (Windows Subsystem for linux)
* Ubuntu 20.04.6 LTS

### Installing Libraries
Install the following libraries using ubuntu terminal:

* Installing “gtts”:
```
sudo apt install python3-gtts
```
* Installing “playsound”:
```
pip3 install playsound==1.2.2
```
* Installing “geopy”:
```
sudo apt install python3-geopy
```
* Installing “mpv”:
```
sudo apt install mpv
```
* Installing “Gstreamer”:
```
sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```
### Download Files
Download all the files and put them in a one folder.

### Run
Go to the directory where the files are saved using the ubuntu terminal.
Run the main.py file using the following command:
```
python3 main.py
```
After running it will show the following output. Just type in the city name and unit.
![input](https://github.com/UOITEngineering/programmingproject-AnirbanBarua/assets/148647000/2d22eb0b-e204-41f3-a2f0-0b3d511e8c54)
### Output
Text output will look like this.
![output](https://github.com/UOITEngineering/programmingproject-AnirbanBarua/assets/148647000/96ce32d9-bb5d-4002-8006-e28508e8e8e8)
## Challenges
After executing the application, the voice part sometimes may not work. Solution is to install the Gstreamer library again.
## Future Enhancements
* Adding 5 days weather forcast feature
* Design a GUI using tkinter library.
## Author
Anirban Barua (100920756)



