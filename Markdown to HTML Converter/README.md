# Markdown to HTML Converter

This project is a simple Python script that converts a Markdown file into an HTML file using the `markdown` library. 

## Requirements

To run this script, you need:

- **Python**: Version 3.12.4 or higher
- **file**: .md file to convert into .html file (for eg: markdown.md)
- **Libraries**: 
  - `markdown`: This library is used to convert Markdown text to HTML.
  
You can install the required library using pip:

```bash
pip install markdown
```

## Files

- `markdown.md`: This is the input Markdown file that you want to convert.
- `output.html`: This is the output HTML file that will be generated after conversion.

## Usage

1. Ensure you have Python 3.12.4 installed on your machine.
2. Install the required libraries using the command mentioned above.
3. Place your Markdown content in the `markdown.md` file.
4. Run the script using the following command in your terminal:

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the actual name of your Python script file.

## Code Explanation

The script performs the following steps:

1. **Import Libraries**: It imports the necessary libraries, `markdown` for conversion and `os` for file handling.
2. **Define File Names**: It sets the input and output file names.
3. **Read Markdown File**: It opens the input Markdown file and reads its content.
4. **Convert to HTML**: It uses the `markdown` library to convert the read content into HTML.
5. **Write to Output File**: It writes the converted HTML content to the specified output file.
6. **Error Handling**: The script includes error handling to manage file not found errors and other exceptions.

## Example

To see the conversion in action, create a `markdown.md` file with some Markdown content, and run the script. You will find the converted HTML in `output.html`.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add.
