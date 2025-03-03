"""
Uno me sorprendio de lo facil jaja supongo era para ver si usaba logica o me iba como cochi a la mier** a buscar combinaciones.... una arreglo de longitud par, con numeros enteros, decir si hay forma de colocar los numeros en parejas de tal forma que todas las sumas de parejas den impar
"""

arr = [1, 2, 1, 2,3,3]

# pair + impair = impair
# you could use a stack
# 2 + 1 = 3


def es_par(num: int) -> bool:
    return num % 2 == 0


def makePairs(arr) -> list[list[int]]:
    if not es_par(len(arr)):
        return []

    result = []
    pair_shelf = []  # store all pairs
    impair_shelf = []

    for i in range(0, len(arr)):
        if not es_par(arr[i]):
            if pair_shelf:
                result.append([arr[i], pair_shelf.pop()])
            else:
                impair_shelf.append(arr[i])
        if es_par(arr[i]):
            if impair_shelf:
                result.append([arr[i], impair_shelf.pop()])
            else:
                pair_shelf.append(arr[i])
    print(len(arr) * 2)
    return result


res = makePairs(arr)
print(f"The result is: {res}")
