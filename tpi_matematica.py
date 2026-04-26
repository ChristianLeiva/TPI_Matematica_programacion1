# Trabajo Practico Integrador de Matematicas y Programación 1

def decimal_a_binario(num_decimal: str) -> str:
    """
    Convierte un número decimal positivo a su representación en binario.
    
    Parámetros:
        num_decimal (str): Número decimal en formato string (ej: "10").
    
    Retorna:
        str: Representación binaria del número (ej: "1010").
    """
    num_decimal = int(num_decimal)  # Convertimos el string a entero para operar
    restos = []  # Lista donde guardamos los restos de cada división por 2

    # Caso especial: el binario de 0 es "0"
    if num_decimal == 0:
        return "0"

    # Algoritmo de división sucesiva por 2:
    # En cada iteración guardamos el resto (0 o 1) y dividimos el número por 2
    while num_decimal > 0:
        resto = num_decimal % 2
        restos.append(resto)
        num_decimal = num_decimal // 2

    # Los restos se obtienen de menor a mayor peso, así que los invertimos
    # para armar el número binario en el orden correcto (de mayor a menor peso)
    binario_str = ""
    for i in restos[::-1]:
        binario_str += str(i)

    return binario_str  # Retornamos el número binario como string


def binario_a_decimal(num_binario: str) -> int:
    """
    Convierte un número binario (como string) a su equivalente decimal.
    
    Parámetros:
        num_binario (str): Cadena binaria a convertir (ej: "1010").
    
    Retorna:
        int: Valor decimal equivalente (ej: 10).
    """
    sumador = 0  # Acumulador del resultado decimal

    # Invertimos el string para que el índice 0 corresponda a 2^0 (bit menos significativo)
    binario_invertido = num_binario[::-1]

    # Recorremos cada bit: si es "1", sumamos la potencia de 2 correspondiente a su posición
    for i in range(len(binario_invertido)):
        if binario_invertido[i] == "1":
            sumador += 2 ** i

    return sumador  # Retornamos el valor decimal calculado


def validar_numero_entrada(msj: str) -> str:
    """
    Solicita al usuario un número entero positivo y lo valida.
    Repite la solicitud hasta que el usuario ingrese solo dígitos.
    
    Parámetros:
        msj (str): Mensaje que se muestra al usuario al pedir el dato.
    
    Retorna:
        str: El número ingresado como string, garantizando que es un dígito válido.
    """
    num = input(msj)

    # Repetimos la solicitud mientras el valor ingresado no sea un número positivo válido
    while not num.isdigit():
        num = input("Error: Caracter Invalido. Intente nuevamente: ")

    return num


def es_binario(cadena_binaria: str) -> bool:
    """
    Verifica si una cadena está compuesta únicamente por los caracteres '0' y '1'.
    
    Parámetros:
        cadena_binaria (str): Cadena a verificar.
    
    Retorna:
        bool: True si es un binario válido, False si contiene otros caracteres.
    """
    for caracter in cadena_binaria:
        if caracter not in ["0", "1"]:
            return False  # Encontramos un carácter inválido, no es binario
    return True  # Todos los caracteres son 0 o 1


# -------------------------------------------------------
# Programa principal: menú interactivo
# -------------------------------------------------------

print("*** Bienvenido al Sitio ***")

while True:
    # Mostramos el menú y pedimos una opción válida al usuario
    opcion_ingresada = validar_numero_entrada(
        "Menú de opciones:\n"
        "1 - Convertir numero decimal a binario.\n"
        "2 - Convertir número binario a decimal.\n"
        "3 - Operaciones de Lógica Proposicional (Tablas de verdad)\n"
        "4 - Salir.\n"
    )
    opcion_ingresada = int(opcion_ingresada)  # Convertimos a entero para comparar

    if opcion_ingresada == 1:
        # --- Opción 1: Decimal → Binario ---
        print("Conversión de número decimal a binario.")
        num_decimal = validar_numero_entrada("Ingrese un número (entero positivo): ")
        num_binario = decimal_a_binario(num_decimal)
        print(f"El número decimal {num_decimal} equivale a {num_binario} en binario.\n")

    elif opcion_ingresada == 2:
        # --- Opción 2: Binario → Decimal ---
        print("Conversión de número binario a decimal.")
        num_binario = validar_numero_entrada("Ingrese un número binario: ")

        # Verificamos que el número ingresado sea realmente un binario válido
        if not es_binario(num_binario):
            print("Error: El número ingresado no es un binario válido (solo 0 y 1).")
            continue  # Volvemos al inicio del menú sin procesar

        num_decimal = binario_a_decimal(num_binario)
        print(f"El número binario {num_binario} equivale a {num_decimal} en decimal.\n")

    elif opcion_ingresada == 3:
        # --- Opción 3: Condicional lógica (p → q) ---
        print("\n--- Verificador de Condicional Lógica (p -> q) ---")
        print("Ingrese 1 para Verdadero o 0 para Falso")

        p = int(validar_numero_entrada("Valor de p: "))
        q = int(validar_numero_entrada("Valor de q: "))

        # Verificamos que los valores sean exactamente 0 o 1 (valores lógicos válidos)
        if p in [0, 1] and q in [0, 1]:
            # La condicional p → q es falsa SOLO cuando p es Verdadero y q es Falso
            # En todos los demás casos, el resultado es Verdadero
            resultado = not (p == 1 and q == 0)
            valor_final = "Verdadero (1)" if resultado else "Falso (0)"
            print(f"La proposición p -> q es: {valor_final}\n")
        else:
            print("Error: Los valores lógicos deben ser 0 o 1.\n")

    elif opcion_ingresada == 4:
        # --- Opción 4: Salir del programa ---
        print("Saliendo del programa.")
        break  # Terminamos el bucle principal

    else:
        # Opción fuera de rango: volvemos a mostrar el menú
        print("Error: Opción invalida. Intente nuevamente.")
        continue