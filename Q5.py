numeroDigitado = int(input('Digite um número: '))

primos = []

for i in range(numeroDigitado + 1):
    if i % 2 == 1 and i != 2:
        primos.append(i)

print(f'Os números primos são: {primos}')