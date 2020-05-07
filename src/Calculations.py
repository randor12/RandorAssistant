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
        self.app_id = "WOLFRAMALPHA_APP_ID"
        self.client = wolframalpha.Client(self.app_id)
    
    def calc(self, req):
        """
        :param req: Request to be calculated 
        :return: None
        """
        index = req.lower().split().index('calculate')
        query = req.split()[index + 1:]
        response = client.query(' '.join(query))
        answer = next(response.results).text
        return answer


