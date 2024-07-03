# AULA 198, 199
""" class - Classes são moldes oara criar novos objetos 
as classes geram novos objetos (isntâncias) que
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe de podem usar seus dados
internos para realizar várias ações.
por convenção, usamos PascalCase para nomes de classes
"""
# string = 'Luiz'
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    # atributos -> dados
    # métodos -> funções

    # uma das primeiras coisas que é feia quando uma classe é iniciada: 
    def  __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('luiz', 'otavio')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)