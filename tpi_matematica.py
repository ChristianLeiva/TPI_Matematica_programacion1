# Trabajo Practico Integrador de Matematicas y Programación 1
def decimal_a_binario(num_decimal: str) -> str: 
    # Función para convertir el número en decimal (positivo) a binario
    num_decimal = int(num_decimal)
    restos = []
    if num_decimal == 0: return "0"

    while num_decimal > 0:
        resto = num_decimal % 2
        restos.append(resto)
        num_decimal = num_decimal // 2
    
    # Invertimos la lista para que el binario quede en el orden correcto
    binario_str = ""
    for i in restos[::-1]:
        binario_str += str(i)
    # retornamos el valor en formato string
    return binario_str

def binario_a_decimal(num_binario: str) -> int:
    sumador = 0
    # Invertimos el string para que la posición 0 coincida con 2^0
    binario_invertido = (num_binario)[::-1]
    
    for i in range(len(binario_invertido)):
        if binario_invertido[i] == "1":
            sumador += 2 ** i 
     # Retornamos el número en binario       
    return sumador
        

def validar_numero_entrada(msj : str):
    # Función para validar que el nnúmero ingresado sea valido, no permite ingresar caracteres.
    num = input(msj)
    while not num.isdigit():
        num = input("Error: Caracter Invalido. Intente nuevamente: ")
    return num

def es_binario(cadena_binaria: str) -> bool:
    """Función auxiliar para validar si el string solo tiene 0 y 1"""
    for caracter in cadena_binaria:
        if caracter not in ["0", "1"]:
            return False
    return True


print("*** Bienvenido al Sitio ***")
while True:
    opcion_ingresada = validar_numero_entrada("Menú de opciones:\n1 - Convertir numero decimal a binario.\n2 - Convertir número binario a decimal.\n3 - Operaciones de Lógica Proposional (Tablas de verdad)\n4 - Salir.\n")
    opcion_ingresada = int(opcion_ingresada)
    if opcion_ingresada == 1:
        print("Conversión de número decimal a binario.")
        num_decimal = validar_numero_entrada("Ingrese un número (entero positivo): ")
        num_binario = decimal_a_binario(num_decimal)
        print(f"El número decimal {num_decimal} equivale a {num_binario} en binario.\n")
    elif opcion_ingresada == 2:
        print("Conversión de número binario a decimal.")
        num_binario = validar_numero_entrada("Ingrese un número binario: ")
        if not es_binario(num_binario):
            print("Error: El número ingresado no es un binario válido (solo 0 y 1).")
            continue
        num_decimal=binario_a_decimal(num_binario)
        print(f"El número binario {num_binario} equivale a {num_decimal} en decimal.\n")    
    elif opcion_ingresada == 3:
        print("\n--- Verificador de Condicional Lógica (p -> q) ---")
        print("Ingrese 1 para Verdadero o 0 para Falso")
        
        p = validar_numero_entrada("Valor de p: ")
        p=int(p)
        q = validar_numero_entrada("Valor de q: ")
        q=int(q)
        
        # Validamos que solo metan 0 o 1
        if p in [0, 1] and q in [0, 1]:
            # La lógica de la condicional: es falsa solo si V -> F
            resultado = not (p == 1 and q == 0)
            valor_final = "Verdadero (1)" if resultado else "Falso (0)"
            print(f"La proposición p -> q es: {valor_final}\n")
        else:
            print("Error: Los valores lógicos deben ser 0 o 1.\n")
    elif opcion_ingresada == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Error: Opción invalida. Intente nuevamente ")
        continue
    



        

