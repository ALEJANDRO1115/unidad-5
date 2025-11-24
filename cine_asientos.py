
# cine_asientos.py

def crear_sala(filas, columnas):
    """Crea la matriz inicial de asientos libres (L)."""
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    """Imprime la sala con formato bonito."""
    print("\nEstado de la sala:")
    for fila in sala:
        print(" ".join(fila))
    print()

def reservar_asiento(sala, fila, columna):
    """Reserva un asiento si está libre."""
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("El asiento no existe.")
    elif sala[fila][columna] == "X":
        print("El asiento ya está ocupado.")
    else:
        sala[fila][columna] = "X"
        print("Asiento reservado correctamente.")

def liberar_asiento(sala, fila, columna):
    """Libera un asiento si está ocupado."""
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("El asiento no existe.")
    elif sala[fila][columna] == "L":
        print("El asiento ya está libre.")
    else:
        sala[fila][columna] = "L"
        print("Asiento liberado correctamente.")

def contar_asientos(sala):
    """Cuenta asientos libres y ocupados."""
    libres = sum(fila.count("L") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)
    print("\nEstadísticas:")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")

def menu():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    sala = crear_sala(filas, columnas)

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_sala(sala)
        elif opcion == "2":
            fila = int(input("Ingrese la fila: ")) - 1
            columna = int(input("Ingrese la columna: ")) - 1
            reservar_asiento(sala, fila, columna)
        elif opcion == "3":
            fila = int(input("Ingrese la fila: ")) - 1
            columna = int(input("Ingrese la columna: ")) - 1
            liberar_asiento(sala, fila, columna)
        elif opcion == "4":
            contar_asientos(sala)
        elif opcion == "5":
            print("Gracias por usar el sistema de cine. Hasta luego.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
