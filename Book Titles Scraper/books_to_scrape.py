import requests
from bs4 import BeautifulSoup

# Counter to track pages scraped
page_count = 1  # Start from page 1

# Function to scrape a single page
def scrape_page(url):
    global page_count  # Declare that we're using the global page_count variable that is outside the function

    response = requests.get(url)
    response.raise_for_status()
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all book entries by targeting the 'li' with class 'ast-col-sm-12'
    books = soup.find_all('li', class_='ast-col-sm-12')

    # Loop through each book and extract title and author
    for book in books:
        # Find the title element
        title_element = book.find('h4', class_='woocommerce-loop-product__title')
        # Find the author element
        author_element = book.find('div', class_='pwb-brands-in-loop').find('a', href=True) if book.find('div', class_='pwb-brands-in-loop') else None
        
        # Extract and clean title and author
        if title_element:
            title = title_element.text.strip()
            author = author_element.text.strip() if author_element else 'Unknown Author'
            print(f"Title: {title}, Author: {author}")

    # Handle pagination and limit scraping to only 3 pages
    if page_count < 2:  # Change to "<" so it moves to page 3 after printing page 2
        pagination = soup.find('nav', class_='woocommerce-pagination')
        if pagination:
            # Find the next available page link
            next_page = pagination.find('a', class_='page-numbers', href=True)
            if next_page:
                next_page_url = next_page['href']
                page_count += 1  # Increment the page count
                print(f"Moving to page {page_count}: {next_page_url}")
                scrape_page(next_page_url)  # Recursive call to scrape the next page

# Starting URL
start_url = "https://shopratnaonline.com/product-category/books/"
scrape_page(start_url)
