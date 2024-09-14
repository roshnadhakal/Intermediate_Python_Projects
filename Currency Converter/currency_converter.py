# Defining dictionary to store the exchange rate
exchange_rates = {
    "NPR" : 1.0, # Nepalese Rupee
    "USD" : 0.0074, # US Dollar
    "EUR" : 0.0067, # Euro
    "GBP" : 0.0057, # British Pound
    "INR" : 0.62, #Indian Rupee
    "CNY" : 0.053, # Chinese Yuan
    "JPY" : 1.05 # Japanese Yen
}

#Function to convert currency
# Converts the given amount from one currency to another.
def convert_currency(amount, from_currency, to_currency):
    #Get the exchange rates
    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]

    # Calculate the converted amount
    converted_amount = amount *(to_rate / from_rate)
    return converted_amount
# Get user input for the amount and the currencies
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (NPR, USD, EUR, GBP, INR, JPY, CNY): ").upper()
to_currency = input("Enter the currency to convert to (NPR, USD, EUR, GBP, INR, JPY, CNY):").upper()

# Check if the currency are valid
if from_currency not in exchange_rates or to_currency not in exchange_rates:
    print("Invalid currency. Please try again.")
else:
    # Convert the currency and print the result
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}") #.2f is the format specifier, for "fixed-point notation with two decimal places".
