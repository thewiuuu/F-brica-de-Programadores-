# Variaveis
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é sua idade? "))

# Condição

if idade >= 18:

    carteira = input("Possui carteira de motorista \n (1-Sim / 2-Não)")

    if carteira == "1":
        print("Pode dirigir")      

else:
    print("Não pode Dirigir")
    
