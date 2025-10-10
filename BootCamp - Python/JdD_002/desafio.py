# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if not nome.strip():
        raise ValueError("O nome não pode estar vazio.")
    
    # Verifica se o nome contém números
    if any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode conter números.")
    
    # Verifica se o nome contém caracteres especiais (exceto espaço)
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\"
    if any(char in caracteres_especiais for char in nome):
        raise ValueError("O nome não pode conter caracteres especiais.")
    
    # Verifica se o nome é muito curto (por exemplo, com menos de 2 caracteres)
    if len(nome.strip()) < 2:
        raise ValueError("O nome é muito curto. Deve ter pelo menos 2 caracteres.")
    
    # Verifica se o nome é muito longo (por exemplo, com mais de 50 caracteres)
    if len(nome.strip()) > 50:
        raise ValueError("O nome é muito longo. Deve ter no máximo 50 caracteres.")

except ValueError as e:
    print(e)
    
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario_input = input("Qual o valor do seu salário? ")

    # Verifica se a entrada está vazia
    if not salario_input.strip():
        raise ValueError("A entrada não pode estar vazia. Por favor, digite um número.")

    # Substitui vírgulas por pontos (caso o usuário use vírgula como separador decimal)
    salario_input = salario_input.replace(',', '.')

    # Converte a entrada para float
    salario = float(salario_input)

    # Verifica se o salário é um valor negativo
    if salario < 0:
        raise ValueError("O salário não pode ser um valor negativo.")

    # Verifica se o salário é zero ou próximo de zero
    if salario == 0:
        raise ValueError("O salário deve ser maior que zero.")
    

except ValueError as e:
    print(e)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus_input = input("Qual o valor do seu bonus? ")

    # Verifica se a entrada está vazia
    if not bonus_input.strip():
        raise ValueError("A entrada não pode estar vazia. Por favor, digite um número.")

    # Substitui vírgulas por pontos (caso o usuário use vírgula como separador decimal)
    bonus_input = bonus_input.replace(',', '.')

    # Converte a entrada para float
    bonus = float(bonus_input)

    # Verifica se o salário é um valor negativo
    if bonus < 0:
        raise ValueError("O salário não pode ser um valor negativo.")

    # Verifica se o salário é zero ou próximo de zero
    if bonus == 0:
        raise ValueError("O salário deve ser maior que zero.")
    

except ValueError as e:
    print(e)
    
# 4) Calcule o valor do bônus final

CONSTANTE_BONUS = 1000
bonus_final = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do KPI para o usuário

print(f"\nCalculo do KPI: {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"\nInformacoes do Usuario\nNome: {nome}\nSalario: {salario}\nBonus: {bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

print("\nOs bugs e riscos é a possibilidade de ValueError vindo do input salario e bonus, não conseguindo transformar em float, caso nao venha um numero.")