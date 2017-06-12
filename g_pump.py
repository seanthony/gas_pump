from time import sleep

def det_gas_price(option):
    """(str)->(float)
    matches a string choice to send a message to the 
    user and return the price of gas
    for invalid choices it will return false
    >>> det_gas_price('1'):
    print('You have selected our Regular Gasoline')
    2.351
    >>> det_gas_price('2'):
    2.638
    >>> det_gas_price('3'):
    2.883
    >>> det_gas_price('4'):
    2.502
    >>> det_gas_price('other'):
    False
    """
    if option == '1':
        print('You have selected our Regular Gasoline.')
        return 2.351
    elif option == '2':
        print('You have selected our Mid-Grade Gasoline, good choice!')
        return 2.638
    elif option == '3':
        print('You have selected our best product, Premium Gasoline. Excellent choice!')
        return 2.883
    elif option == '4':
        print('You have selected our Diesel Fuel.')
        return 2.502
    else:
        print('Invalid Section\nYou entered: ', option)
        return False
    
def pre_pay(money, gas_price):
    """(num, num) -> num
    returns the number of gallons pumped for an amount
    of money entered with a determined gas price
    >>> pre_pay(20.0, 2.0)
    10.0
    >>> pre_pay(9.0, 2.25)
    4.0
    """
    return money / gas_price

def pay_after(gallons, gas_price):
    """(num, num) -> num
    returns the cost of the pumped amount
    of gas with a determined gas price
    >>> pre_pay(10.0, 2.0)
    20.0
    >>> pre_pay(4.0, 2.25)
    9.0
    """
    return gallons * gas_price

def pump():
    input('Press Enter to begin pumping.')
    print('pumping...')
    sleep(3)
    return None

def main():
    # welcome user to store
    print('WeLcOmE tO sEaN\'s GaS bOnAnZa!')
    print(""" 
      ___
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'
            """)
    # get user's gas
    msg = '''What type of gas would you like to purcahse today?
    \tSelect 1 for Regular Gas at $2.351 / gallon
    \tSelect 2 for Mid-Grade Gas at $2.638 / gallon
    \tSelect 3 for Premium Gas at $2.883 / gallon
    \tSelect 4 for Diesel Gas at $2.502 / gallon\n1, 2, 3, or 4?\n'''
    gas_option = input(msg)
    
    # check the user choice to determine gas price
    gas_price = det_gas_price(gas_option)
    if not gas_price:
        print('Please Try Again.')
        return None
    
    # user selects pay at pump or pay cashier later
    msg = '''How would you like pay today?
    \tSelect 1 to pay here at the pump using your card.
    \tSelect 2 to pre-pay inside using cash or card.\n1 or 2?\n'''
    pump_option = input(msg)
    if pump_option == '1':
        gal = float(input('How many gallons would you like to purchase?\n(valid numbers only)\n'))
        cost = pay_after(gas_price, gal)
        pump()
        print('Thank you for shopping today, your final cost is $', round(cost, 2), sep='')
        return None
    elif pump_option == '2':
        money = float(input('How much would you like to spend today?\n(valid dollar amounts only)\n$'))
        gal = pre_pay(money, gas_price)
        pump()
        print('Thank you for shopping today, you were able to purchase', round(gal, 2), 'gallons of gas.')
        return None
    else:
        print('Invalid Selection, please try again')
        return None

main()