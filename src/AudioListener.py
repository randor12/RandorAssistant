"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: The purpose of this file is to create something that can listen and
              convert speech to text
"""

# in case of need for PyAudio installation being needed for Windows,
# go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/
# Files will show python version and check for 32 bit or 64 bit version

import speech_recognition as sr
import os
import json
import asyncio
import time
from Speaker import Speaker as sp
from command import Commands as cmd
import random


class AudioListener:
    def __init__(self):
        """
        Initialize Audio Listener
        """
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/randor/PycharmProjects/RandorAssistant/Randor Assistant-413444f14dd2.json"
        # with open(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), 'r') as f:
        #     val = json.load(f)
        #     self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{}""".format(val)
        #     self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = self.GOOGLE_CLOUD_SPEECH_CREDENTIALS.replace("\'", "\"")
        # print("Google Auth JSON: ", self.GOOGLE_CLOUD_SPEECH_CREDENTIALS)  # display location of GOOGLE AUTH JSON
        self.r = sr.Recognizer()
        self.source = sr.Microphone()
        self.text = ""
        self.command = False
        self.speakingStartResponses = ['go ahead ryan', 'i am listening',
                                    'what is it ryan', 'how can i help ryan']

    def startMicrophone(self):
        """
        Start the microphone in order to allow communication with the smart
        assistant
        :return: Return the text received from the speech, or None if there is no text
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something!")
            audio = r.listen(source, phrase_time_limit=5)

        # recognize speech with speech-to-text API
        text = None
        # recognize speech using Google Cloud Speech
        try:
            # attempt to recognize the speech
            text = r.recognize_google(audio, language='en-US')
            print("Randor Assistant thinks you said: ", text)
        except sr.UnknownValueError:
            print("Randor Assistant could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google services; {0}".format(e))

        return text

    def callback(self, recognizer, audio):
        """
        Callback funtion to recognize noise in the background
        :return: None
        """
        previousText = self.text
        try:
            self.text = recognizer.recognize_google(audio, language='en-US')
            print("Randor Assistant thinks you said: ", self.text)
        except sr.UnknownValueError:
            self.text = previousText
            print("Randor Assistant Could Not Understand You")
        except sr.RequestError as e:
            self.text = previousText
            print("Could not request results form Google services; {0}".format(e))

        if self.text not None and 'randor' in self.text and not self.command:
            self.command = True
            speaking = sp()
            speakResponse = random.choice(self.speakingStartResponses)
            speaking.respond(speakResponse)

        if self.command:
            response = cmd(self.text)
            self.command = False



    async def backgroundListener(self):
        """
        Start listening from the background and call a
        callback function in order to allow for the assistant to
        communicate
        :return: Return the text that is sent from the background noise
        """
        stop_audio = self.r.listen_in_background(self.source, self.callback)
        previousText = ""
        sameAsBefore = True
        while 'exit' not in self.text:
            if previousText == self.text:
                sameAsBefore = True
            else:
                sameAsBefore = False
                previousText = self.text
            await asyncio.sleep(1)
            if self.text not None and not sameAsBefore:
                yield self.text
            time.sleep(0.1)

        stop_audio(wait_for_stop=False)
        for i in range(50):
            time.sleep(0.1)

# ex = AudioListener()
#
# ex.startMicrophone()
