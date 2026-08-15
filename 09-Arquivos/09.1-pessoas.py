# Solicitando os Dados 
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

# Acessando o arquivo e gravando os dados do usuário
arquivo = open("09.1-pessoas.txt","a", encoding="utf-8")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()