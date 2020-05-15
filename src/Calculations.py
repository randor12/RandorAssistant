"""
:author: Ryan Nicholas
:date: May 6, 2020
:description: Allow for calculations from the smart assistant
"""

import wolframalpha
import os
from os import path
import json

class Calculations:
    def __init__(self):
        """
        Initialize the Calculations Class
        :return: None
        """
        self.client = None
        try:
            self.app_id = os.getenv("WOLFRAMALPHA_APP_ID")

            if (path.exists('config.json') and self.app_id is None):
                with open('config.json') as f:
                    data = json.load(f)
                    try:
                        self.app_id = data['WOLFRAMALPHA_APP_ID']
                    except Exception:
                        self.app_id = None

            self.client = wolframalpha.Client(self.app_id)
        except Exception as e:
            print("Sorry, that API Key did not work")

    def calc(self, req):
        """
        :param req: Request to be calculated
        :return: Return the answer to the calculation or return None if
        there was an exception
        """
        try:
            index = req.lower().split().index('calculate')
            query = req.split()[index + 1:]
            response = self.client.query(' '.join(query))
            answer = next(response.results).text
            print("The answer is ", answer)
            return answer
        except Exception as e:
            return None
