"""
RETO 1: PUNTO 5
Escribir una función que reciba una lista de string y retorne unicamente
aquellos elementos que tengan los mismos caracteres.
"""
def mismos_caracteres(lista: list) -> list:
    iguales = {}

    #*Iteramos para validar que todos los elementos sean de tipo string.
    for item in lista:
        if not isinstance(item, str):
            #Si un elemento no es string, lanzamos un TypeError.
            raise TypeError(f"Error: La lista solo puede contener strings."
                        "Se encontró un elemento de tipo '{type(item).__name__}'.")

    #*para cada elemento de la lista, ordena los caracteres y los usa como clave
    for i in lista:
        key = "".join(sorted(i))
        #*si la clave ya existe, agrega el elemento a la lista de valores
        if key in iguales:
            iguales[key].append(i)
        #*si no existe, crea una nueva entrada en el diccionario
        else:
            iguales[key] = [i]
            
    #*filtra los grupos que tienen más de un elemento
    resultado = [palabra for grupo in iguales.values()
                 if len(grupo) > 1 for palabra in grupo]
    return resultado

def main():
    try:
        lista = list(input().split(","))
        resultado = mismos_caracteres(lista)
        print(resultado)
    
    except TypeError as error:
        # Capturamos el error de tipo y mostramos el mensaje personalizado.
        print(error)

if __name__ == "__main__":
    main()