from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from twilio.rest import Client
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

account_sid = "from_twilio" ## SIGN UP FOR A FREE TWILIO ACCOUNT AND GET YOUR SID AND AUTH TOKEN 
auth_token  = "from_twilio" ## AS ABOVE
client = Client(account_sid, auth_token)

browser_options = Options()
browser_options.headless = True
url = "https://store.steampowered.com/sale/steamdeckrefurbished"

def start():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=browser_options)

    
    driver.get(url)
    return driver


def refresh(driver):
    driver.refresh()


def quit(driver):
    driver.quit()


def runner(driver):
    all_btn = driver.find_elements(By.XPATH, "//*[@id='SaleSection_33131']")
    x = all_btn[0].text
    x = x.split("00")[0]  ## HERE YOU CAN BREAKPOINT AND DETERMINE WHICH PART OF THE TEXT YOU ARE INTERESTED IN (E.G. STRIP FOR 64GB, 256GB ETC
    print(x)
    if "add" in x.lower():
        message = client.messages.create(
            to="+44777777777", ## THE NUMBER THE ALERT WILL GO TO
            from_="+44777777777", ## THE NUMBER PROVIDED BY TWILIO
            body="In Stock https://store.steampowered.com/sale/steamdeckrefurbished")
        status = 1
    else:
        print(x)
        print(datetime.now())
        status = 0
    return status


def get_my_deck():
    c= 0
    driver = start()
    time.sleep(10) ## DO NOT EDIT
    print("Started Scraper")
    while True:
        try:
            if c<11:
                status = runner(driver)
                if status == 1:
                    break
                time.sleep(20) ## HOW OFTEN TO CHECK THE WEBSITE
                c = c+1
                refresh(driver)
            else:
                print("Rebooting")
                quit(driver)
                time.sleep(20) ## DO NOT EDIT
                c = 0
                driver = start()
        except Exception as e:
            print(e)
            driver.quit()
            time.sleep(20) ## DO NOT EDIT
            get_my_deck()


get_my_deck()
