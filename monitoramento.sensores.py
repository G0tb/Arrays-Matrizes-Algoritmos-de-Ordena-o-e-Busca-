import random

NUM_SENSORES = 5
NUM_HORAS = 24

sensores = []
mediaSensor = []
somaGeral = 0.0

print("Entrada de dados")

for i in range(NUM_SENSORES):
    somaSensor = 0.0
    temperaturas = []

    for j in range(NUM_HORAS):
        valor = round(random.uniform(0.0, 40.0), 2)
        print(f"Sensor {i} - Hora {j:02d}: {valor}") 
        temperaturas.append(valor)
        somaSensor += valor

    sensores.append(temperaturas)
    mediaSensor.append(somaSensor / NUM_HORAS)
    somaGeral += somaSensor

print("\nMedia de cada sensor")

for i in range(NUM_SENSORES):
    print(f"Sensor {i}: media = {mediaSensor[i]:.2f}")

maior = sensores[0][0]
sensorMaior = 0
horaMaior = 0

for i in range(NUM_SENSORES):
    for j in range(NUM_HORAS):
        if sensores[i][j] > maior:
            maior = sensores[i][j]
            sensorMaior = i
            horaMaior = j

print("\nMaior temperatura registrada")
print(f"Valor: {maior:.2f}")
print(f"Sensor responsavel: {sensorMaior}")
print(f"Horario da ocorrencia: {horaMaior:02d}h")

mediaGeral = somaGeral / (NUM_SENSORES * NUM_HORAS)

print("\nMedia geral")
print(f"Media de todas as 120 medicoes: {mediaGeral:.2f}")
