nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial: ", nomes)

# Adcionando Elementos
nomes.append("Carlos") # Adciona ao final da lista
print("Após o append", nomes)

nomes.insert(1,"Fernanda") # Insere Fernanda no indice 1 
print("Após Insert ", nomes)

# Modificando Elementos ]
nomes[2] = "Paulo" # Modifica o elemento no indice 2 
print("Após Modificação", nomes)

# Removendo Elementos 
del nomes[3] # Remove o elemento de indice 3 
print("Após del ", nomes)

nomes.remove("Paulo")
print("Após remove ", nomes)

removido = nomes.pop(2) # Removee e retorna o elemento do indice 2 
print(f"Após pop (removido {removido})", nomes)

