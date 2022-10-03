idade = []
altura = []

i = 0

while i < 5:
    idadeDigitada = int(input('Digite a sua idade: '))
    alturaDigitada = float(input('Digite a sua altura: '))
    idade.append(idadeDigitada)
    altura.append(alturaDigitada)
    i = i + 1

print(f'As idades na ordem que foram lidas são: {idade[0]}, {idade[1]}, {idade[2]}, {idade[3]}, {idade[4]}')
print(idade)
print('')
idadeInverso = list(reversed(idade))
print(f'As idades na ordem inversa são: {idadeInverso[0]}, {idadeInverso[1]}, {idadeInverso[2]}, {idadeInverso[3]}, {idadeInverso[4]}')
print(idadeInverso)

print('')
print('')

print(f'As alturas na ordem que foram lidas são: {altura[0]}, {altura[1]}, {altura[2]}, {altura[3]}, {altura[4]}')
print(altura)
print('')
alturaInverso = list(reversed(altura))
print(f'As idades na ordem inversa são: {alturaInverso[0]}, {alturaInverso[1]}, {alturaInverso[2]}, {alturaInverso[3]}, {alturaInverso[4]}')
print(alturaInverso)