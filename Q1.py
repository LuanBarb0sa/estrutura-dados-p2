nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    print(f'Reprovado! Sua média é {media:.2f}')
elif media <= 9:
    print(f'Aprovado! Sua média é {media:.2f}')
else:
    print(f'Aprovado com distinção')