
currencies = {
  "USD": 0.73,
  "EUR": 0.85,
  "JPY": 0.0064,
  "CAD": 0.59,
  "CHF": 0.79,
  "RON": 0.17,
  "AUD": 0.54
}


type_currency = input("What currency do you want to convert to pounds? (USD/EUR/JPY):  ")
amount = int(input("Enter the amount: "))
print(f"Amount in pounds: {int(amount) * currencies[type_currency]}")
