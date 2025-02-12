#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. (usar ELIF)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Subtração")
print("2 - Divisão")
print("3 - Soma")
print("4 - Multiplicação")

operacao = int(input("Digite o número da operação desejada: "))

if operacao == 1:
        print("Resultado:", num1 - num2)
        print("Gustavo Wendt")
elif operacao == 2:
        if num2 != 0:
            print("Resultado:", num1 / num2)
            print("Gustavo Wendt")
        else:
            print("Erro: divisão por zero não é permitida!")
            print("Gustavo Wendt")
elif operacao == 3:
        print("Resultado:", num1 + num2)
        print("Gustavo Wendt")
elif operacao == 4:
        print("Resultado:", num1 * num2)
        print("Gustavo Wendt")
else:
        print("Opção inválida! Escolha um número entre 1 e 4.")
        print("Gustavo Wendt")

    

    