"""
:author: Ryan Nicholas
:date: April 16, 2020
:description: Create a chat bot in order to respond to the user
"""


class ChatBot:
    def __init__(self):
        """
        Initialize chat bot
        """

    def send_response(self, msg):
        """
        Send a response to a message
        :param msg: message sent from the user
        :return: return the response to the message
        """
        response = ""
        answer = self.use_model(msg)
        if answer is not None and len(answer) > 0:
            response = answer
        return response

    @staticmethod
    def use_model(msg):
        """
        Use ChatBot model in order to come up with a response and message
        :param msg: message sent
        :return: response to the message
        """
        r = msg
        return r
