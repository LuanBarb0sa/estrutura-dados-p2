# Construa uma Fila de Prioridade utilizando a linguagem Python em que sejam
# implementadas as funções para inserção de um novo elemento (inteiro) na fila e a
# remoção do elemento de mais alta prioridade


import numpy as np
class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("Pilha  cheia!")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("Pilha vázia!")
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def imprimir_inversamente(self):
        pilha_inversa = []
        for i in self.valores[::-1]:
            pilha_inversa.append(i)

        return pilha_inversa
        
pilha = Pilha(5)
pilha.empilhar(3)
pilha.empilhar(7)
pilha.empilhar(2)
pilha.empilhar(5)
pilha.empilhar(1)
pilha.empilhar(8)

print(pilha.imprimir_inversamente())
# Aluno: Luan Lucas Barbosa
