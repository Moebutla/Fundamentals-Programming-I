##
#  Stock profit calculator
#  Author:  Mose Butler
#  Date:    09/15/2018
#  Version: 1.0.0
##

# Commission rate is set by stockbroker.
COMMISSION_RATE = 0.03

# Declare Variables
share_qty = float(input("How many share would you like to purchase: "))
purchase_price = float(input("What is purchase price per share (in USD): "))
sell_price = float(input("What sell price per share (in USD): "))
isGain = False

# functions to find total spent on purchase, and commission of purchase.
total_purchase = share_qty * purchase_price
purchase_commission = total_purchase * COMMISSION_RATE

# functions to find total made from sale, and commission of sale.
total_sell = share_qty * sell_price
sell_commission = total_sell * COMMISSION_RATE

# Find amount you have left
profit = total_sell - sell_commission - purchase_commission - total_purchase

if profit > 0:
    isGain = True
else:
    isGain = False
    profit = -1 * profit

if isGain:
    print("After the transaction, you gained %s dollars." % round(profit, 2))
else:
    print("After the transaction, you lost %s dollars." % round(profit, 2))
