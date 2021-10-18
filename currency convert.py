#declaring values dict
currencies = {
  "USD": 0.73,
  "EUR": 0.85,
  "JPY": 0.0064,
  "CAD": 0.59,
  "CHF": 0.79,
  "RON": 0.17,
  "AUD": 0.54
}

#inputting type and amount
type_currency = input("What currency do you want to convert to pounds? (USD/EUR/JPY):  ")
amount = int(input("Enter the amount: "))
#declaring the convert function
def convert():
   return int(amount) * currencies[type_currency]

print(f"Amount in pounds: {convert()}")
