"""
Logic Exercise
Onwer: Vinicius Godoy
Data: 27/05/2025
Plataform: Udemy
Professor: Ryan Aragão
"""

list = ['Vinicius', 'Lethicia', 'Olivete', 'Marcia', 'Julia', 'JP', 'Junior', 'Idália']

while True:
    print("""
        1. Including People
        2. Search People
        """)

choice = int(input("Insert the required option: "))
if choice == 1:
    people = input("Insert the name to including: ")
    lista.append(people)

    if choice == 2:
        people = input("Insert the name to search: ")

if people in list:
    print("People inserted successfully! ")
elif people not in list:
    print("Sorry, the people doensn't in the list")
else:
    print("Invalid People")
