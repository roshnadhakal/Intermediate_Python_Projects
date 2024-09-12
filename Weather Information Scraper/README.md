# Weather Automation Script

This README provides instructions for running a Python script that retrieves weather information for a specified city using Selenium and ChromeDriver.

## Requirements

- **Python 3.12.4**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Selenium Library**: Install Selenium using pip:
 
  pip install selenium
 
- **ChromeDriver**: Download the ChromeDriver that matches your version of Chrome from [ChromeDriver downloads](https://chromedriver.chromium.org/downloads). Place the \`chromedriver.exe\` in a known directory (e.g., \`F:\\Work\\PYTHON\\chromedriver-win64\\\`).

## Script Overview

The script uses Selenium to automate the process of fetching weather data from Google for a user-specified city. It retrieves temperature, precipitation, humidity, and wind information.

### Code Explanation


from selenium import webdriver  # Allows interaction with web browser  
from selenium.webdriver.common.by import By  # To locate elements on webpage  
from selenium.webdriver.support.ui import WebDriverWait  # To wait until the element is available  
from selenium.webdriver.support import expected_conditions as EC  # Defines conditions to wait for  
from selenium.webdriver.chrome.service import Service  # To manage ChromeDriver execution  
import time  

1. **Imports**: The script imports necessary modules from the Selenium library to interact with the web browser and locate elements on the page.
2. **User Input**: It prompts the user to enter the name of the city for which they want to check the weather.
3. **ChromeDriver Setup**: The path to the ChromeDriver executable is specified, and a service object is created to manage it.
4. **WebDriver Initialization**: A new instance of the Chrome WebDriver is created to open the Chrome browser.
5. **URL Construction**: The script constructs a Google search URL for the weather of the specified city.
6. **Element Waiting**: It uses `WebDriverWait` to wait for specific elements (temperature, precipitation, humidity, wind) to load on the page.
7. **Data Retrieval**: The script retrieves and prints the weather data for the specified city.
8. **Cleanup**: Finally, it pauses for 2 seconds and then closes the browser.

## Running the Script

1. Open your terminal or command prompt.
2. Navigate to the directory containing your script.
3. Run the script using:
   
   python your_script_name.py
   
5. Enter the name of the city when prompted.

## Notes

- Ensure that the path to \`chromedriver.exe\` is correctly specified in the script.
- The script will open a Chrome browser window, fetch the weather data, and print it to the console.

## Troubleshooting

- If you encounter issues with ChromeDriver not being found, ensure that the path is correct and that Chrome is installed on your machine.
- Make sure the version of ChromeDriver matches your installed version of Chrome." >
