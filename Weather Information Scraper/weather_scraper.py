from selenium import webdriver                                      #allows interaction with web browser
from selenium.webdriver.common.by import By                         #to locate elements on webpage(by XPath,class name etc..)
from selenium.webdriver.support.ui import WebDriverWait             #to ait until the element is available on the webpage
from selenium.webdriver.support import expected_conditions as EC    #defines conditions to wait for (e.g., presence of an element).
from selenium.webdriver.chrome.service import Service               #to manage the execution of the ChromeDriver executable.
import time

# Get the city name from the user
city = input("Enter the name of the city: ")

# Provide the path to the ChromeDriver executable file
chrome_driver_path = r'F:\Work\PYTHON\chromedriver-win64\chromedriver.exe'

# Create a Service object for managing the ChromeDriver process with the specified path
service = Service(chrome_driver_path)

# Create a new instance of the Chrome WebDriver to launch chrome browser
driver = webdriver.Chrome(service=service)

# Construct the URL with the user-provided city
url = f"https://www.google.com/search?q=weather+of+{city}"

# Open the URL
driver.get(url)

# Wait for the elements to load
wait = WebDriverWait(driver, 10)

# Waits until the temperature element is found on the page using its XPath
temperature = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='wob_t q8U8x']")))
print(f"Temperature in {city}: {temperature.text}")

# Find the precipitation element
precipitation = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='wob_pp']")))
print(f"Precipitation in {city}: {precipitation.text}")

# Find the humidity element
humidity = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='wob_hm']")))
print(f"Humidity in {city}: {humidity.text}")

# Find the wind element
wind = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='wob_ws']")))
print(f"Wind in {city}: {wind.text}")


time.sleep(2) # Pauses the script for 2 seconds before closing the browser.
driver.quit() # Closes the browser and ends the WebDriver session.
