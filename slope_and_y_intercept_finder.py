# This tool calculates the slope (m) and y-intercept (c) of a line
# given two points (x1, y1) and (x2, y2).
# It takes user input for the coordinates of the two points
# and prints the slope and y-intercept.

# Function to calculate slope and y-intercept
def slope_m_c(x1, y1, x2, y2):
    # Calculate the slope (m)
    m = (y2 - y1) / (x2 - x1)
    # Calculate the y-intercept (c)
    c = y2 - m * x2
    return m, c

# Take user input for the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Take user input for the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate and print the slope and y-intercept
print(slope_m_c(x1, y1, x2, y2))
