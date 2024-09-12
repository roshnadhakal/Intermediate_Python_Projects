import requests
from bs4 import BeautifulSoup

# adjust the URL of news website as needed

url = "https://edition.cnn.com/"

#send an HTTP request to the website
response = requests.get(url)

#Check if the request was succesful
if response.status_code == 200:
    # Parse the html content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
   
    #Find all the headlines elements on the page
    headLines = soup.find_all('h2', class_='container__title_url-text container_lead-plus-headlines-with-images__title_url-text') # passing the heade and class info of specific website 
    #Print the headlines
    for headline in headLines:
        print(headline.text.strip())
else:
    print("Failed to retrieve the webpage")


