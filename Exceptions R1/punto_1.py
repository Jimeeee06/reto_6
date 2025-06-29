"""
RETO 1: PUNTO 1
Crear una función que realice operaciones básicas (suma, resta, multiplicación,
división) entre dos números,según la elección del usuario, la forma de entrada
de la función será los dos operandos y el caracter usado para la operación.
"""

def suma(a: int, b: int) -> int:
    return a + b
def resta(a: int, b: int) -> int:
    return a - b
def multiplicacion(a: int, b: int) -> int:
    return a * b
def division(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def main():
    try:
        operacion=str(input())
# Se espera que la entrada sea del tipo "número espacio número espacio operador"
        a = int(operacion.split()[0])
        b = int(operacion.split()[1])
        c = operacion.split()[2]
        
        operaciones = {"+": suma, "-": resta, "*": multiplicacion, "/": division}

        for key in operaciones:
            resultado: int = operaciones[c](a, b)
        
        print(resultado)

    except ValueError:
        #Captura errores de conversión a int (ej. "a" + 3)
        print("Error: Verifique que los dos primeros valores sean "
        "números enteros.")
    
    except IndexError:
        #Captura errores si el usuario no ingresa los 3 componentes.
        print("Error: Formato de entrada incorrecto. (Número número operador).")

    except KeyError:
        #Captura errores si el operador no es válido.
        print("Error: Operador no válido. Use '+', '-', '*' o '/'.")
    
    except Exception as error:
        #Excepción para cualquier otro error no previsto.
        print(f"Ha ocurrido un error inesperado: {error}")


if __name__ == "__main__":
    main()