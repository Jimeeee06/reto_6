"""
RETO 1: PUNTO 2
Realice una función que permita validar si una palabra es un palíndromo.
Condición: No se vale hacer slicing para invertir la palabra y verificar que
sea igual a la original.
Excepción: Debe arrojar un error si la palabra contiene caracteres que no
sean letras o números.
"""
#se comparan los caracteres desde los extremos hacia el centro, si no es igual
# se retorna False, si todos son iguales se retorna True
def palindromo(word: str) -> bool:        
    #Verificamos si la palabra NO es solo letras Y TAMPOCO es solo números.
    if not (word.isalpha() or word.isdigit()):
        raise ValueError("Error: La entrada debe contener únicamente letras o"
        "únicamente números, sin mezclar ni usar símbolos.")

    length = len(word)
    #Compara los caracteres desde los extremos
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False
    return True

def main():
    try:
        word = str(input())
        if palindromo(word):
            print("Es palíndromo")
        else:
            print("No es palíndromo")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()