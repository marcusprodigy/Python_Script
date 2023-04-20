numero = int(input('informe o numero'))
contador = numero
divisor = int
listinha=[]
while contador > 0:
    divisor =  numero % contador
    if divisor == 0:
        listinha.append(contador)
    contador -= 1
if len(listinha) < 3:
    print ("Numero Primo - Seus Divisores - ", listinha)
else:
    print ("Seus divisores")
    print (listinha)