#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
chuva=input("Está chovendo?(sim/nao) ")
if chuva=='sim'.lower():
   vento = input("Está ventando?: ").lower()

if vento =='sim':
   print("Está ventando demais para usar um guarda-chuva")
   print("Gustavo Wendt")
   if vento == 'nao':
      print("Pegue um guarda-chuiva")
      print("Gustavo Wendt")
   else:
      print("aproveite o seu dia")
      print("Gustavo Wendt")