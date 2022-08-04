#Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
#- ValueError: se o usuário digitar um caracter
#- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
#- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
#- KeyboardInterrupt: caso o usuário interrompa a execução

#Mostre uma mensagem personalizada na ocorrência de cada um desses erros

from time import sleep
empty_list = []

while True:
  try:
    value_1 = float(input("Enter a number:"))
    value_2 = float(input("Enter another number:"))
  except ValueError:
    print("Please numbers only.")
  except ZeroDivisionError:
    print("Zero Division is impossible.")
  except IndexError:
    print("Only 0 and 1 index")
  except KeyboardInterrupt:
    print("User interrupted program execution, aborting.")
    break
  else:
    empty_list.insert(0, value_1)
    empty_list.insert(1, value_2)

    division = value_1 / value_2

    print("Calculating...")
    sleep(2)
    print(empty_list)
    print(division)
    break



