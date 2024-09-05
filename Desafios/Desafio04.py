quantidade_passos = int(input("Digite a quantidade de passos: "))

while quantidade_passos < 0:
    quantidade_passos = int(input("Quantidade de passos precisa ser positiva, digite novamente:"))

if quantidade_passos == 0:
    print('Nenhum passo dado na floresta')
elif quantidade_passos == 1:
    print("Explorador: 1 passo")
else:
    print("Explorador: 1 passo")
    for i in range (2,quantidade_passos+1):
        print(f"Explorador: {i} passos")
