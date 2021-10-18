
currencies = {
  "USD": 0.73,
  "EUR": 0.85,
  "JPY": 0.0064
}


type_currency = input("What currency do you want to convert to pounds? (USD/EUR/JPY):  ")
amount = int(input("Enter the amount: "))
if type_currency == "USD":
   print(f"Amount in pounds: {int(amount) * currencies[type_currency]}")
elif type_currency == "EUR":
   print(f"Amount in pounds: {int(amount) * currencies[type_currency]}")
elif type_currency == "USD":
   print(f"Amount in pounds: {int(amount) * currencies[type_currency]}")
else:
   quit()
