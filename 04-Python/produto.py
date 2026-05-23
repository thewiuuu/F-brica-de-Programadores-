# Variaveis e Usuario

nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

#Calculos

valor_desconto = preco * desconto / 100
valor_final = preco - valor_desconto 

# Apresentando
print("-----------------------------------------------------------------")
print(f"| Produto: {nome_produto} | \n| Valor final: R$ {valor_final} |" )
print("-----------------------------------------------------------------")

