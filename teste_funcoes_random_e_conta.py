### etapa1 ###
import random
from random import choices, sample

numeros_impares = [0,2,4,6,8]
numeros_pares = [1,3,5,7,9]

lista = numeros_impares
lista = numeros_pares

for numeros_impares in lista:
    if numeros_impares % 2 == 0:
        print(lista)

lista = numeros_pares
for numeros_pares in lista:
    if numeros_pares % 1 == 3:
        print(lista)

def numeros_aleatorios(self, lista):
    self, lista = lista
    lista = []

    while lista != 50:
        for l in range(0,15):
            lista.append(random.randint(1,50))
            lista.sort()
            return lista

            lista = numeros_aleatorios()
            print(f'sua lista e: {lista}')

tamanho = 15
tamanho = 15
valores = range(1,50)

print(choices(valores, k=tamanho))
print(sample(valores, tamanho))
print(sample(valores, tamanho))

class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.titular = nome
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente para saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


conta = ContaBancaria("João", 1000)

conta.consultar_saldo()

conta.depositar(500)
conta.consultar_saldo()