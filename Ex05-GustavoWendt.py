#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
sechuva=input("Está chovendo?(sim/nao) ")
sechuva02=sechuva.lower()
if sechuva == 'sim':
  resposta=input("Está ventando muito?(sim/nao)")
else:
  print("Então aproveite o seu dia!")
  if resposta == sim:
    print("Está ventando muito para usar um guarda-chuvas!")
  else:
    print("Então pegue um guarda-chuvas!")
