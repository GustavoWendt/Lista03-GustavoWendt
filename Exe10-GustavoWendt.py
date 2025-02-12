#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario=float(input("Digite o seu salário mensal: "))
if salario >=1250:
    porcentagem=salario*0.10
    aumento=porcentagem + salario
    print("Seu salário com o aumento é de: ",aumento)
    print("Gustavo Wendt")
elif salario <1250:
      porcentagem=salario*0.15
      aumento=porcentagem + salario
      print("eu salário com o aumento é de: ",aumento)
      print("Gustavo Wendt")