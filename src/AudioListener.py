"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: The purpose of this file is to create something that can listen and
              convert speech to text
"""

import speech_recognition as sr
import os


class AudioListener:
    def __init__(self):
        """
        Initialize Audio Listener
        """
        self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = os.getcwd()
        index = self.GOOGLE_CLOUD_SPEECH_CREDENTIALS.index('src')
        self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = self.GOOGLE_CLOUD_SPEECH_CREDENTIALS[0:index]
        self.GOOGLE_CLOUD_SPEECH_CREDENTIALS = os.path.join(self.GOOGLE_CLOUD_SPEECH_CREDENTIALS,
                                                       'Randor Assistant-413444f14dd2.json')

    def startMicrophone(self):
        """
        Start the microphone in order to allow communication with the smart
        assistant
        :return: Return the text received from the speech, or None if there is no text
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech with speech-to-text API
        text = None
        # recognize speech using Google Cloud Speech
        try:
            # attempt to recognize the speech
            text = r.recognize_google_cloud(audio, credentials_json=self.GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print("Google Cloud Speech thinks you said " + text)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))

        return text
