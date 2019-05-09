import math  ##importa o módulo math para ser possivel fazer as operações necessárias

resultadoBinario = '' ##define a variável do resultado vazia no começo do código
x = float(input('Digite um número para ser convertido em binário: ')) ##pede ao usuário que informe um válor a ser convertido
num = x ##cria a variável "num" para o número escrito pelo usuário
while x > 0:                                           
  if (x % 2) == 0: 
    x = x / 2   
    resultadoBinario = '0' + str(resultadoBinario) ##o if e else determinam se o número é 0 ou 1, o primeiro if calcula o resto da
  else:                                            ##divisão, verifica se o número é igual a 0 e o adiciona ao resultado o else faz
    x = x / 2                                      ##a mesma coisa so que sem verificar o resto da divisão adicionando 1 ao resultado
    x = math.floor(x)                              ##e o while repete a função até que a quantidade de caracteres do número seja
    resultadoBinario = '1' + str(resultadoBinario) ##convertida em binário.
    
resultadoBinario = str(str('O número ' + str(num)) + ' convertido para binario é: ') + str(resultadoBinario) ##mostra na tela o número convertido
print(resultadoBinario)
