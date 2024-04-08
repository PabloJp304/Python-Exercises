def crear_matriz(x: int, z: int, M: int, N: int) -> list[int]:
    """
    Crea una matriz llena de ceros y coloca la letra 'P' en la 
    posición especificada.

    Args:
        x (int): La posición en la dimensión x donde se colocará la letra 'P'.
        z (int): La posición en la dimensión z donde se colocará la letra 'P'.
        M (int): El tamaño en la dimensión x de la matriz.
        N (int): El tamaño en la dimensión z de la matriz.

    Returns:
        list[list[int]]: Una matriz con ceros en todas las posiciones excepto en 
        la posición (x, z), donde se coloca la letra 'P', se retorna la posición.
    """
    # Crear una matriz llena de ceros
    matriz = [[0 for _ in range(N)] for _ in range(M)] 
    
    # Colocar la letra 'P' en la posición especificada
    matriz[x][z] = 'P'
    
    return [matriz,x,z]

def solicitar_valores_iniciales() -> list[int]:
    """
    Solicita al usuario los valores iniciales para crear una matriz y 
    colocar la letra 'P' en una posición específica.

    Returns:
        list[int]: Una lista que contiene los valores de la fila inicial, 
        la columna inicial, el ancho y el alto de la matriz.
    """
    while True: 
        M = int(input("Ingresa el ancho de la matriz: "))
        if M > 0:
            break
        else:
            print("No puedes ingresar números menores de 0 para el ancho de la matriz. ¡Inténtalo de nuevo!")

    while True: 
        N = int(input("Ingresa el alto de la matriz: "))
        if N > 0:
            break
        else:
            print("No puedes ingresar números menores de 0 para el alto de la matriz. ¡Inténtalo de nuevo!")

    while True:
        x = int(input("Ingresa la fila inicial de la letra P: "))
        if M > x >= 0:
            break
        else:
            print(f"El valor de la fila debe estar entre 0 y {M-1}")

    while True:
        z = int(input("Ingresa la columna inicial de la letra P: "))
        if N > z >= 0:
            break
        else:
            print(f"El valor de la columna debe estar entre 0 y {N-1}")    

    return [x, z, M, N]

def movimiento(valor: int, x: int, z: int, matriz: list[list[int]]) -> list[int]:
    """
    Realiza un movimiento en la matriz, desplazando la letra 'P' en 
    diagonal hacia abajo a la derecha.

    Args:
        valor (int): El valor de desplazamiento.
        x (int): La fila actual de la letra 'P'.
        z (int): La columna actual de la letra 'P'.
        matriz (list[list[int]]): La matriz en la que se realizará el movimiento.

    Returns:
        list[int]: Una lista que contiene las nuevas coordenadas de la letra 'P' (x, z) 
        y la matriz actualizada.
    """
    if 0 <= x + valor < len(matriz[0]) and 0 <= z + valor < len(matriz):
        matriz[x][z] = 0
        x += valor
        z += valor
        matriz[x][z] = "P"
    else:
        print("No se puede realizar el movimiento!")
    return [x, z, matriz]

def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Imprime la matriz en la consola.

    Args:
        matriz (list[list[int]]): La matriz que se va a imprimir.
    """
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")
        print()

def main() -> None:
    """
    Función principal del programa. Crea una matriz, solicita valores iniciales al usuario, 
    realiza movimientos y muestra la matriz resultante en cada paso.
    """
    valores = [1, -1, 2, 3, -1, 2, 1, 0]

    # Crear la matriz y obtener las coordenadas iniciales
    matriz, x, z = crear_matriz(*solicitar_valores_iniciales())
    
    # Imprimir la matriz inicial
    print("\nMATRIZ INICIAL")
    imprimir_matriz(matriz)
    print()

    # Realizar movimientos con los valores proporcionados
    for valor in valores:
        print(f"Movimiento con valor '{valor}'")
        x, z, matriz = movimiento(valor, x, z, matriz)
        imprimir_matriz(matriz)
        print()

if __name__ == "__main__":
    main()