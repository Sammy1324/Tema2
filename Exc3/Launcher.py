def nums_magic(lista):
    # Eliminar duplicados
    list_without_duplicates = list(set(lista))
    
    # Ordenar de mayor a menor
    organised_list = sorted(list_without_duplicates, reverse=True)
    
    # Eliminar números impares
    list_of_pairs = [num for num in organised_list if num % 2 == 0]
    
    # Sumar los números restantes
    addition = sum(list_of_pairs)
    
    # Colocar la suma como el primer elemento
    result = [addition] + list_of_pairs
    
    # Verificar la condición
    if addition == sum(result[1:]):
        print("La suma de los elementos a partir del segundo es igual al primer elemento.")
    else:
        print("La suma de los elementos a partir del segundo no es igual al primer elemento.")
    
    return result