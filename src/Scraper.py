"""
Class in order to allow for internet scraping on any topic specified
@author Ryan Nicholas
@version 2020.04.21
"""

# SOURCE FOR LATER: https://scrapy.org/
# Stack Overflow: https://stackoverflow.com/questions/15798878/how-to-search-internet-with-python
# Other helpful links: https://www.edureka.co/blog/web-scraping-with-python/

# SOURCE FOR ASSISTANT: https://www.geeksforgeeks.org/personal-voice-assistant-in-python/


from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os

class Scraper:
    def __init__(self):
        """
        Initialize the scraper
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()


    def search(self, topic):
        """
        Search for a topic and scrape the internet for data on the topic
        :param topic: topic to scrape
        :return: return the search response
        """

        answer = None

        try:
            if 'youtube' in topic.lower():
                index = topic.lower().split('youtube')
                query = topic.split()[index + 1:]
                answer = self.driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
            elif 'wikipedia' in topic.lower():
                index = topic.lower().split('wikipedia')
                query = topic.split()[index + 1:]
                answer = self.driver.get("https://en.wikipedia.org/wiki/" + "_".join(query))
            else:
                if 'google' in topic.lower():
                    index = topic.lower().split().index('google')
                    query = topic.split()[index + 1:]
                    self.driver.get("https://www.google.com/search?q=" + '+'.join(query))
                    results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
                    value = results[0].click() # clicks the first one
                    print('Value: ', value)
                    answer = value.title
                elif 'search' in topic.lower():
                    index = topic.lower().split().index('search')
                    query = topic.split()[index + 1:]
                    answer = self.driver.get("https://www.google.com/search?q=" + '+'.join(query))
                else:
                    answer = self.driver.get("https://www.google.com/search?q=" + '+'.join(topic.split()))
        except Exception as e:
            print("Could not find that on the internet")

        self.driver.close()

        return answer
