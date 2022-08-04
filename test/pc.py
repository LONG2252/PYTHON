from selenium import webdriver
import time 
import re
from pyquery import PyQuery as pq

def openurl(url,num):
    browser = webdriver.Chrome()
    browser.get(url)
    html=browser.page_source
    data=str(pq(html))

    print(data)