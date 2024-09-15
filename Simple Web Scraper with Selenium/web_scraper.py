from selenium import webdriver  # Import the webdriver module
from selenium.webdriver.common.by import By  # Import the By class
from selenium.webdriver.support.ui import WebDriverWait  # Import the WebDriverWait class
from selenium.webdriver.support import expected_conditions as EC  # Import the expected_conditions module

# Initialize the Chrome driver
driver = webdriver.Chrome()  # Create a new Chrome browser instance

# Navigate to the website
driver.get('https://www.simplypsychology.org/parental-involvement-and-student-creativity.html')  # Load the webpage

# Define the element to wait for
element_to_wait = (By.ID, 'content')  # Specify the element by its ID

# Wait for the element to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_to_wait))  # Wait for the element to appear

# Extract the data
data = driver.find_element(By.ID, 'content').text  # Get the text content of the element

# Print the extracted data
print(data)  # Print the data

# Close the driver
driver.quit()  # Close the browser
