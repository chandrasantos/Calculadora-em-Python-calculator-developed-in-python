#!/usr/bin/env python
# coding: utf-8

# # <p style="color:#FF1493; background-color:#1C1C1C">Propósito do Desafio é criar uma calculadora em Python</p>
# 
# 
# ## <p style="color:#DC143C">O que ela deve fazer?</p>
# 
# <b> Sequência do Algoritmo </b>
# 
# Dar boas-vindas ao usuário e pedir para ele escolher uma das quatro operações básicas de matemática:
# 
# 1- Soma
# 
# 2- Subtração
# 
# 3- Multiplicação
# 
# 4- Divisão
# 
# 
# Em seguida, o usuário precisará digitar o primeiro número. 
# 
# Em seguida, o usuário precisará digitar o segundo número. 
# 
# A calculadora retornará com o resultado. 
# 
# Caso o usuário digite uma operação matemática não listada, deve retornar mensagem de erro.

# In[ ]:


print ('Bem-Vindo! Obrigada por usar a calculadora da Chandra :D Volte sempre!')
print ('Escolha uma das opções abaixo:')
print ('[1]soma','[2]subtração', '[3]multiplicação','[4]divisão')
escolha = input('Digite a opção (1,2,3,4):')

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))

def soma (a,b):
	return a + b
def subtração(a,b):
	return a - b
def multiplicação (a,b):
	return a * b
def divisão (a,b):
	return a / b

if escolha =='1':
	print (a+b)

elif escolha =='2':
	print (a-b)

elif escolha =='3':
    print (a*b)

elif escolha =='4':
    print (a/b)
    
else:
    print ('você não escolheu uma opção entre 1 e 4. Refaça a operação')

