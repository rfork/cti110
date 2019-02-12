# This program calculates the total amount of a meal(plus tips)
#   purchased at a restaurant
# 12Feb2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Katie Rutherford
#

# Pseudocode
# Get amount charged for food from user
# Calculate a tip percentage of 15%
# Calculate total meal cost with a tip of 15%
# Calculate a tip percentage of 18%
# Calculate total meal cost with a tip of 18%
# Calculate a tip percentage of 20%
# Calculate total meal cost with a tip of 20%
# Display different tip amounts calculated (for 15%, 18%, and 20%)
# Display the meal's total cost for each tip amount


# Get amount charged for food from user, convert to a float
mealCost = float(input('Enter amount charged for your meal: '))

# Calculate tip amount as 15%
tip15 = mealCost * 0.15

# Calculate total meal cost with a tip of 15%
mealTotal15 = mealCost + tip15

# Calculate tip amount as 18%
tip18 = mealCost * 0.18

# Calculate total meal cost with a tip of 18%
mealTotal18 = mealCost + tip18

# Calculate tip amount as 20%
tip20 = mealCost * 0.20

# Calculate total meal cost with a tip of 20%
mealTotal20 = mealCost + tip20

# Display tip percentage, tip amount, and total cost of meal:
print('Here are some commonly used tipping percentages: ')

# Format tip amounts on the left, and total(meal plus tip) on right
# I could have used only one print comment, but I think the code
#   formatting looks easier to read this way
print('\t15% tip = $', format(tip15, ',.2f'),
      '\tTotal Meal plus 15% Tip = $', format(mealTotal15, ',.2f'),
      '\n\t18% tip = $', format(tip18, ',.2f'),
      '\tTotal Meal plus 18% Tip = $', format(mealTotal18, ',.2f'),
      '\n\t20% tip = $', format(tip20, ',.2f'),
      '\tTotal Meal plus 20% Tip = $', format(mealTotal20, ',.2f'), sep='')




