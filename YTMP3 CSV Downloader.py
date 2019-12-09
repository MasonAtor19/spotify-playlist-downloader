#This is for https://ytmp3.cc/en/
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


fname = input("Enter downloaded file name (without txt entention): ")
num_lines = 0
with open("C:/Users/Mason/Downloads/" + fname + ".txt", 'r') as f:
    for line in f:

            
        temp = line
        temp = temp.replace("\"","")
        temp = temp.replace(","," ")
        temp = temp.replace("-","")
        temp = temp.replace("  "," ")
        #Parsed input from txt document
        
        browser = webdriver.Chrome()
        browser.get('http://www.google.com')
        search = browser.find_element_by_name('q')
        search.send_keys("youtube " + temp)
        result = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')        
        result[0].click()
        #Opened first search result


        URL = browser.current_url
        URL = URL.replace("https://","")
        if(URL[:15] == "www.youtube.com"):#14
            try:
                #Copy URL from search result and check to make sure Youtube

                browser.get("https://ytmp3.cc/en/")
                #Navigate to Youtube to MP3 Converter

                
                search = browser.find_element_by_id('input')
                search.send_keys(URL)
                search = browser.find_element_by_id("submit")
                search.send_keys(Keys.RETURN)
                time.sleep(30)
                
                try:
                    search = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]").click()
                    time.sleep(10)
                    print ("Song " + temp + " successfully downloading")
                    browser.quit()
                except:
                    print("Song " + temp + " failed. Closing and moving on")
                    browser.quit()
                #Find entry bar, enter URL, wait, download

            #except ElementNotInteractableException as exception:
             #    print ("Song " + temp + " failed due to unclickable element")
              #   browser.quit()
            except:
                browser.quit()
        #Close the browser and iterate to next entry
        
        
    #Just an extra line!
