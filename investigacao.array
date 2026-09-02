temperatura = []
soma = 0.0
media = 0.0
operacoes = 0

print("Entrada de dados")

for i in range(10):
    valor = float(input(f"Digite a temperatura do indice {i}: "))
    temperatura.append(valor)
    soma += temperatura[i]

operacoes += 1

print("\nTemperaturas armazenadas")
print("Indice:      ", end="")

for i in range(10):
    print(f"{i:5}", end=" ")

print("\nTemperatura: ", end="")

for i in range(10):
    print(f"{temperatura[i]:5.1f}", end=" ")

print()

operacoes += 1

media = soma / 10

print(f"\nMedia das temperaturas: {media:.2f}")

maior = temperatura[0]
menor = temperatura[0]

idxMaior = 0
idxMenor = 0

for i in range(1, 10):
    if temperatura[i] > maior:
        maior = temperatura[i]
        idxMaior = i

    if temperatura[i] < menor:
        menor = temperatura[i]
        idxMenor = i

operacoes += 1

print(f"Maior temperatura: {maior:.2f} (indice {idxMaior})")
print(f"Menor temperatura: {menor:.2f} (indice {idxMenor})")

acimaMedia = 0

for i in range(10):
    if temperatura[i] > media:
        acimaMedia += 1

operacoes += 1

print(f"Quantidade de valores acima da media: {acimaMedia}")
print(f"\nNumero aproximado de passadas pelo array: {operacoes}")
