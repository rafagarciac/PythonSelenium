#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Selenium Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Utils Import 
import time
import json

URL = 'https://www.apple.com/'

TITLE = 'Apple'
PRODUCT_TO_SEARCH = 'AirPods' # MacBook Pro  # iPhone # AirPods

def assertions(title=None):
    assert TITLE in title

def send_keys_as_human(elem, search):
    for char in search:
        print(char + '\n')
        elem.send_keys(char)
        time.sleep(0.3)

def get_cookies(driver):
    # Get Cookies from the URL
    print('\n\t\t\t\t\t\t---------- COOKIES ----------\n')
    for cookie in driver.get_cookies():
        print(cookie)

def scroll_down_as_human(driver, scroll_y):
    for n in range(scroll_y):
        print('SCROLL Y:' + str(n))
        driver.execute_script("window.scrollTo(0, " + str(n) + ")")
        time.sleep(1 / 1000000)


def main():
    print("Getting the URL...")
    # Open WebDriver and specify the URL
    driver = webdriver.Firefox()
    driver.get(URL)
    print("URL Obtained!")
    print("-----------------\n")
    
    # Call get cookies
    print("Getting Cookies...")
    get_cookies(driver)
    print("Cookies Obtained!")
    print("-----------------\n")

    # Get UI Elements by ID, Class, Type...
    try:
        print("Click Close Language Support...")
        # Close Countr Warning!
        button_warning = driver.find_element_by_id("ac-ls-close")
        button_warning.click()
        print("Clicked!")
        print("-----------------\n")
        

        print("Click Search Button...")
        # Click search Button.
        search_button = driver.find_element_by_id("ac-gn-link-search")
        search_button.click()
        print("Clicked!")
        print("-----------------\n")
        time.sleep(2)

        print("Click Search Toolbar...")
        # Put search string.
        search_input = driver.find_element_by_xpath("//input[@id='ac-gn-searchform-input']")
        
        print("Send Keys: %s" % PRODUCT_TO_SEARCH)
        send_keys_as_human(search_input, PRODUCT_TO_SEARCH)
        print("Clicked!")
        print("-----------------\n")
        time.sleep(3)

        print("Click Search Button...")
        # Press Enter to Search
        search_input.send_keys(Keys.ENTER)
        print("Clicked!")
        print("-----------------\n")
        time.sleep(2)

        print("Getting Container Results...")
        # Get the main results from the search.
        cotainer_results = driver.find_element_by_id("exploreCurated")
        all_childrens = cotainer_results.find_elements_by_xpath("./*")
        print("Obtained!")
        time.sleep(2)
        
        print("Click in the first result (title - h2)...")
        # We always get the first result
        title = all_childrens[0].find_elements_by_xpath(".//h2")[0]
        title.click()
        print("Clicked!")
        print("-----------------\n")
        time.sleep(2)
        
        print("Scrolling...")
        scroll_down_as_human(driver, 4500)
        print("Stop Scrolling")
        print("-----------------\n")

        print("Click in the 'Buy' button....")
        # Click to Buy
        buy_button = driver.find_elements_by_xpath('//a[contains(text(), "{0}") and @class="ac-ln-button"]'.format('Buy'))[0]
        buy_button.click()
        print("Clicked!")
        print("-----------------\n")
        time.sleep(2)

        print("Getting gallery Items...")
        # Gallery Functionality
        gallery = driver.find_element_by_xpath("//ul[@class='thumbnails clearfix']").find_elements_by_xpath("./li[@role='presentation']")
        gallery.pop(0)
        print("Obtained!")
        for i, gallery_item in enumerate(gallery):
            gallery_item.click()
            print("Clicked in Gallery Item - %d" % i)
            time.sleep(1)
        print("-----------------\n")
        
        print("Click in the 'Add To Bag' button....")
        # Add To Bag
        add_to_bag_button = driver.find_element_by_xpath("//button[@title='Add to Bag']")
        add_to_bag_button.click()
        print("Clicked!")
        print("-----------------\n")
        time.sleep(2)
        
        # Scroll to see price
        print("Scrolling...")
        scroll_down_as_human(driver, 3000)
        print("Stop Scrolling")
        print(" Test Passed!")
        # print(" F I N I S H !")

    except NoSuchElementException as e:
        print("NoSuchElementException Exception ! ")
    
    driver.close()

if __name__ == "__main__":
    main()    