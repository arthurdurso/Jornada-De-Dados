# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("\nDigite o valor do seu salario: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("\nDigite o valor do seu bonus: "))

# 4) Calcule o valor do bônus final
CONSTANTE_BONUS = 1000
bonus_final = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(f"\nCalculo do KPI: {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"\nInformacoes do Usuario\nNome: {nome}\nSalario: {salario}\nBonus: {bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
print("\nOs bugs e riscos é a possibilidade de ValueError vindo do input salario e bonus, não conseguindo transformar em float, caso nao venha um numero.")