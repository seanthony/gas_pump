# don't code like this!
prices, decision = {'regular': 2.351, 'mid-grade': 2.638, 'premium': 2.883}, input('Welcome\nHow can we help today?\n\tpre-pay\n\tpay-after\n')
if decision == 'pre-pay':
    msg_1, msg_2, val, boo = 'dollars paid for', 'gallons of gas', float(input('How many dollars? $')), True
else:
    msg_1, msg_2, val, boo = 'gallons of gas cost', 'dollars', float(input('How many gallons? ')), False
gas_type = input('What type of gas would you like today?\n\tregular\n\tmid-grade\n\tpremium\n')
if boo:
    print(val, msg_1, round(val / prices[gas_type], 2), msg_2)
else:
    print(val, msg_1, round(val * prices[gas_type], 2), msg_2)