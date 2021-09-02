'''nomes = ['Milena','Roberta','Lucimara','roberto']

for nome in nomes:
    print(nome)
    #isso é uma estrutura de laço

    i=0
    while i<10:
        print('i ainda é menor que 10:',i)
        i+=1

numero = 0

while True:
        print(numero)
        if numero==20:
            break
        numero+=1'''

'''exercicio: faça um programa que leia a quantidade de pessoas
que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e 
colocar numa lista de convidados e imprimir todos os nomes da lista'''

print('programa de controle de festas')
numero_de_convidados= input('coloque o numero de convidados')
lista_de_convidados= []
i=1
while i <= int(numero_de_convidados):
    nome_do_convidado=input('coloque o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i+=1

for convidado in lista_de_convidados:
    print(convidado)