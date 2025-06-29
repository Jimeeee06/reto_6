"""
RETO 1: PUNTO 4
Escribir una función que reciba una lista de números enteros y retorne la mayor
suma entre dos elementos consecutivos.
"""

def max_suma(numeros: list) -> int:
    sumas = []
    #itera sobre la lista de números y suma cada par de elementos consecutivos
    #la conversión int() puede arrojar ValueError si un elemento no es numérico.
    for i in range(0, len(numeros)-1):
        suma = int(numeros[i]) + int(numeros[i+1])
        sumas.append(suma)
    
    #La función max() puede arrojar ValueError si la lista 'sumas' está vacía.
    #Esto sucede si la lista original tiene menos de 2 elementos.
    return(max(sumas))

def main():
    try:
        #convierte la lista de números en enteros
        numeros = list(input().split())
        print(max_suma(numeros))

    except ValueError:
    #Captura el error de conversión a int() o el de llamar a max() en una lista vacía.
        print("Error: Ingrese al menos dos números enteros válidos separados "
        "por espacios.")
    
if __name__ == "__main__":
    main()