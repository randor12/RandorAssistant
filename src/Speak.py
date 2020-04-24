"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: File that allows Randor Assistance to respond to speech requests
"""

# NOTE: CAN USE gTTS in the future for Python Speach -> Should convert over eventually to become free
# Link to documentation: https://pypi.org/project/gTTS/
# Link to video: https://youtu.be/_Q8wtPCyMdo


import pyttsx3
from datetime import datetime
import json
import os
from os import path
import requests
from sys import platform


def KToF(temp):
    """
    Converts temperature from Kelvin to Fahrenheit
    :param temp: temperature
    :return: Return the temperature in Fahrenheit
    """
    C = temp - 273
    F = (C * 9/5) + 32
    F = round(F, 0)
    return F


class Speak:
    def __init__(self):
        """
        Initialize Speak Class that allows for text-to-speech functionality
        """
        index = 1
        if platform == 'linux' or platform == 'linux2':
            self.engine = pyttsx3.init('espeak')
            self.engine.setProperty('rate', 140)
            index = 16
        else:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 160)  # set the rate of speaking
        self.engine.setProperty('volume', 1.0)  # set the volume (btwn 0-1)
        voices = self.engine.getProperty('voices')  # get voices

        # voices[0].id == MALE
        # voices[1].id == FEMALE
        if index != 16:
            self.engine.setProperty('voice', voices[index].id)  # set voice
        else:
            self.engine.setProperty('voice', voices[11].id)


    def respond(self, msg):
        """
        Respond with a certain message
        :param msg: message to respond with
        :return: None
        """
        if msg is not None:
            self.engine.startLoop(False)
            self.engine.say(msg)
            self.engine.iterate()
            self.engine.endLoop()
            self.engine.stop()


    def getTime(self):
        """
        Say the current time
        :return: None
        """
        time = datetime.now()
        currTime = time.strftime("%I:%M %p")
        sayTime = "It is " + currTime
        self.respond(sayTime)

    def search(self, msg):
        """
        Search the web for a certain request
        :param msg: request to search the internet
        :return: None
        """

    def getWeather(self):
        """
        Say the weather outside
        :return: None
        """
        WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        if path.exists('config.json') and WEATHER_API_KEY is None:
            with open('config.json') as f:
                data = json.load(f)
                try:
                    WEATHER_API_KEY = data['WEATHER_API_KEY']
                except Exception:
                    WEATHER_API_KEY = None
        if WEATHER_API_KEY is not None:
            # url -> base url + ?q={city, state, country code}&appid={API KEY}
            locations = ['blacksburg,virginia', 'monroe,connecticut']
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + locations[0] + "&appid=" + WEATHER_API_KEY
            response = requests.get(url)
            x = response.json()
            if x["cod"] != "404":
                # if there are no problems
                y = x['main']
                curr_temp = y['temp']
                fTemp = str(KToF(curr_temp))
                feels = y['feels_like']
                fFeels = str(KToF(feels))
                curr_pressure = str(y['pressure'])
                curr_humidity = str(y['humidity'])
                z = x['weather']
                description = z[0]['description']
                if 'sky' in description:
                    description = description.replace('sky', 'skies')

                msg = "It is " + fTemp + " degrees Fahrenheit in " + locations[0] + ". " \
                                         "It feels " + fFeels + ". the pressure is " \
                                                                "" + curr_pressure + " hPa. "
                msg += "The humidity is " + curr_humidity + " percent. The weather outside is " + description
                self.respond(msg)
            else:
                self.respond('Sorry, I can not look this up at the moment')
        else:
            self.respond('Sorry, I can not look this up at the moment')
