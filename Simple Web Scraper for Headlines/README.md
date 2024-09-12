# Web Scraper for CNN Headlines

This Python script scrapes the latest headlines from the CNN website using the Requests library to send an HTTP request and the BeautifulSoup library to parse the HTML content.

## Prerequisites

- Python 3.12.4 or higher
- Requests library
- BeautifulSoup library

## Installation

1. Install Python 3.12.4 or higher from the official website: https://www.python.org/downloads/
2. Open a terminal or command prompt and run the following commands to install the required libraries:

\`\`\`bash
pip install requests  
pip install beautifulsoup4
\`\`\`

## Usage

1. Save the following code in a file named \`scraper.py\`:

\`\`\`python
import requests  
from bs4 import BeautifulSoup

# Adjust the URL of the news website as needed
url = \"https://edition.cnn.com/\"

# Send an HTTP request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
   
    # Find all the headlines elements on the page
    headLines = soup.find_all('h2', class_='container__title_url-text container_lead-plus-headlines-with-images__title_url-text')
    
    # Print the headlines
    for headline in headLines:
        print(headline.text.strip())
else:
    print(\"Failed to retrieve the webpage\")
\`\`\`

2. Run the script in the terminal:

\`\`\`bash
python scraper.py
\`\`\`

3. The script will output the latest headlines from the CNN website.

## Customization

- You can modify the \`url\` variable to scrape headlines from a different news website.
- Adjust the \`find_all()\` parameters (\`'h2'\`, \`class_\`) based on the HTML structure of the target website.

## Note

- Web scraping should be done ethically and in compliance with the website's terms of service.
- Excessive scraping may be considered abusive and could lead to IP blocking or other measures by the website.
