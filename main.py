import funcoes_sql

# Função convert_number (assumida da imagem)
def conversao(number, from_base, to_base):
    # Converter número de entrada para decimal primeiro
    try:
        decimal = int(str(number), from_base)
    except ValueError:
        return "Entrada inválida para a base especificada"
    
    # Converter decimal para a base desejada
    if to_base == 2:
        return bin(decimal)[2:]  # Remove prefixo '0b'
    elif to_base == 8:
        return oct(decimal)[2:]  # Remove prefixo '0o'
    elif to_base == 10:
        return str(decimal)
    elif to_base == 16:
        return hex(decimal)[2:].upper()  # Remove prefixo '0x' e usa maiúsculas
    else:
        return "Base de destino não suportada"

# Função receber_numeros
def receber_numeros():
    try:
        number = input("Digite o número a ser convertido: ")
        from_base = int(input("Digite a base de origem (2, 8, 10, 16): "))
        to_base = int(input("Digite a base de destino (2, 8, 10, 16): "))
        
        if from_base not in [2, 8, 10, 16] or to_base not in [2, 8, 10, 16]:
            raise ValueError("As bases suportadas são apenas 2, 8, 10 ou 16.")
        
        result = conversao(number, from_base, to_base)
        return number, from_base, to_base, result
    
    except ValueError as e:
        raise ValueError("Por favor, insira entradas válidas.")

# Função main
def main():
    funcoes_sql.criar_tabela()  # Garante que a tabela exista antes de qualquer operação
    
    while True:
        print("\n=== Menu Conversor de Bases ===")
        print("1. Converter um número")
        print("2. Listar todas as operações realizadas")
        print("3. Sair")
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == "1":
            try:
                number, from_base, to_base, result = receber_numeros()
                conversao_existente = funcoes_sql.buscar_conversao_existente(number, from_base, to_base)
                if conversao_existente:
                    print(f"Conversão já realizada. Resultado: {conversao_existente}")
                else:
                    print(f"Resultado da conversão: {result}")
                    funcoes_sql.adicionar_conversao(number, from_base, to_base, result)
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
        
        elif escolha == "2":
            conversoes = funcoes_sql.listar_conversoes()
            if conversoes:
                print("\n=== Histórico de Conversões ===")
                for conversao in conversoes:
                    print(f"ID: {conversao[0]}, Número: {conversao[1]}, Origem: {conversao[2]}, Destino: {conversao[3]}, Resultado: {conversao[4]}")
            else:
                print("Nenhum histórico de conversões encontrado.")
        
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            break
        
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()