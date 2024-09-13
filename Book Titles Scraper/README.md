# Book Scraper

A simple web scraper built with Python 3.12.4 that extracts book titles and authors from a specified online bookstore.

## Requirements

To run this project, ensure you have Python 3.12.4 installed on your machine. You will also need to install the required libraries. You can do this using pip:

pip install requests beautifulsoup4

## Usage

Run the script from your terminal:

python book_scraper.py

The script will start scraping book titles and authors from the specified online bookstore, displaying the results in the terminal.

**Example Output**
When you run the script, you should see output similar to the following in your terminal:
text
Title: The Great Gatsby, Author: F. Scott Fitzgerald
Title: To Kill a Mockingbird, Author: Harper Lee
Moving to page 2: https://shopratnaonline.com/product-category/books/page/2/
Title: 1984, Author: George Orwell
Title: Pride and Prejudice, Author: Jane Austen

## Code Explanation

1. **Imports**: 
   - The script imports the \`requests\` library for making HTTP requests and \`BeautifulSoup\` from \`bs4\` for parsing HTML content.

2. **Global Counter**: 
   - A global variable \`page_count\` is initialized to track the number of pages scraped. The scraping is limited to two pages.

3. **Function \`scrape_page(url)\`**:
   - This function takes a URL as an argument and performs the scraping.
   - It sends a GET request to the URL and checks for a successful response.
   - The HTML content of the page is parsed using BeautifulSoup.

4. **Finding Book Entries**:
   - The script searches for all book entries on the page by looking for \`<li>\` elements with the class \`ast-col-sm-12\`.
   - For each book entry, it extracts the title and author information.

5. **Pagination Handling**:
   - The script checks for pagination links to navigate to the next page.
   - If there is a next page and the page count is less than 2, it recursively calls \`scrape_page()\` with the next page URL.

6. **Starting Point**:
   - The scraping begins with a predefined starting URL that points to the book category page.
  
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
