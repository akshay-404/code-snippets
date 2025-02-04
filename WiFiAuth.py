from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time, os

# Set the path to the chromedriver
path = "C:\Program Files\Google\Chrome\webdriver\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("http://connectivitycheck.gstatic.com/generate_204")
print(driver.title)

# import username and password
USER, PASS = os.environ.get("WIFI_CREDENTIALS").split("-")

try:
    # Find the search bar
    username = driver.find_element(By.NAME, "username")
    username.send_keys(USER)
    password = driver.find_element(By.NAME, "password")
    password.send_keys(PASS)
    password.send_keys(Keys.RETURN)

except Exception as e:
    print(e)

driver.quit()

