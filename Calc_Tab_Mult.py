num = int(input("Digite um número inteiro positivo: "))
contador = 0

while num >= 1:
    contador += 1
    num /= 10

print("O número tem", contador, "dígito(s).")
