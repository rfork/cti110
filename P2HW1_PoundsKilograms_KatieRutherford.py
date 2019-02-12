
# This program converts pounds to kilograms, using the 
#   formula kg = lb/2.2046
# 11Feb2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Katie Rutherford
#
# Pseudocode:
# Get pounds as input from user
# Calculate kilograms from pounds (kg = lb/2.2046)
# Display kilograms

# Get pounds as input from user, convert it to float
pounds = float(input('Enter amount in pounds: '))

# Calculate amount in kilograms
kilograms = pounds / 2.2046

# Display kilograms
print(pounds, 'pounds is approximately', \
      format(kilograms, ',.2f'), 'kilograms.')

