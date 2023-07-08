#bloco try-except-finally

try:
  num1 = 3
  num2 = 0

  response = num1/num2

  print(response)

except ZeroDivisionError: #tratamento específico
  print("Erro de divisão de zero!!!!")

except Exception as exception: #tratamento geral
  print(exception)
  print(isinstance(exception, ZeroDivisionError))

finally:
  print("Venha para cá independentemente")