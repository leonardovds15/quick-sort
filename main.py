def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
       
        pivo = lista[-1]
        
        menores = [x for x in lista[:-1] if x <= pivo]
        maiores = [x for x in lista[:-1] if x > pivo]
        
        
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


numeros = [10, 7, 8, 9, 1, 5]
ordenada = quick_sort(numeros)
print(ordenada)

