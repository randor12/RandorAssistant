"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: The purpose of this file is to create something that can listen and
              convert speech to text
"""

import speech_recognition as sr


class AudioListener:
    def __init__(self):
        """
        Initialize Audio Listener
        """

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
        GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
        try:
            # attempt to recognize the speech
            text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            print("Google Cloud Speech thinks you said " + text)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))

        return text
