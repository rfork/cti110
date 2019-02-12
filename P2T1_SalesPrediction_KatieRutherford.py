# This program asks the user for the projected amount of
#   total sales, calculates the projected profit made from
#   the total sales (23%), and displays the projected profit
# 11Feb2019
# CTI-110 P2T1 - Sales Prediction
# Katie Rutherford
#

# Get projected total sales as imput
totalSales = float(input('Enter projected sales: '))

# Calculate profit as 23% of total sales
profit = totalSales * 0.23

# Display the profit
    # format ',.2f' formats profit to have 2 decimal
    #        spaces and commas every hundredth place
    # sep='' changes the seperator between the printed string and
    #        the variable from a blank space to no spaces
print('Your projected profit is $', format(profit, ',.2f'), sep='')
