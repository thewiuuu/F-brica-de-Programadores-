# Solicitando os Dados 
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

# Acessando o arquivo e gravando os dados do usuário
with open("09.2-pessoas.txt", "a",encoding="utf-8") as arquivo:
    arquivo.write(nome + " | " + email + "\n")