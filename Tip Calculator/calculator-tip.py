# Cass Terrell-Burleson
# June 12, 2023
# This program has the user input a service cost and percentage to calculate the total tip the user should give in dollars and cents.

# program header
DASHES = "-" * 15
print(DASHES)
print("Tip Calculator")
print(DASHES)
# get input from the user

serviceCost = float(input("Cost of service:\t\t"))
tipPercentage = float(input("Tip Percentage i.e. 15, 20, 25:\t\t")) / 100

# calculate tip
tip = float(serviceCost * tipPercentage)
totalAmt = tip + serviceCost

# :, thousands seperator
# .2f limits string to 2 decimal places
tipInDollars = '${:,.2f}'.format(tip)
amtInDollars = '${:,.2f}'.format(totalAmt)

# print totals
print(DASHES)
print(f"Tip Amount:\t{tipInDollars}\nTotal Amount:\t{amtInDollars}")