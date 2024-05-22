
lista = []

for n in range(1,10):
    lista.append([f'E{n}', n])
    
for n in range(20,30):
    lista.append([f'E{n}', n])
    
    
for n in range(50,60):
    lista.append([f'E{n}', n])
    
for n in range(10,20):
    lista.append([f'E{n}', n])
    
    
# print(lista)

longitud = len(lista)
lista_nueva = [0]*(longitud)

for a in range(len(lista)):
    for b in range(len(lista)):
        if lista[a][1] > lista[b][1]:
            menor = lista[b]
            mayor = lista[a]
            lista[a] = menor
            lista[b] = mayor
print(lista)