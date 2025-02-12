#- Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
salario=float(input("Digite a sua renda mensal: "))
if salario <  2259.21:
 print("Você está isento!")
 print("Gustavo Wendt")
elif salario >=  2259.21 and salario <=2826.65:
    imposto=0.075*salario
    print("Você terá que pagar: ", imposto,"de imposto!")
    print("Gustavo Wendt")
elif salario >= 2826.66 and salario <=3751.05:
   imposto=salario*0.15
   print("Você terá que pagar: ", imposto,"de imposto!")
   print("Gustavo Wendt")
elif salario >= 3751.06 and salario<= 4664.68:
   imposto=salario*0.225
   print("Você terá que pagar: ", imposto,"de imposto!")
   print("Gustavo Wendt")
elif salario >=4664.68:
   imposto= salario*0.275
   print("Você terá que pagar: ", imposto,"de imposto!")
   print("Gustavo Wendt")