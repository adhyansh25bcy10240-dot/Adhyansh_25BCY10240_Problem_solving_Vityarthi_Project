# PROJECT DESCRIPTION
The goal of this project is to generate secure passwords
for the user for multiple platforms. This password generator uses the
random function to generate randomised passwords with compulsion
of alphabets,numbers,first letter being capital and minimum number
of 8 characters. This program has a lot of applications in the field of cybersecurity
as with increase in computational power along with decrease in price of strong computers
, the vulnerability of passwords being cracked has increased. 

It uses the following python concepts:-
1. String(str)
2. Integer(int)
3. Boolean(bool)
4. Dictionary(dict)
5. random.choice()
6. while loop

# ALGORITHM
STEP 1: Start the program

STEP 2: create a storage dictionary passes = {}

STEP 3: Add a random First character to the password

STEP 4: Let user input length(minimum 8 characters), use_numbers(compulsory), use_symbols (yes/no), and platform_name

STEP 5: Create a character pool containing alphabets (A-Z)

STEP 6: If the user chose "yes" for numbers, add digits (0-9) to the pool

STEP 7: If the user chose "yes" for symbols, add special characters (!@#) to the pool

STEP 8: Pick a random character from the pool and add it to the password

STEP 9: Repeat step 8 until the password reaches the desired length

STEP 10: Save the generated password in the dictionary using the platform name

STEP 11: Print the generated password for the user to see when user enters correct platform name

STEP 12: If the platform name is not a part of the dictionary, print "Not Found"

STEP 13: Ask the user if he/she wants to create password for another platform(yes/no), if yes then repeat all steps above, otherwise end the program

# PROGRAM USED

Programming Language: Python was used.

Version Control: Git and GitHub were utilized.

Code Editor: VS Code (Visual Studio Code) was the code editor



# Made by- (Adhyansh Raina,25BCY10240)
