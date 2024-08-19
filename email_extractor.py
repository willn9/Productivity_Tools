# This tool will take an email header saved in a text file 
# and convert it into an email list in the form of a CSV file 
# with 3 columns for first_name, last_name, and email.  
# Your contacts file should be named raw_contacts.txt or change file_path below.

# Importing libraries
import re
import csv

# Read the content of the text file
file_path = 'raw_contacts.txt'
with open(file_path, 'r') as file:
    content = file.read()

# Extract email addresses using regular expressions
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

# Function to split email into first name, last name, and email address
def split_email(email):
    name_part = email.split('@')[0]
    first_name, last_name = name_part.split('.')
    return first_name, last_name, email

# Write the extracted data to a CSV file
output_file_path = 'new_contacts.csv'
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First Name', 'Last Name', 'Email'])
    for email in emails:
        first_name, last_name, email = split_email(email)
        writer.writerow([first_name, last_name, email])

print(f"Emails have been extracted and saved to {output_file_path}")
