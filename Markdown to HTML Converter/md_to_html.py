# Import the markdown library, which provides a function to convert Markdown to HTML
import markdown

# Import the os library, which provides functions for interacting with the operating system
import os

# define the input and output file names
input_file = 'markdown.md'
output_file = 'output.html'

try:
    # open input file and read its content
    with open (input_file, 'r') as f:
        text = f.read()

    # Convert the markdown text to html
    html = markdown.markdown(text)

    # Open the output file and write the html contents
    with open (output_file, 'w') as f:
        f.write(html)

    print(f"Conversion of markdown file to Html file Successful! Output written to {output_file} ")

except FileNotFoundError:
    print(f"File {input_file} not found. Please check the file path and try again")
except Exception as e:
    print(f"An error occurred: {e}")
        
