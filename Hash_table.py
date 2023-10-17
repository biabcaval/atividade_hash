# -*- coding: utf-8 -*-


class Hash_table:
    def __init__(self, s):
        self.size = int(s* 1.25)
        self.T = [[] for _ in range(self.size)]
     
    def __hash_str(self, key_str):
        num = 0
        for c in key_str:
            num += ord(c)
        return num

        # Criar primeiro nivel do hash, onde vai um vetor com 10 espaços onde cada item é uma lista

    def primeiro_nivel(self, n = 10):
      for i in range(n):
          self.T.append([]) # criará n listas dentro da tabela hash

  # ajustar a hash de modo que ela coloque os itens de um mesmo conflito em um dos vetores do primeiro nível
    def __hash(self, key_str):
        key = self.__hash_str(key_str)
        return key % self.size

    def __hash2(self,pos, value):
        key = self.__hash_str(key_str)
        return key % (self.size // 10)
        
      
    
    def insert(self, key, value):
        pos = self.__hash(key)
        self.T[pos].append(value) # adiciona nesse formato os itens
    
    def get(self, key):
        pos = self.__hash(key)
        L = self.T[pos]
        for value in L:
            if(value.matricula == key):
                return value
        return None
            
    def print(self):
        print("{")
        for i in range(self.size):
            alunos = self.T[i]
            _str = ""
            for aluno in alunos:
                _str += aluno.to_string() + " "
            print("[" + _str + "]")
        
        print("}")


        
class Aluno:

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula

  def to_string(self):
    return self.nome + " - " + str(self.matricula)


a1 = Aluno("Maria", 12)
a2 = Aluno("João", 6)
a3 = Aluno("José", 24)
a4 = Aluno("Lucas", 36)
a5 = Aluno("Matheus", 3)
a6 = Aluno("Simão", 7)

ht = Hash_table(10)
ht.insert(a1.nome, a1)
ht.insert(a2.nome, a2)
ht.insert(a3.nome, a3)
ht.insert(a4.nome, a4)
ht.insert(a5.nome, a5)
ht.insert(a6.nome, a6)

ht.print()
#aluno = ht.get()
#print(aluno.to_string())
