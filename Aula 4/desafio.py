#DESAFIO

#Crie um sistema de calculadora 
#concatenar as saídas
#SOMA | DIVISÃO | MULTIPLICAÇÃO | SUBSTRAÇÃO 
#UTILIZAR input() - print() -  `+ ` |- |/ |- ** - 

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

soma = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2
pot = n1**n2
div2 = n1//n2

print("Soma: {} + {} = {}".format(n1, n2, soma))
print("Subtração: {} - {} = {}".format(n1, n2, sub))
print("Multiplicação: {} * {} = {}".format(n1, n2, mul))
print("Divisão: {} / {} = {}".format(n1, n2, div))
print("Potencia: {} ** {} = {}".format(n1, n2, pot))
print("Divisão (apenas inteiro): {} // {} = {}".format(n1, n2, div2))