#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
km=float(input("Digite quantos km deseja percorer: "))
if km <=200:
    preco=km*0.50
    print("O preço da viagem será: ", preco)
    print("Gustavo Wendt")
elif km >200:
    preco=km*0.45
    print("O preço da viagem será: ", preco)
    print("Gustavo Wendt")