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
            print("Google Cloud Speech thinks you said: ", text)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))

        return text

# ex = AudioListener()
#
# ex.startMicrophone()
