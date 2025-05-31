"""
Project: Simple Calculator
Onwer: Vinicius Godoy
Platform: Udemy
Data: 26/05/2025
Teacher: Ryan Aragão
"""

from typing import Any

#User inserted a first number
n1 = int(input("Insert the first number: "))
#User inserted the required option
option = str (input("Insert the operator: "))
#User inserted a second number
n2 = int(input("Insert the second number: "))


#variables and your types
addiction = int
subtraction = float
division = float
multiplication = int
potentiation = int
resdivision = float

#If the user required the calculator do the addiction, the funcion is below
if option == "+":
    addiction = n1 + n2
    print("A soma entre {} + {} = {}".format(n1, n2, addiction))
#If the user required the calculator do the subtraction, the funcion is below
elif option == "-":
    subtraction = n1 - n2
    print("A subtração entre {} - {} = {}".format(n1, n2, subtraction))
#If the user required the calculator do the multiplication, the funcion is below
elif option == "*":
    multiplication = n1 * n2
    print("A multiplicação entre {} * {} = {}".format(n1, n2, multiplication))
#If the user required the calculator do the potentiation, the funcion is below
elif option == "**":
    potentiation = n1 ** n2
    print("A Potenciação entre {}**{} = {}".format(n1, n2, potentiation))
#If the user required the calculator do the rest of division, the funcion is below
elif option == "//":
    resdivision = n1 // n2
    print("O resto da divisão entre {} // {} = {}".format(n1, n2, resdivision))
#If the user required the calculator do the division, the funcion is below
else:
    division = n1 / n2
    print("A divisão entre {} / {} = {}".format(n1, n2, division))
