# Almacenar en una lista 15 números e imprimir cuantos son ceros, negativos, positivos, además imprimir la suma de números positivos y suma de números negativos.

print("========== Lista de 15 Numeros =========\n")

numsNeg = []
numsPos = []
numsCero = []

cantNeg = 0
cantPos = 0
cantCero = 0

sumNeg = 0
sumPos = 0

for i in range (15):
    num = int(input(f"Digite el Numero {i+1}:"))
    if num < 0:
        numsNeg.append(num)
        cantNeg = len(numsNeg)
        sumNeg = sum(numsNeg)
    elif num == 0:
        numsCero.append(num)
        cantCero = len(numsCero)
    else:
        numsPos.append(num)
        cantPos = len(numsPos)
        sumPos = sum(numsPos)

print(f"\n1. Numeros Positivos: \n- Cantidad: {cantPos} \n- Suma de Numeros Positivos: {sumPos}")
print(f"\n2. Numeros Negativos: \n- Cantidad: {cantNeg} \n- Suma de Numeros Negativos: {sumNeg}")
print(f"\n3. Numeros Cero: \n- Cantidad: {cantCero}")
print("\n========================================")