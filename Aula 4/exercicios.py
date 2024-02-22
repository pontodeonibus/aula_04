#Exercicios Aula 4

#1 concatene uma cidade e um adjetivo para ela

#adjetivo = "é suja"
#cidade = input("Escolha uma cidade: ")
#print('{} {}' .format(cidade, adjetivo))

#2 concatene uma viagem e quem vai participar dela

#lugar = input("Para onde você viajará?: ")
#pessoas = input('Quem vai?: ')
#print('Você vai para {} com {}' .format(lugar, pessoas))

#3 concatene um programador: sua função, seu nome e seu usuario  

programador = input("Nome do programador: ")
funcao = input("Função: ")
usuario = input("Usúario: ")
print("O nome do programador é {}, seu usuário é {} e sua função é {}" .format(programador, usuario, funcao))

#Exercicios Aula 5

#1 Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número

numero = int(input('Escolha o número: '))
expoente = 2
resultado = numero ** expoente
print("O resultado de {} elevado a {} é {}" .format(numero, expoente, resultado))

#2 Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print(nome, sobrenome)

#3 Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

n1 = input('Escolha um número: ')
n2 = input('Escolha outro número: ')
print(f'Os números escolhidos foram {n1} e {n2}')

#4 Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado

name = "Python"
number = input('Escolha um número: ')
print('{}{}' .format(name, number))

#5 *Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

frase = "Eu gosto muito de jogar"
print(frase)
palavra = input()
print(frase, palavra)