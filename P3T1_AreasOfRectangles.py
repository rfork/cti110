# CTI-110
# P3T1 - Areas of Rectangles
# Katie Rutherford
# 25Feb2019
#

# This program calculates the area of 2 rectangles and determines
#   which rectangle has the greater area, or if the rectangles
#   are the same size

# Get input for first rectangle
Length1 = float(input('Enter length of first rectangle: '))
Width1 = float(input('Enter width of first rectangle: '))

# Calculate area of first triangle
Area1 = Length1 * Width1

# Get input for second triangle
Length2 = float(input('Enter length of second rectangle: '))
Width2 = float(input('Enter width of second rectangle: '))

# Calculate area of second triangle
Area2 = Length2 * Width2

# Determine which area is larger, or if they are equal
if Area1 > Area2:
    print('The first rectangle has a greater area than the \
second rectangle')
elif Area2 > Area1:
    print('The second rectangle has a greater area than the \
first rectangle')
else:
    print('Both rectangles have the same area')
