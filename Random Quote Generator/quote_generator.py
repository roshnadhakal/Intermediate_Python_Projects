# import random module
import random

# Define file_path and name where quotes are stored
quote_file = "quotes.txt"

# Function to read quotes from file
def read_quotes(file_path):
    try:
        with open (file_path, "r") as f:
            #read the contents of a file and store each line as a separate element in a list.
            quotes = [Line.strip() for Line in f.readlines()]
            return quotes
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []
    
# Function to display a random quotes
def display_random_quote(quotes):
    # display random quotes from list
    random_quote = random.choice(quotes)
    print(random_quote)

# Read quotes from file
quotes = read_quotes(quote_file)

# Display random quote
print("\nQuote of the day: ")
display_random_quote(quotes)

