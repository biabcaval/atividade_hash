class Hash_table:
  def __init__(self, s):
      self.size = int(s * 1.25)
      self.first_level = [[] for _ in range(self.size)]  # Primeiro nível com "size" ponteiros para listas vazias
      self.second_level_size = self.size // 10 # isso representa o número de tabelas no segundo nível
      self.second_level = [[[] for _ in range(self.second_level_size)] for _ in range(10)]
  
  def __hash_str(self, key_str):
    if type(key_str) == str:
      num = 0
      for c in key_str:
          num += ord(c)
      return num
    else:
      num = key_str
      return num
  
  def __hash(self, key_str):
      key = self.__hash_str(key_str)
      return key % 10  # Usando 10 como divisor para o primeiro nível
  
  def __hash2(self, key_str):
      key = self.__hash_str(key_str)
      return key % self.second_level_size  # Usando second_level_size como divisor para o segundo nível
  
  def insert(self, key, value):
      first_level_pos = self.__hash(key)
      second_level_pos = self.__hash2(key)
      self.second_level[first_level_pos][second_level_pos].append(value)

  def remove(self, key):
    first_level_pos = self.__hash(key)
    second_level_pos = self.__hash2(key)
    aluno_list = self.second_level[first_level_pos][second_level_pos]
    for aluno in aluno_list:
        if aluno.nome == key:
            self.second_level[first_level_pos][second_level_pos].remove(aluno)

    
    

  def get(self, key):
    lista_alunos = []
    first_level_pos = self.__hash(key)
    second_level_pos = self.__hash2(key)
    aluno_list = self.second_level[first_level_pos][second_level_pos]
    for aluno in aluno_list:
        if aluno.nome == key:
            lista_alunos.append(aluno.to_string())
    
    return lista_alunos  # Se a chave (nome) não for encontrada, retorna lista vazia
  
  def print(self):
      print("{")
      for i in range(10):
          first_level_list = self.second_level[i]
          for j in range(self.second_level_size):
              alunos = first_level_list[j]
              _str = ""
              for aluno in alunos:
                  _str += aluno.to_string() + " "
              print("[{}]".format(_str))
      print("}")



class Aluno:

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula

  def to_string(self):
    return "Nome: " + self.nome + " - Matrícula: " + str(self.matricula) + ", "


a1 = Aluno("Maria", 12)
a2 = Aluno("João", 6)
a3 = Aluno("José", 24)
a4 = Aluno("Lucas", 36)
a5 = Aluno("Matheus", 3)
a6 = Aluno("Simão", 7)
a7 = Aluno("Maria Rita", 13)

ht = Hash_table(10)
ht.insert(a1.nome, a1)
ht.insert(a2.nome, a2)
ht.insert(a3.nome, a3)
ht.insert(a4.nome, a4)
ht.insert(a5.nome, a5)
ht.insert(a6.nome, a6)
ht.insert(a7.nome, a7)
ht.print() # exibindo a tabela 

print(ht.get(a1.nome)) # achando a matrícula de um aluno na tabela com base em seu nome
ht.remove(a1.nome) # removendo um aluno da tabela
ht.print() # exibindo a tabela atualizada

