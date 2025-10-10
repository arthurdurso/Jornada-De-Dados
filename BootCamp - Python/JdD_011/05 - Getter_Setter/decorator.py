class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Idade deve ser um número positivo.")

pessoa = Pessoa("Arthur", 24)

print("Nome: ", pessoa.nome)

print("Idade: ", pessoa.idade)

pessoa.nome = "Duda"
pessoa.idade = 22

print("Nome: ", pessoa.nome)

print("Idade: ", pessoa.idade)

pessoa.idade = -1