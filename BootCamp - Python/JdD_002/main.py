# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
def programa01():
    num1 = int(input("Qual o primeiro numero? "))
    num2 = int(input("Qual o segundo numero? "))
    return num1 + num2
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
def programa02():
    num = int(input("Digite um numero: "))
    return num % 5
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
def programa03():
    num1 = int(input("Qual o primeiro numero? "))
    num2 = int(input("Qual o segundo numero? "))
    return num1 * num2
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
def programa04():
    num1 = int(input("Digite um numero inteiro: "))  
    num2 = int(input("Digite um numero: "))  
    return num1 // num2
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
def programa05():
    num = int(input("Digite um numero: "))
    return num ** 2

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
def programa06():
    num1 = float(input("Qual o primeiro numero float? "))
    num2 = float(input("Qual o segundo numero float? "))
    return num1 + num2
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def programa07():
    num1 = float(input("Qual o primeiro numero float? "))
    num2 = float(input("Qual o segundo numero float? "))
    return (num1 + num2) / 2
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def programa08():
    num1 = int(input("Qual o base? "))
    num2 = int(input("Qual o expoente? "))
    return num1 ** num2
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
def programa09():
    Cel = int(input("Qual a temperatura em Celsius? "))
    Fah = Cel * 9 / 5 + 32
    return Fah
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
def programa10():
    raio = int(input("Qual o raio do circulo? "))
    pi = 3.14
    area_circ = pi * (raio ** 2)
    return area_circ
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def programa11():
    user_input = input("Digite uma frase: ")
    return user_input.upper()
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def programa12():
    user_input = input("Digite seu nome completo: ")
    return print(user_input.lower())
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def programa13():
    user_input = input("Digite uma frase: ")
    return print(user_input.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
def programa14():
    user_input = input('Digite uma data no formato "dd/mm/aaaa": ')
    return print(user_input.split("/"))
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
def programa15():
    user_input1 = input("Digite a primeira frase: ")
    user_input2 = input("Digite a segunda frase: ")
    return user_input1 + user_input2

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def programa16():
    user_input1 = input("Digite a primeira expressão booleana (True ou False): ")
    user_input2 = input("Digite a segunda expressão booleana (True ou False): ")

    result = user_input1 and user_input2
    return result

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def programa17():
    user_input1 = input("Digite a primeira expressão booleana (True ou False): ")
    user_input2 = input("Digite a segunda expressão booleana (True ou False): ")

    result = user_input1 or user_input2
    return result
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def programa18():
    user_input1 = input("Digite a primeira expressão booleana (True ou False): ")

    result = not user_input1
    return result
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
def programa19():
    user_input1 = input("Digite a primeira expressão booleana (True ou False): ")
    user_input2 = input("Digite a segunda expressão booleana (True ou False): ")

    result = user_input1 == user_input2
    return result
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def programa20():
    user_input1 = input("Digite a primeira expressão booleana (True ou False): ")
    user_input2 = input("Digite a segunda expressão booleana (True ou False): ")

    result = user_input1 != user_input2
    return result


# 21: Conversor de Temperatura
def conv_temp():
    try:
        Cel = int(input("Qual a temperatura em Celsius? "))
        Fah = Cel * 9 / 5 + 32
        return Fah
    except ValueError:
        print("A entrada nao foi valida.")

# 22: Verificador de Palíndromo
def verif_palind():
    try:
        user_input = input("Digite uma frase para verificar se e um palindromo: ")
        if isinstance (user_input, str):
            user_input = user_input.replace(" ","").lower()
            user_input_inv = user_input[::-1]
        if user_input == user_input_inv:
            return print("A frase e um palindromo!")
    except ValueError:
        print("Digite uma frase válida.")

# 23: Calculadora Simples
def calculadora():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        op   = input("Digite o operador (+, -, *, /): ")
    
        if op == "+":
            return print(num1 + num2)
        elif op == "-":
            return print(num1 - num2)
        elif op == "*":
            return print(num1 * num2)
        elif op == "/":
            return print(num1 / num2)
        else:
            print("Operador invalido.")

    except ZeroDivisionError:
        print("Nao e possivel dividir por zero.")
    except ValueError:
        print("Digite um número inteiro válido.")

# 24: Classificador de Números
def class_num():
    try:
        num1 = int(input("Digite um número: "))
        
        if   num1 > 0:
            print("O numero e positivo.")
        elif num1 < 0:
            print("O numero e negativo.")
        elif num1 == 0:
            print("O numero e zero.")

        elif num1 % 2 == 0:
            print("O numero e par.")
        elif num1 % 2 == 1:
            print("O numero e impar.")

    except ValueError:
        print("Digite um número inteiro válido.")
    
# 25: Conversão de Tipo com Validação
def conversor_tipo():
    user_input = input("Digite uma serie de numeros separados por virgula: ")
    num_list_str = user_input.split(",")
    num_list_int = []

    try:
        for num in num_list_int:
            num_list_int.append(int(num.strip()))
        print(num_list_int)
    except ValueError:
        print("Digite numeros inteiros validos na serie de numeros.")