from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from twilio.rest import Client
from webdriver_manager.firefox import GeckoDriverManager
from datetime import datetime
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    RECIPIENT_PHONE_NUMBER,
    STEAM_DECK_URL
)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

browser_options = Options()
browser_options.add_argument("--headless")
url = STEAM_DECK_URL

def start():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=browser_options)
    driver.get(url)
    return driver


def refresh(driver):
    driver.refresh()
    # Wait for the page to load after refresh
    time.sleep(5)


def quit(driver):
    driver.quit()


def runner(driver):
    try:
        # Wait up to 10 seconds for the element to be present
        wait = WebDriverWait(driver, 10)
        stock_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'CartBtn')]/span"))
        )
        
        x = stock_element.text.strip()
        print("Found text:", x)
        
        if "Out of stock" not in x:
            # message = client.messages.create(
            #     to=RECIPIENT_PHONE_NUMBER,
            #     from_=TWILIO_PHONE_NUMBER,
            #     body=f"In Stock {STEAM_DECK_URL}")
            print("Message sent - Steam Deck is in stock!")
            status = 1
        else:
            print("Current status:", x)
            print("Time checked:", datetime.now())
            status = 0
        return status
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 0


def get_my_deck():
    c = 0
    driver = start()
    time.sleep(10) ## DO NOT EDIT
    print("Started Scraper")
    while True:
        try:
            if c < 11:
                status = runner(driver)
                if status == 1:
                    break
                time.sleep(20) ## HOW OFTEN TO CHECK THE WEBSITE
                c = c + 1
                refresh(driver)
            else:
                print("Rebooting")
                quit(driver)
                time.sleep(20) ## DO NOT EDIT
                c = 0
                driver = start()
        except Exception as e:
            print(f"Main loop error: {str(e)}")
            driver.quit()
            time.sleep(20) ## DO NOT EDIT
            get_my_deck()


get_my_deck()
