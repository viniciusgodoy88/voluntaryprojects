"""
Exercício de Lógica
Autor: Vinicius Godoy
Data: 27/05/2025
Plataforma: Udemy
Professor: Ryan Aragão
"""

lista = ['Vinicius', 'Lethicia', 'Olivete', 'Marcia', 'Julia', 'JP', 'Junior', 'Idália']

while True:
    print("""
        1. Adicionar Pessoa
        2. Buscar por Pessoa
        """)

escolha = int(input("Digite a opção desejada: "))
if escolha == 1:
    pessoa = input("Digite o nome a ser adicionado: ")
    lista.append(pessoa)

    if escolha == 2:
        pessoa = input("Digite o nome a ser buscado: ")

if pessoa in lista:
    print("Pessoa adicionada com sucesso!")
elif pessoa not in lista:
    print("Pessoa não esta na lista")
else:
    print("Pessoa invalida")
