# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if altura <= 0: 
        print("Error: La altura debe ser un entero positivo")
        return

    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    for i in range(altura, 0, -1):
        espacios = altura - i
        print(" " * espacios + "*" * (2 * i - 1))

    for i in range(2, altura + 1):
        espacios = altura - i
        print(" " * espacios + "*" * (2 * i - 1))


    
