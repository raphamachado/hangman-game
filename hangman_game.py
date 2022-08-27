#jogo da forca
def jogar():
  print('*********************************')
  print('***Bem-vindo ao jogo da forca!***')
  print('*********************************')

  palavra_secreta='banana'
  letras_acertadas=['_','_','_','_','_','_']

  acertou=False
  enforcou=False
  erros=0

  tentativas=5

  print(letras_acertadas)
  while(not acertou and not enforcou):
    chute=input('Digite uma letra')
    if (chute in palavra_secreta):
      posicao = 0
      for letra in palavra_secreta:
        if (chute.upper()==letra.upper()):
          print('Acertou! Encontrei a letra {} na posição {}'.format(letra,posicao))
          letras_acertadas[posicao]=letra
        posicao+=1
    else:
      erros+=1

    acertou="_" not in letras_acertadas
    enforcou=erros==tentativas
    print(letras_acertadas)


  if (acertou):
    print('Você ganhou')
  else:
    print('Você perdeu')

  print('Fim do jogo')

jogar()