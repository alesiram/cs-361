from forex_python.converter import CurrencyRates


print("**********************************************\n")
print('   Welcome to Your Currency Converter \n ')
print("**********************************************")


program_start = input('\nTo begin, enter "start" or press "1": ')
print('To exit enter "0"')
codes = ' IDR | BGN | ILS \n GBP | DKK | CAD \n JPY | HUF | RON   \n MYR | SEK | SGD \n HKD | AUD | CHF \n KRW | CNY | TRY \n HRK | NZD | THB \n EUR | NOK | RUB \n INR | MXN |CZK \n BRL | PLN | PHP \n ZAR'

print(f"\nCountries available for currency excahnge:\n------------------\n{codes} \n------------------")

def intro():
    if program_start == "start" or "Start" or "1":
        amount = float(input("Please enter the amount you want to convert: $ "))
        curr_currency = input("Please enter home currency code that has to be converted: ").upper()
        new_currency = input("Please enter the currency code you wish to convert to: ").upper()

        print('Thanks, please hold...')
        convertor(curr_currency, new_currency, amount)

def convertor(curr_currency, new_currency , amount):
    cr = CurrencyRates()
    print("You are converting", amount, curr_currency, "to", new_currency,".")
    output = cr.convert(curr_currency, new_currency, amount)
    print("The converted rate is:", output)

intro()

