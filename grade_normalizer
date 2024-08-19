# This tool helps a teacher normalize the grades of a class 
# by calculating the gain (m or slope) and offset (c or y-intercept) 
# given the minimum and maximum grades obtained and the desired minimum and maximum grades.
# The teacher can use the calculated gain and offset to normalize grades in Excel.

# Function to calculate gain (m) and offset (c)
def normalize_grades(min_obtained, max_obtained, min_desired, max_desired):
    # Calculate the gain (m)
    m = (max_desired - min_desired) / (max_obtained - min_obtained)
    # Calculate the offset (c)
    c = min_desired - m * min_obtained
    return m, c

# Take user input for the minimum and maximum grades obtained
min_obtained = float(input("Enter the minimum grade obtained: "))
max_obtained = float(input("Enter the maximum grade obtained: "))

# Take user input for the desired minimum and maximum grades
min_desired = float(input("Enter the desired minimum grade: "))
max_desired = float(input("Enter the desired maximum grade: "))

# Calculate and print the gain (m) and offset (c)
m, c = normalize_grades(min_obtained, max_obtained, min_desired, max_desired)
print(f"Gain (m): {m}")
print(f"Offset (c): {c}")

# Excel formula to normalize grades:
# Assuming the existing grade is in cell D2 and the normalized grade should be in cell E2:
# In cell E2, use the formula: =(D2*m)-c
print(f"To normalize grades in Excel, use the formula: =(D2*{m})-{c} in the output cell (e.g., E2) where D2 contains the existing grade.")
