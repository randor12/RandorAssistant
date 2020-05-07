"""
:author: Ryan Nicholas
:date: May 6, 2020
:description: Allow for calculations from the smart assistant
"""

import wolframalpha

class Calculations:
    def __init__(self):
        """
        Initialize the Calculations Class
        :return: None
        """
        self.client = None
        try:
            self.app_id = "WOLFRAMALPHA_APP_ID"
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
            return answer
        except Exception as e:
            return None