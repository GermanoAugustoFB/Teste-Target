num = int(input("Digite um número: "))
a = 0
b = 1

while a <num:
    a, b = b, a + b

if a == num:
    print(num, "Pertence a sequência de Fibonacci. ")
else:
     print(num, "NÂO pertence a sequência de Fibonacci. ")   