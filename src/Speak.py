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

class Speak:
    def __init__(self):
        """
        Initialize Speak Class that allows for text-to-speech functionality
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 160)  # set the rate of speaking
        self.engine.setProperty('volume', 1.0)  # set the volume (btwn 0-1)
        voices = self.engine.getProperty('voices')  # get voices
        # voices[0].id == MALE
        # voices[1].id == FEMALE
        self.engine.setProperty('voice', voices[1].id)  # set voice


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
