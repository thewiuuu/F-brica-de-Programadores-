# definindo as funções de conversão de moeda
def dolar_real(valor_dolar):
    taxa = 5.06
    valor_real = valor_dolar * taxa
    return valor_real 

def real_dolar(valor_real):
    taxa = 5.06
    valor_dolar = valor_real / taxa
    return valor_dolar

# criando menu interativo
def menu():
    while True:
        print("\n=== Conversor de Moedas ===")
        print("1 - Dólar  para Real")
        print("2 - Real para Dólar")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: ")) # lê a opção do usuário

        if opcao == 1:
            valor = float(input("Digite o valor em Dólar $ "))
            resultado = dolar_real(valor)
            print(f"$ {valor} = R$ {resultado:.2f}")

        elif opcao == 2:
            valor = float(input("Digite o valor em Real R$ "))
            resultado = real_dolar(valor)
            print(f"$ {valor} = R$ {resultado:.2f}")

        elif opcao == 0:
            print("Obrigado por usar o Conversor de Moedas!")
            break

        else:
            print("Opção Inválida. Tente novamente.")

# executa o programa
menu()
