# Lista para armazenar os itens
item1 = str(input())
item2 = str(input())
item3 = str(input())

itens = []
itens.append(item1)
itens.append(item2)
itens.append(item3)
#TODO: Solicite os itens ao usuário


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")