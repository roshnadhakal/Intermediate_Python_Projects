# Random Quote Generator

This is a simple Python script that displays a random quote from a text file. The script reads quotes from a specified file and prints a randomly selected quote to the console.

## Requirements

- Python 3.12.4 or higher
- A text file named `quotes.txt` containing quotes, with each quote on a new line.

## Installation

1. Ensure you have Python 3.12.4 installed on your machine. 
2. Clone this repository or download the script.

   ```bash
   git clone https://github.com/yourusername/random-quote-generator.git
   cd random-quote-generator
   ```

3. Create a `quotes.txt` file in the same directory as the script and populate it with your favorite quotes.

## Usage

To run the script, use the following command in your terminal:

```bash
python quote_generator.py
```

Make sure that `quotes.txt` is in the same directory as the script. The script will read the quotes from the file and display a random quote each time it is executed.

## How It Works

1. **Importing Modules**: The script imports the `random` module to facilitate the selection of a random quote.
2. **Reading Quotes**: The `read_quotes` function attempts to open the `quotes.txt` file and read its contents. Each line is stripped of whitespace and stored in a list.
3. **Error Handling**: If the file is not found, an error message is displayed, and an empty list is returned.
4. **Displaying a Random Quote**: The `display_random_quote` function selects a random quote from the list and prints it to the console.
5. **Execution**: When the script is run, it reads the quotes from the file and displays one randomly.

## Example Quotes

Here are some example quotes you can add to your `quotes.txt` file:

```
"The only limit to our realization of tomorrow is our doubts of today." 
"Life is what happens when you're busy making other plans." 
"The purpose of our lives is to be happy." 
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features!
