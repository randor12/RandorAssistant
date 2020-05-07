"""
Speaker Class in order to allow for Text-To-Speech without reliance on Google-Cloud
:author: Ryan Nicholas
:date: April 21, 2020
"""

from gtts import gTTS
from playsound import playsound
import os
import time
from datetime import datetime
from os import path
import json
import requests

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

class Speaker:
    def __init__(self):
        """
        Initialize Speaker
        """

    def respond(self, msg):
        """
        Respond with message
        :param msg: Message to be said
        :return: None
        """
        startTime = time.time()
        tts = gTTS(msg, lang='en')  # Create audio file with String
        tts.save('output.mp3')   # save output audio
        saveTime = time.time()
        print("Save Time: ", saveTime - startTime)
        playsound('output.mp3')  # play output audio
        endTime = time.time()
        print("Finished Speaking: ", endTime - startTime)
        os.remove('output.mp3')

    def getTime(self):
        """
        Say the current time
        :return: None
        """
        time = datetime.now()
        currTime = time.strftime("%I:%M %p")
        sayTime = "It is " + currTime
        self.respond(sayTime)

    def getWeather(self):
        """
        Say the weather outside
        :return: None
        """
        WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        try:
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
        except Exception as e:
            self.respond('Sorry, I can not look this up at the moment')
            print("Exception: ", str(e))

    def scrape(self, req):
        """
        Search for a topic and scrape the internet for the information
        :param req: request to be searched
        :return:
        """

    def search(self, msg):
        """
        Search the web for a certain request
        :param msg: request to search the internet
        :return: None
        """
        web = Scraper()
        res = web.search(msg)
        if res is not None:
            self.respond("Sorry, I could not find an answer to that")
        else:
            self.respond("I found this on the web. " + str(res))
