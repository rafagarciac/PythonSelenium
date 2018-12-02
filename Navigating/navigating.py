#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = 'https://www.apple.com/'
TITLE = 'Apple'
PRODUCT_TO_SEARCH = "MacBook Pro" 

def assertions(title=None):
    assert TITLE in title

def send_keys_as_human(elem, search):
    for char in search:
        elem.send_keys(char)
        time.sleep(0.3)

def main():
    # Open WebDriver and specify the URL
    driver = webdriver.Firefox()
    driver.get(URL)

    # Get UI Elements by ID, Class, Type...
    try:
        # Click search Button.
        search_button = driver.find_element_by_id("ac-gn-link-search")
        search_button.click()
        time.sleep(2)


        # Put search string.
        search_input = driver.find_element_by_xpath("//input[@id='ac-gn-searchform-input']")
        send_keys_as_human(search_input, PRODUCT_TO_SEARCH)
        time.sleep(3)

        # Press Enter to Search
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)

        # Scroll Down 
        # driver.execute_script("window.scrollTo(0, 1200)")
        # time.sleep(3)

        # Get the main results from the search.
        cotainer_results = driver.find_element_by_id("exploreCurated")
        all_childrens = cotainer_results.find_elements_by_xpath("./*")
        all_childrens[0]
        time.sleep(4)

    except NoSuchElementException as e:
        print("NoSuchElementException Exception ! ")
    
    driver.close()

if __name__ == "__main__":
    main()    