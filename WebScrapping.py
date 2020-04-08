import webbrowser
from unicodedata import category

import pyautogui



from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import re
import matplotlib.pyplot as plt

import requests

#page = requests.get('https://www.wired.com/category/culture/')

#print(page)

# Create a BeautifulSoup object
#soup = BeautifulSoup(page.text, 'html.parser')





import time
import feedparser
import webbrowser
import random
feed = feedparser.parse("https://www.wired.com/feed/rss")

# feed_title = feed['feed']['title']  # NOT VALID
feed_entries = feed.entries

flag = 1

for entry in feed.entries:
    if(flag == 5):
        article_title = entry.title
        article_link = entry.link
        article_published_at = entry.published # Unicode string
        article_published_at_parsed = entry.published_parsed # Time object
        # article_author = entry.author  DOES NOT EXIST
        content = entry.summary
        #article_tags = entry.tags # DOES NOT EXIST


        print ("{}[{}]".format(article_title, article_link))
        print (" - Published at:  {}".format(article_published_at))
        # print ("Published by {}".format(article_author))
        print(" - Content:  {}".format(content))
        # print("catagory{}".format(article_tags))

        #print("TESTE.....")

        chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromedir).open(article_link)
        t = pyautogui.size()
        pyautogui.moveTo(100, 100, duration=0.1)


        teste = False
        while (teste == False):

            teste = iconX, iconY = pyautogui.locateCenterOnScreen('icon.png')
            pyautogui.moveTo(iconX, iconY, duration=0.25)
            pyautogui.click()
            pyautogui.moveTo(iconX-10, iconY+25, duration=0.25)
            #time.sleep(5000)
            pyautogui.click()

    flag +=1
    print("END THIS ONE")


print("SAIDAAAAA:::::")