class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_idade(self):
        return self.idade
    
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.idade = nova_idade
        else:
            print("Idade deve ser um número positivo.")

pessoa = Pessoa("Arthur", 24)

print("Nome: ", pessoa.get_nome())

print("Idade: ", pessoa.get_idade())

pessoa.set_nome("Duda")
pessoa.set_idade(22)

print("Nome: ", pessoa.get_nome())

print("Idade: ", pessoa.get_idade())

pessoa.set_idade(-1)