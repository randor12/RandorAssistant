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
        greetings = ['hello', 'hey', 'hi']
        leaving = ['bye', 'goodbye', 'adios', 'see you later']
        emotions = ['how are you', 'how are you doing']
        activity = ["what's up", 'what are you doing', 'what you doing', 'what is up', 'whats up']
        name = ["what's your name", 'what is your name', 'whats your name']
        time = ['what time is it', "what's the time", 'what is the time']
        if self.command is not None:
            if self.command == 'ping':
                self.ping()
            if any(x in self.command for x in greetings):
                self.speak.respond("hello ryan")
            elif any(x in self.command for x in leaving):
                self.speak.respond('see you later')
            if any(x in self.command for x in emotions):
                self.speak.respond('i am doing well')
            if any(x in self.command for x in activity):
                self.speak.respond('i am not doing much ryan')
            if any(x in self.command for x in name):
                self.speak.respond('my name is ran door')
            if any(x in self.command for x in time):
                self.speak.getTime()
        else:
            self.speak.respond('i am sorry i did not get that')



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
