var = str(input("Informe o numero: "))
var = var.split(".")
numeros_int = list(map(int, var))

print(numeros_int)

binario = [[],[],[],[]]
cont = 3

while cont >= 0:
    num = numeros_int[cont]
    for i in range(8):
        binario[cont].append(num % 2)
        num //= 2
    cont -= 1

binario[0].reverse()
binario[1].reverse()
binario[2].reverse()
binario[3].reverse()

print(binario)
