import pyodbc

# Conexión a la base de datos con autenticación de Windows
try:
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EGIQPU3;DATABASE=FINANZAS1;Trusted_Connection=yes')
    cursor = conexion.cursor()
    
    # Eliminar las tablas si existen
    cursor.execute('''
        IF OBJECT_ID('Ingresos', 'U') IS NOT NULL
        DROP TABLE Ingresos
    ''')
    cursor.execute('''
        IF OBJECT_ID('Gastos', 'U') IS NOT NULL
        DROP TABLE Gastos
    ''')
    cursor.execute('''
        IF OBJECT_ID('Prestamos', 'U') IS NOT NULL
        DROP TABLE Prestamos
    ''')
    conexion.commit()
    
    # Creación de las tablas
    cursor.execute('''
        CREATE TABLE Ingresos (
            id INT PRIMARY KEY IDENTITY(1,1),
            cantidad DECIMAL(18, 2),
            descripcion NVARCHAR(255)
        )
    ''')
    cursor.execute('''
        CREATE TABLE Gastos (
            id INT PRIMARY KEY IDENTITY(1,1),
            cantidad DECIMAL(18, 2),
            descripcion NVARCHAR(255)
        )
    ''')
    cursor.execute('''
        CREATE TABLE Prestamos (
            id INT PRIMARY KEY IDENTITY(1,1),
            cantidad DECIMAL(18, 2),
            tasa_interes DECIMAL(18, 2),
            plazo INT
        )
    ''')
    conexion.commit()

    # Funciones para interactuar con la base de datos
    def agregar_ingreso_db(cantidad, descripcion):
        cursor.execute("INSERT INTO Ingresos (cantidad, descripcion) VALUES (?, ?)", (cantidad, descripcion))
        conexion.commit()

    def agregar_gasto_db(cantidad, descripcion):
        cursor.execute("INSERT INTO Gastos (cantidad, descripcion) VALUES (?, ?)", (cantidad, descripcion))
        conexion.commit()

    def agregar_prestamo_db(cantidad, tasa_interes, plazo):
        cursor.execute("INSERT INTO Prestamos (cantidad, tasa_interes, plazo) VALUES (?, ?, ?)", (cantidad, tasa_interes, plazo))
        conexion.commit()

    def listar_ingresos_db():
        cursor.execute("SELECT * FROM Ingresos")
        ingresos = cursor.fetchall()
        print("\n--- Ingresos ---")
        for ingreso in ingresos:
            print(f"{ingreso.id}. {ingreso.descripcion} - {ingreso.cantidad}")

    def listar_gastos_db():
        cursor.execute("SELECT * FROM Gastos")
        gastos = cursor.fetchall()
        print("\n--- Gastos ---")
        for gasto in gastos:
            print(f"{gasto.id}. {gasto.descripcion} - {gasto.cantidad}")

    def listar_prestamos_db():
        cursor.execute("SELECT * FROM Prestamos")
        prestamos = cursor.fetchall()
        print("\n--- Préstamos ---")
        for prestamo in prestamos:
            print(f"{prestamo.id}. Monto: {prestamo.cantidad} - Tasa: {prestamo.tasa_interes} - Plazo: {prestamo.plazo} años")

    # Función principal del programa
    def main():
        while True:
            print("\nBienvenido a tu gestor financiero")
            print("1. Agregar Ingreso")
            print("2. Agregar Gasto")
            print("3. Agregar Préstamo")
            print("4. Listar Ingresos")
            print("5. Listar Gastos")
            print("6. Listar Préstamos")
            print("7. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                cantidad = float(input("Ingrese la cantidad del ingreso: "))
                descripcion = input("Ingrese la descripción del ingreso: ")
                agregar_ingreso_db(cantidad, descripcion)
            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad del gasto: "))
                descripcion = input("Ingrese la descripción del gasto: ")
                agregar_gasto_db(cantidad, descripcion)
            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad del préstamo: "))
                tasa_interes = float(input("Ingrese la tasa de interés (porcentaje): "))
                plazo = int(input("Ingrese el plazo del préstamo en años: "))
                agregar_prestamo_db(cantidad, tasa_interes, plazo)
            elif opcion == "4":
                listar_ingresos_db()
            elif opcion == "5":
                listar_gastos_db()
            elif opcion == "6":
                listar_prestamos_db()
            elif opcion == "7":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

    # Ejecutar el programa
    if __name__ == "__main__":
        main()

finally:
    conexion.close()
