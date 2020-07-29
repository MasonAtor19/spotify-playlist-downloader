# This is for https://ytmp3.cc/en/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

# TODO: use youtube-dl

fname = input("Enter downloaded file name (without txt entention): ")

with open(fname + ".txt", "r") as f:

    songs = f.readlines()

# Parse and clean up song names from file
songs = [x.strip('"-').replace(",", " ").replace("  ", " ") for x in songs]

for song in songs:

    # Open a webdriver
    try:
        browser = webdriver.Chrome()
        browser.get("http://www.google.com")
    except:
        print("Failed to open chromedriver")
        exit(-1)

    # Search google for the songname
    search = browser.find_element_by_name("q")
    search.send_keys("youtube " + song)
    result = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')

    # Select the first result
    result[0].click()

    if "www.youtube.com" in browser.current_url:
        try:
            # Copy URL from search result and check to make sure Youtube

            browser.get("https://ytmp3.cc/en/")
            # Navigate to Youtube to MP3 Converter

            search = browser.find_element_by_id("input")
            search.send_keys(URL)
            search = browser.find_element_by_id("submit")
            search.send_keys(Keys.RETURN)
            time.sleep(30)

            try:
                search = browser.find_element_by_xpath(
                    "/html/body/div[2]/div[1]/div[1]/div[3]/a[1]"
                ).click()
                time.sleep(10)
                print("Song " + song + " successfully downloading")
                browser.quit()
            except:
                print("Song " + song + " failed. Closing and moving on")
                browser.quit()
            # Find entry bar, enter URL, wait, download

        # except ElementNotInteractableException as exception:
        #    print ("Song " + temp + " failed due to unclickable element")
        #   browser.quit()
        except:
            browser.quit()
    # Close the browser and iterate to next entry

    # Just an extra line!
