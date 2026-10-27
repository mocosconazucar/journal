def lockFile(rutaArchivo, fechaActual):                                        # Función para asegurar que solo exista una escritura por día
    with open(rutaArchivo, "r", encoding="utf-8") as lastVer:   # se abre el archivo en modo "read"
        fechaFormateada = fechaActual.strftime("%d/%m")
        lastEntry = lastVer.readlines()[-2]                     # leer la última entrada en el archivo
        if lastEntry[1:6] == fechaFormateada:                   
            return True                                         # si la fecha de la última entrada coincide con la fecha actual
        else:                                                   # se devuelve un valor para no permitir que se escriba el diario
            return False            

def blockNotif(fechaActual):
    hRest = 23 -int(fechaActual.strftime("%H"))                 # calcula cuánto tiempo falta para un nuevo día
    mRest = 60 -int(fechaActual.strftime("%M"))                 # y lo informa en un mensaje por pantalla
    print(f"¡Ya escribiste una entrada para el día de hoy!\nPuedes escribir una nueva en {hRest} horas y {mRest} minutos.")  

def newEntry(nomArchivo, fechaHoy):
    diasES = { "Mon":"Lunes","Tue":"Martes","Wed":"Miércoles","Thu":"Jueves","Fri":"Viernes","Sat":"Sábado", "Sun":"Domingo"}
    # diccionario para transformar los días de la semana a su equivalente en español
    dia = fechaHoy.strftime("%d")
    mes = fechaHoy.strftime("%m")
    diaSemana = diasES[fechaHoy.strftime("%a")]                # obtiene el dia de la semana a partir del dia de hoy
    nomArchivo.write(f"[{dia}/{mes}({diaSemana})]: ")        # escribe la fecha a partir de los datos obtenidos previamente
    nomArchivo.write(input("¿Cómo te sientes hoy?: "))        # pide al usuario el contenido de la entrada y lo añade
    print("Tu entrada se guardó correctamente.")            # muestra un mensaje confirmando el éxito de la tarea
    nomArchivo.write("\n" + "-"*50 + "\n")                  # deja un separador para que se distinga una entrada de otra.