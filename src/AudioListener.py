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
import time
from Speak import Speak as sp
from Speaker import Speaker as sp2
from commands import Commands as cmd
import random
import playsound
from sys import platform


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
        self.speaker = sp()
        if platform == 'linux' or platform == 'linux2':
            self.speaker = sp2()
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
        # attempt to recognize words being said, check for errors
        try:
            # convert speech to text
            self.text = recognizer.recognize_google(audio, language='en-US')
            print("Randor Assistant thinks you said: ", self.text)
        except sr.UnknownValueError:
            # if the audio could not be understood
            self.text = None
            print("Randor Assistant Could Not Understand You")
        except sr.RequestError as e:
            # if there is an internal error with Google or
            # no internet connection
            self.text = None
            print("Could not request results form Google services; {0}".format(e))

        if self.command:
            # respond to a command
            response = cmd(self.text)
            response.result()
            self.command = False

        commonNameSpells = ['randor', 'ran door', 'randeur']

        if self.text is not None and (any(x in self.text for x in commonNameSpells)) and not self.command:
            # Check if randor was called and it is not in command mode
            self.command = True
            speakResponse = random.choice(self.speakingStartResponses)
            self.speaker.respond(speakResponse)
            playsound.playsound('beep.mp3')

    def backgroundListener(self):
        """
        Start listening from the background and call a
        callback function in order to allow for the assistant to
        communicate
        :return: Return the text that is sent from the background noise
        """
        print("Starting up")
        stop_audio = self.r.listen_in_background(self.source, self.callback, phrase_time_limit=5)
        print("Go ahead and speak! Randor is listening! ")
        while self.text is None or 'exit' not in self.text:
            # Loop until told to stop looping
            time.sleep(0.1)  # time pause to not overload CPU

        print("Exiting...")
        byeCommand = cmd('bye')
        byeCommand.result()
        stop_audio(wait_for_stop=False)  # Stop the audio listener
        for i in range(50):  # give 5 seconds to stop background proccess
            time.sleep(0.1)


# ex = AudioListener()
#
# ex.backgroundListener()
