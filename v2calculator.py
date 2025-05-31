"""
Project: Calculator V2
Onwer: Vinicius Godoy
Platform: Udemy
Data: 31/05/2025
Teacher: Ryan Aragão
"""
def welcome():
    print("Welcome to Calculator V2! ")

first_numero = int(input("Please insert the first value: "))
second_numero = int(input("Please insert the second value: "))

while True:
    welcome()
    print(""""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
       """)

option = int(input("Insert the required option: "))

if option == 1:
    addition = first_numero + second_numero
    print("The addition is: ", addition)
elif option == 2:
    subtraction = first_numero - second_numero
    print("The subtraction is: ", subtraction)
elif option == 3:
    multiplication = first_numero * second_numero
    print("The multiplication is: ", multiplication)
elif option == 4:
    division = first_numero / second_numero
    print("The division is: ", division)
else:
    print("Option Not Found, please try again !")
