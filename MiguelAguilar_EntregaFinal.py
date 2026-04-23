import os

# =============================================
# Usuarios y contraseñas del sistema
# (solo en comentario, no se muestran en pantalla)
# ADMIN  - Contraseña: 123
# LUIS   - Contraseña: 456
# MIGUEL - Contraseña: 789
# =============================================

# --- Variables globales ---
reservas = []       # Lista que almacena todas las reservas
nombre = ""         # Nombre del usuario registrado en Módulo 1
apellido = ""       # Apellido del usuario registrado en Módulo 1
telefono = 0        # Teléfono del usuario registrado en Módulo 1


# =============================================
# Función para limpiar la pantalla
# =============================================
def limpiar_consola():
    os.system('cls')


# =============================================
# Subprograma: Inicio de sesión
# =============================================
def inicio_sesion():
    intentos = 0
    acceso_exitoso = False

    print("=" * 52)
    print("   Bienvenido al sistema de reservas para")
    print("          canchas de futbol")
    print("=" * 52)

    while not acceso_exitoso and intentos < 3:
        usuario = input("\nIngrese su usuario: ").strip().upper()
        contrasena = input("Ingrese su contrasena: ").strip()

        if (usuario == "ADMIN" and contrasena == "123") or \
           (usuario == "LUIS"  and contrasena == "456") or \
           (usuario == "MIGUEL" and contrasena == "789"):
            acceso_exitoso = True
        else:
            intentos += 1
            if intentos < 3:
                print(f"Acceso denegado. Intentos restantes: {3 - intentos}")
            else:
                print("Acceso denegado. Ha superado los intentos permitidos.")

    return acceso_exitoso


# =============================================
# Subprograma: Módulo 1 - Registro de datos del usuario
# =============================================
def modulo_registro():
    global nombre, apellido, telefono

    print("\n" + "=" * 52)
    print("   MODULO 1 - Registro de datos del usuario")
    print("=" * 52)

    nombre = input("Ingrese su nombre: ").strip()
    apellido = input("Ingrese su apellido: ").strip()

    while True:
        try:
            telefono = int(input("Ingrese su numero de telefono (8 digitos): "))
            if 10000000 <= telefono <= 99999999:
                break
            else:
                print("Numero no valido. Debe tener exactamente 8 digitos.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

    print("\nRegistro de datos exitoso.")


# =============================================
# Subprograma: Módulo 2 - Registrar fecha, hora y verificar disponibilidad
# =============================================
def modulo_procesamiento():
    global reservas

    print("\n" + "=" * 52)
    print("   MODULO 2 - Registro de fecha y hora")
    print("=" * 52)

    if nombre == "" or apellido == "" or telefono == 0:
        print("\nDebe registrar sus datos personales primero (Opcion 1).")
        return

    # Validar mes
    while True:
        try:
            mes = int(input("Ingrese el mes de la reserva (1-12): "))
            if 1 <= mes <= 12:
                break
            else:
                print("El mes ingresado no es valido. Debe estar entre 1 y 12.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

    # Validar día
    while True:
        try:
            dia = int(input("Ingrese el dia de la reserva (1-31): "))
            if 1 <= dia <= 31:
                break
            else:
                print("El dia ingresado no es valido. Debe estar entre 1 y 31.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

    # Validar hora
    while True:
        try:
            hora = int(input("Ingrese la hora de la reserva (8-24): "))
            if 8 <= hora <= 24:
                break
            else:
                print("La hora ingresada no es valida. Debe estar entre 8 y 24.")
        except ValueError:
            print("Por favor ingrese un numero valido.")

    # Verificar traslape con reservas existentes
    for r in reservas:
        if r["mes"] == mes and r["dia"] == dia and r["hora"] == hora:
            print("\nNo es posible hacer su reserva, la cancha ya esta reservada para ese dia y hora.")
            return

    # Guardar la nueva reserva en la lista
    nueva_reserva = {
        "nombre":   nombre,
        "apellido": apellido,
        "telefono": telefono,
        "mes":      mes,
        "dia":      dia,
        "hora":     hora
    }
    reservas.append(nueva_reserva)
    print(f"\nSu reserva fue registrada para el dia {dia}/{mes} a las {hora}:00.")


# =============================================
# Subprograma: Módulo 3 - Visualización de reservas activas
# =============================================
def modulo_visualizacion():
    print("\n" + "=" * 52)
    print("   MODULO 3 - Reservas activas")
    print("=" * 52)

    if len(reservas) == 0:
        print("\nNo hay ninguna reserva registrada.")
        return

    for i in range(len(reservas)):
        r = reservas[i]
        print(f"\n--- Reserva #{i + 1} ---")
        print(f"  Nombre:           {r['nombre']} {r['apellido']}")
        print(f"  Telefono:         {r['telefono']}")
        print(f"  Fecha:            {r['dia']}/{r['mes']}")
        print(f"  Hora:             {r['hora']}:00")


# =============================================
# Subprograma: Módulo 4 - Informes
# =============================================
def modulo_informes():
    print("\n" + "=" * 52)
    print("   MODULO 4 - Informes")
    print("=" * 52)
    print("1 ---- Informe 1: Total de reservas por mes")
    print("2 ---- Informe 2: Horarios mas demandados")
    print("3 ---- Volver al menu principal")
    print("=" * 52)

    while True:
        opcion_informe = input("Seleccione un informe (1-3): ").strip()

        if opcion_informe == "1":
            informe_reservas_por_mes()
        elif opcion_informe == "2":
            informe_horarios_demandados()
        elif opcion_informe == "3":
            break
        else:
            print("Opcion no valida. Seleccione entre 1 y 3.")

        print("\n" + "=" * 52)
        print("   MODULO 4 - Informes")
        print("=" * 52)
        print("1 ---- Informe 1: Total de reservas por mes")
        print("2 ---- Informe 2: Horarios mas demandados")
        print("3 ---- Volver al menu principal")
        print("=" * 52)


# =============================================
# Informe 1: Total de reservas por mes
# =============================================
def informe_reservas_por_mes():
    print("\n--- Informe 1: Total de reservas por mes ---")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return

    meses_nombres = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }

    # Contamos reservas por mes usando una lista de 12 posiciones
    conteo_meses = [0] * 13   # índice 1-12

    for r in reservas:
        conteo_meses[r["mes"]] += 1

    for m in range(1, 13):
        if conteo_meses[m] > 0:
            print(f"  {meses_nombres[m]}: {conteo_meses[m]} reserva(s)")

    mes_mayor = conteo_meses.index(max(conteo_meses[1:]), 1)
    print(f"\nMes con mas reservas: {meses_nombres[mes_mayor]} ({conteo_meses[mes_mayor]} reserva(s))")


# =============================================
# Informe 2: Horarios más demandados
# =============================================
def informe_horarios_demandados():
    print("\n--- Informe 2: Horarios mas demandados ---")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return

    # Contamos reservas por hora (8 a 24) usando una lista de 25 posiciones
    conteo_horas = [0] * 25   # índice 0-24, usamos 8-24

    for r in reservas:
        conteo_horas[r["hora"]] += 1

    print(f"  {'Hora':<10} {'Reservas'}")
    print(f"  {'-'*20}")
    for h in range(8, 25):
        if conteo_horas[h] > 0:
            print(f"  {h}:00{' ' * 7}{conteo_horas[h]} reserva(s)")

    hora_pico = conteo_horas.index(max(conteo_horas))
    print(f"\nHorario mas demandado: {hora_pico}:00 ({conteo_horas[hora_pico]} reserva(s))")


# =============================================
# Subprograma: Menú principal
# =============================================
def menu():
    while True:
        print("\n" + "=" * 52)
        print("   MENU PRINCIPAL - Sistema de Reservas")
        print("=" * 52)
        print("1 ---- Registrar datos del usuario")
        print("2 ---- Registrar fecha y hora de reserva")
        print("3 ---- Ver reservas activas")
        print("4 ---- Informes")
        print("5 ---- Salir del sistema")
        print("=" * 52)

        opcion_menu = input("Seleccione una opcion (1-5): ").strip()

        if opcion_menu == "1":
            modulo_registro()
        elif opcion_menu == "2":
            modulo_procesamiento()
        elif opcion_menu == "3":
            modulo_visualizacion()
        elif opcion_menu == "4":
            modulo_informes()
        elif opcion_menu == "5":
            print("\nSalida del sistema exitosa. Hasta luego!")
            break
        else:
            print("\nOpcion no valida. Por favor seleccione entre 1 y 5.")


# =============================================
# Programa principal (main)
# =============================================
def main():
    limpiar_consola()
    acceso_exitoso = inicio_sesion()

    if acceso_exitoso:
        print("\nAcceso exitoso, credenciales validadas.")
        menu()
    else:
        print("\nSistema bloqueado por superar los intentos permitidos.")

main()