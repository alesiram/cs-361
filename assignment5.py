
print("*******************************************")
print("**********************************************\n")
print( 'Hi there! Welcome to Your Currency Converter \n ')
print("**********************************************")
print("*******************************************")


program_start = input('\nTo begin, enter "start" or press "1": ')
print('to exit enter "0"')

print("\nCurrent Countries available for your currency excahnge: ", "\n********************", "\n","USD", "AUD", "BGN", "CAD",'\n' "CHF", "CNY", "EGP", "EUR", "GBP", "\n********************")



def intro():
    if program_start == "start" or "Start" or "1":
        current_country = input( 'Enter source currency: '"\n")
        target_currency = input( 'Enter target currency".'"\n")

        amount = input("How much do you want to send? ")
        amount = float(amount)
        print('Thanks, please hold...')
        convertor(current_country, target_currency, amount)


def convertor(current_country, target_currency , amount):
    exchange_rate = 0
    country_rates ={
    "USD": 1,
    "AUD": 1.4817,
    "BGN": 1.7741,
    "CAD": 1.3168,
    "CHF": 0.9774,
    "CNY": 6.9454,
    "EGP": 15.7361,
    "EUR": 0.9013,
    "GBP": 0.7679 }

    current_country_rate = 0
    target_currency_rate = 0
    for i in country_rates:
        if i == current_country:
            current_country_rate = float(country_rates[i])
        if i == target_currency:
            target_currency_rate = float(country_rates[i])

        division = float(current_country_rate / target_currency_rate)
        exchange_rate = float(division * amount)


    print(exchange_rate)



intro()
