@RonaldoCapitol
#IMC => PESO (KG) / ALTURA (M)²

peso_user = float(input('Insira seu peso: '))
altura_user = float(input('Insira sua altura: '))

def numero_quadrado(numero):
  quadrado = numero * numero
  
  return quadrado

def calcular_imc(peso_user, altura_user):
  altura_quadradada = numero_quadrado(altura_user)
  meu_imc = peso_user / altura_quadradada
  
  return meu_imc

def classificar_imc(meu_imc):
  if imc < 18.5:
    print('Magreza')
  elif imc >= 18.5 and imc < 25:
    print('Normal')
  elif imc >= 25 and imc < 30:
    print('Sobrepeso')
  elif imc >= 30 and imc < 40:
    print('Obesidade')
  else:
    print('Obesidade Grave')

imc = calcular_imc(peso_user, altura_user)

print('Seu imc é: ', calcular_imc(peso_user, altura_user))
print('Sua classificação é: ')
classificar_imc(imc)