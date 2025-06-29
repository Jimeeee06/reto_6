"""
RETO 1: PUNTO 3
Escribir una función que reciba una lista de números y devuelva solo aquellos
que son primos. La función debe recibir una lista de enteros y retornar solo
aquellos que sean primos.
"""
#verifica si un número es primo, si es menor o igual a 1 no es primo
#si es mayor a 1 verifica si es divisible por algún número entre 2 y
# la raíz cuadrada de n


def primo(n: int) -> bool:
    if n <= 1:
        return False
    # La siguiente línea puede lanzar un ValueError si n es negativo.
    # Este error será capturado en la función main.
    for i in range(2, int(abs(n)**0.5) + 1):
        #si n es divisible por alguno de ellos, no es primo
        if n % i == 0:
            return False
    return True

def main():
    try:
        # La siguiente línea puede lanzar un ValueError si la entrada no es numérica.
        lista_inicial = list(map(int, input().split()))
        primos = []
        #verifica si cada número es primo, si lo es lo agrega a la lista de primos
        for n in lista_inicial:
            if primo(n):
                primos.append(n)
        print(primos)

    except ValueError:
    # Captura el error de conversión de texto a número, o el de raíz cuadrada de un negativo.
        print("Error: Por favor, ingrese únicamente números enteros "
        "separados por espacios.")
        
    except Exception as error:
        #Captura cualquier otro error inesperado.
        print(f"Error inesperado: {error}")

if __name__ == "__main__":
    main()