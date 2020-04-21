"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: File that allows Randor Assistance to respond to speech requests
"""

# NOTE: CAN USE gTTS in the future for Python Speach -> Should convert over eventually to become free
# Link to documentation: https://pypi.org/project/gTTS/
# Link to video: https://youtu.be/_Q8wtPCyMdo


from google.cloud import texttospeech
from playsound import playsound
import os
from google.oauth2 import service_account


class Speak:
    def __init__(self):
        """
        Initialize Speak Class that allows for text-to-speech functionality
        """
        file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS',
                         "C:\\Users\\Ryan's Computer\\PycharmProjects\\RandorAssistant\\Randor "
                         "Assistant-413444f14dd2.json")
        credentials = service_account.Credentials.from_service_account_file(file)

        self.client = texttospeech.TextToSpeechClient(credentials=credentials)
        self.voice = texttospeech.types.cloud_tts_pb2.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE  # Can be MALE, FEMALE, or NEUTRAL
        )

        self.audio_config = texttospeech.types.cloud_tts_pb2.AudioConfig(audio_encoding=
                                                                         texttospeech.enums.AudioEncoding.MP3)

    def respond(self, msg):
        """
        Respond with a certain message
        :param msg: message to respond with
        :return: None
        """
        synthesis_input = texttospeech.types.cloud_tts_pb2.SynthesisInput(text=msg)
        response = self.client.synthesize_speech(synthesis_input, self.voice, self.audio_config)

        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to output.mp3')
        playsound('output.mp3')

    def search(self, msg):
        """
        Search the web for a certain request
        :param msg: request to search the internet
        :return: None
        """
