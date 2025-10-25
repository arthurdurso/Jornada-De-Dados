# Refatorar nosso código usando Dicionário, Type Hint e Funcões.

from typing import Dict

def validar_nome() -> str:
    while True:
        try:
            nome: str = input("Digite seu nome: ")

            # Verifica se o nome está vazio
            if not nome.strip():
                raise ValueError("O nome não pode estar vazio.")
            
            # Verifica se o nome contém números
            if any(char.isdigit() for char in nome):
                raise ValueError("O nome não pode conter números.")
            
            # Verifica se o nome contém caracteres especiais (exceto espaço)
            caracteres_especiais: str = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\"
            if any(char in caracteres_especiais for char in nome):
                raise ValueError("O nome não pode conter caracteres especiais.")
            
            # Verifica se o nome é muito curto
            if len(nome.strip()) < 2:
                raise ValueError("O nome é muito curto. Deve ter pelo menos 2 caracteres.")
            
            # Verifica se o nome é muito longo
            if len(nome.strip()) > 50:
                raise ValueError("O nome é muito longo. Deve ter no máximo 50 caracteres.")
            
            return nome.strip()

        except ValueError as e:
            print(e)
            print("Tente novamente.")


def validar_valor(tipo: str) -> float:
    while True:
        try:
            valor_input: str = input(f"Digite o valor do seu {tipo}: ")

            # Verifica se a entrada está vazia
            if not valor_input.strip():
                raise ValueError(f"A entrada para {tipo} não pode estar vazia. Por favor, digite um número.")

            # Substitui vírgulas por pontos (caso o usuário use vírgula como separador decimal)
            valor_input = valor_input.replace(',', '.')

            # Converte a entrada para float
            valor: float = float(valor_input)

            # Verifica se o valor é negativo
            if valor < 0:
                raise ValueError(f"O valor do {tipo} não pode ser negativo.")

            # Verifica se o valor é zero ou muito pequeno
            if valor == 0:
                raise ValueError(f"O valor do {tipo} deve ser maior que zero.")
            
            return valor

        except ValueError as e:
            print(e)
            print("Tente novamente.")


# Início do programa principal
def main() -> None:
    # Armazenando os dados do usuário em um dicionário
    usuario: Dict[str, float | str] = {}

    # Valida o nome do usuário
    usuario["nome"] = validar_nome()

    # Valida o salário
    usuario["salario"] = validar_valor("salário")

    # Valida o bônus
    usuario["bonus"] = validar_valor("bônus")

    # Cálculo do bônus final
    CONSTANTE_BONUS: int = 1000
    bonus_final: float = CONSTANTE_BONUS + usuario["salario"] * usuario["bonus"]

    # Exibe o resultado final
    print(f"\nCálculo do KPI: {bonus_final}")
    print(f"\nInformações do Usuário\nNome: {usuario['nome']}\nSalário: {usuario['salario']}\nBônus: {usuario['bonus']}")


if __name__ == "__main__":
    main()
