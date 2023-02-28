string = "exemplo"

lista = list(string)

inicio = 0
fim = len(lista) - 1


while fim > inicio:
  
    temp = lista[inicio]
    lista[inicio] = lista[fim]
    lista[fim] = temp
    
   
    inicio += 1
    fim -= 1


string_invertida = "".join(lista)


print(string_invertida)
