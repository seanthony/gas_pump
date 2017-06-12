


# all functions above here
# all code below here

# welcome message and choose pre-pay or pay after
print('Hello')
decision = input('Enter 1 to pre-pay or 2 to pay after?')

# pre-pay
if decision == '1':
    # get the money
    money = float(input('How much money?\n'))
    # get the gas type
    gas_type = input('Would you like reg, mid or prem?')
    if gas_type == 'reg':
        price = 1.99
    elif gas_type == 'mid':
        price = 2.04
    elif gas_type == 'prem':
        price = 2.09
    else:
        price = 99.99
    # calculate the gallons
    gallons = money / price
    # tell user the output
    print('You got', round(gallons, 2), 'gallons of gas.')


# pay after
# elif decision == '2':
    # get the gallons

    # get the gas type

    # calculate the money

    # tell the user the output

