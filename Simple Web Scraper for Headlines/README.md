# Web Scraper for CNN Headlines

This Python script scrapes the latest headlines from the CNN website using the Requests library to send an HTTP request and the BeautifulSoup library to parse the HTML content.

## Requirements

- Python 3.12.4 or higher
- Requests library
- BeautifulSoup library

## Installation

1. Install Python 3.12.4 or higher from the official website: https://www.python.org/downloads/
2. Open a terminal or command prompt and run the following commands to install the required libraries:

pip install requests  
pip install beautifulsoup4

## Code Explanation
1. **Imports**: The script imports the requests library to handle HTTP requests and BeautifulSoup from the bs4 library to parse HTML content.
2. **URL Setup**: The URL of the CNN website is defined, which can be adjusted to scrape other sites.
3. **HTTP Request**: The script sends a GET request to the specified URL using requests.get(). It checks the response status code to ensure the request was successful (HTTP 200).
4. **HTML Parsing**: If the request is successful, the HTML content is parsed using BeautifulSoup. The script searches for all '<h2>'elements with a specific class that contains the headlines.
5. **Output**: The script iterates through the found headlines and prints each one to the console. If the request fails, an error message is printed.
6. Run the script in the terminal:  
   python scraper.py
7. The script will output the latest headlines from the CNN website.

## Customization

- You can modify the \`url\` variable to scrape headlines from a different news website.
- Adjust the \`find_all()\` parameters (\`'h2'\`, \`class_\`) based on the HTML structure of the target website.

## Note

- Web scraping should be done ethically and in compliance with the website's terms of service.
- Excessive scraping may be considered abusive and could lead to IP blocking or other measures by the website.
