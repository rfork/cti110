# CTI-110
# P3HW1 - Color Mixer
# Katie Rutherford 
# 25Feb2019
#

# Chapter 3 Exercise #7 (Color Mixer)
# This program displays the secondary color that would be created from 2
#   primary colors, input by the user

# Pseudocode:
# Get 2 colors from the user
# If either color is not 'red', 'blue', or 'yellow', display an error
# If the 2 colors are red and blue, display purple as the result
# If the 2 colors are red and yellow, display orange as the result
# If the 2 colors are blue and yellow, display green as the result


# Get color1 from the user
print('Which colors would you like to mix?')
print('You may choose red, blue, or yellow')
color1 = input('\tFirst color: ')

# Test that color1 is valid primary color
if color1 != 'red' and color1 != 'blue' and color1 != 'yellow':
    # color not valid, print error message
    print('Whoops! That is not a primary color!')

# color1 is good, get color2 from user
else:
    color2 = input('\tSecond color: ')

    # Test that color2 is valid primary color
    if color2 != 'red' and color2 != 'blue' and color2 != 'yellow':
        print('Whoops! That is not a primary color!')

    # Test that color1 and color2 are different colors
    elif color1 == color2:
        print('Hmm, it seems you have a lot of the color', color1)

    # If one color is red and the other is blue, the result is purple
    elif (color1 == 'red' and color2 == 'blue') or \
         (color1 == 'blue' and color2 == 'red'):
        print(color1, 'and', color2, 'make purple!')
    # If one color is red and the other is yellow, the result is yellow
    elif (color1 == 'red' and color2 == 'yellow') or \
         (color1 == 'yellow' and color2 == 'red'):
        print(color1, 'and', color2, 'make orange!')

    # If one color is yellow and the other is blue, the result is green
    elif (color1 == 'yellow' and color2 == 'blue') or \
         (color1 == 'blue' and color2 == 'yellow'):
        print(color1, 'and', color2, 'make green!')

