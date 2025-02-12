#Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
Kh=int(input("Qual a velocidade que você passou com o seu carro?: "))
if Kh >80:
     custo=Kh - 80
     multa=custo*5
     print("Você ultrapaçou o limite de velocidade em",custo,"Km/h e recebeu uma multa de; R$",multa)
     print("Gustavo Wendt")
else:
  print("Está dentro do limite de velocidade")
  print("Gustavo Wendt")