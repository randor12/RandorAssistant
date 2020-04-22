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
