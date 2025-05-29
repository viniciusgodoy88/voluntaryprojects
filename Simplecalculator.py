"""
Project: Simple Calculator
Onwer: Vinicius Godoy
Platform: Udemy
Data: 26/05/2025
Teacher: Ryan Aragão
"""

from typing import Any

#Usuário digitará o primeiro número
n1 = int(input("Digite o primeiro Numero: "))
#Usuário digitará a operação desejada
operacao = str (input("Digite o operacão: "))
#Usuário digitará o segundo número
n2 = int(input("Digite o segundo Numero: "))


#Variáveis e seus tipos
subtracao = float
divisao = float
multiplicacao = int
potenciacao = int
resdivisao = float

#Se o usuário desejar que a calculadora faça uma operação de soma, a função será a de baixo
if operacao == "+":
    soma = n1 + n2
    print("A soma entre {} + {} = {}".format(n1, n2, soma))
#Se o usuário desejar que a calculadora faça uma operação de subtração, a função será a de baixo
elif operacao == "-":
    subtracao = n1 - n2
    print("A subtração entre {} - {} = {}".format(n1, n2, subtracao))
#Se o usuário desejar que a calculadora faça uma operação de multiplicação, a função será a de baixo
elif operacao == "*":
    multiplicacao = n1 * n2
    print("A multiplicação entre {} * {} = {}".format(n1, n2, multiplicacao))
#Se o usuário desejar que a calculadora faça uma operação de potenciação, a função será a de baixo
elif operacao == "**":
    potenciacao = n1 ** n2
    print("A Potenciação entre {}**{} = {}".format(n1, n2, potenciacao))
#Se o usuário desejar que a calculadora faça uma operação de resto de divisão, a função será a de baixo
elif operacao == "//":
    resdivisao = n1 // n2
    print("O resto da divisão entre {} // {} = {}".format(n1, n2, resdivisao))
#Se o usuário desejar que a calculadora faça uma operação de divisão, a função será a de baixo
else:
    divisao = n1 / n2
    print("A divisão entre {} / {} = {}".format(n1, n2, divisao))