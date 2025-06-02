from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#Launching the browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#Open's Google
driver.get("https://www.google.com")
time.sleep(3)
print(driver.title)

#print the title of the page
#print(driver.title)

#Closing the browser after 3 seconds
driver.quit()

