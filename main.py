n1 = int(input("n1?"))
n2 = int(input("n2?"))
n3 = int(input("n3?"))

numeros = [n1]
meio = 0
repetido = 0

if n2 not in numeros:
  numeros.append(n2)
else:
  repetido=n2
  
if n3 not in numeros:
  numeros.append(n3)
else:
  repetido=n3

menor = min(numeros)
maior = max(numeros)

if n1==n2==n3:
  print("todos são iguais a "+str(n1))

elif maior==repetido and repetido!=menor:
  print("maiores: {}\nmenor: {}".format(maior,menor))
  print("não há elementos do meio")

elif maior!=repetido and repetido==menor:
  print("maior: {}\nmenores: {}".format(maior,menor))
  print("não há elementos do meio")

elif n1!=n2!=n3:
  print("maior: {}\nmenor: {}".format(maior,menor))
  for n in numeros:
    if n!= maior and n!=menor:
      print("meio: {}".format(n))
