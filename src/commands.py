"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: Make a file for commands sent to the Smart Assistant
"""
from Speak import Speak as app


class Commands:
    def __init__(self, cmd):
        """
        initialize Commands Class
        """
        self.command = cmd
        self.speak = app()

    def result(self):
        """
        Initialize command
        :return: Check to see if any of the commands fit
        """
        if self.command == 'ping':
            self.ping()

    def ping(self):
        """
        Make a ping-pong command to test if the voice assistant works correctly
        :return: Pong
        """
        msg = "Pong!"
        print(msg)
        self.speak.respond(msg)

    def search(self):
        """
        Search the internet for a request
        :return: None
        """
        self.speak.search(self.command)
