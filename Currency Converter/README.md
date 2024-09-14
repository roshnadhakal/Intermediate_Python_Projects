# Currency Converter

A simple currency converter written in Python 3.12.4 that allows users to convert between various currencies using predefined exchange rates.

## Features

- Convert between multiple currencies including NPR, USD, EUR, GBP, INR, CNY, and JPY.
- User-friendly input prompts for amount and currency selection.
- Validates user input for currency selection.

## Requirements

- Python 3.12.4 or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/currency-converter.git
   cd currency-converter
   ```

## Usage

1. Run the script using Python:

   ```bash
   python currency_converter.py
   ```

2. Follow the prompts to enter the amount and select the currencies you wish to convert from and to.

## Example

```
Enter the amount to convert: 100
Enter the currency to convert from (NPR, USD, EUR, GBP, INR, JPY, CNY): USD
Enter the currency to convert to (NPR, USD, EUR, GBP, INR, JPY, CNY): EUR
100 USD is equal to 67.00 EUR
```

## Code Explanation

- **Exchange Rates Dictionary**: The exchange rates for various currencies are stored in a dictionary called `exchange_rates`.
- **Conversion Function**: The `convert_currency` function takes an amount and the currencies to convert from and to, retrieves the exchange rates, and calculates the converted amount.
- **User Input**: The script prompts the user for the amount and the currencies, checks for validity, and displays the converted amount.

## Contributing  
Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!
