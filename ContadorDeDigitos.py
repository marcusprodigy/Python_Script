num = int(input("Digite um número inteiro: "))

# Inicializa os dois primeiros números da série
fib1, fib2 = 0, 1
cont = 0

# Imprime os dois primeiros números da série
if num == 0:
    print(fib1)
elif num == 1:
    print(fib2)
else:
    print(fib1)
    print(fib2)

    # Calcula os próximos números da série
    while cont < num - 2:
        fib3 = fib1 + fib2
        print(fib3)
        fib1 = fib2
        fib2 = fib3
        cont += 1
