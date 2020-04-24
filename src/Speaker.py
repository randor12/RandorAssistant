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

    def scrape(self, req):
        """
        Search for a topic and scrape the internet for the information
        :param req: request to be searched
        :return:
        """

    def search(self, req):
        """
        Search the internet for an answer to a question and say the top response
        :param req: request to the internet
        :return: None
        """
