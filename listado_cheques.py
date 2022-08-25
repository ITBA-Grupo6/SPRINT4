from datetime import datetime
from sqlite3 import Timestamp
import sys
import csv
#obtengo parametros
parametros = sys.argv

#declaro variables
csv_file = ""
dni=0
salida=0
tipo_cheque=""
estado_cheque=0
fechas=[0,0]
se_ingreso_fecha = False
se_ingreso_estado = False

if len(parametros) > 1 & len(parametros) < 4 :
    csv_file = parametros[1]
    dni = parametros[2]
    salida= parametros[3]
    tipo_cheque = "0"
    if len(parametros) > 4:
        tipo_cheque = parametros[4]
        if len(parametros) > 5: #si se pidio el estado...
            estado_cheque = parametros[5]
            se_ingreso_estado = True
            if len(parametros) > 6: #si se pidio el rango de fechas...
                rango_fecha = parametros[6]
                se_ingreso_fecha = True
                # en el siguiente se crea una lista con los segundos desde 1970 de las dos fechas ingresadas... se utiliza datetime, split, y list comprehension
                # quedo muy ilegible, pedimos disculpas.
                fechas = [datetime(fecha.split("-")[2],fecha.split("-")[1],fecha.split("-")[0]).timestamp() for fecha in rango_fecha.split(":")]
else:
    print("Ingrese bien los parametros!")

#print("Los argumentos pasados fueron: ",sys.argv) #para verificar nomas, despues se borra.
#print("Los datos obtenidos fueron: ", csv_file, dni, salida, tipo_cheque, estado_cheque, fechas) #para verificar nomas, despues se borra.

archivo = open(csv_file, "r") # abre el archivo
lineas = csv.reader(archivo) # lee el archivo

cheques_a_devolver = []
NroCheque = []

# Verificación de cheque repetido para un DNI 
for linea in lineas:
    if linea[-3] == dni:         
        NroCheque.append(linea[0])

if len(NroCheque) != len(set(NroCheque)):
    print("El DNI:", dni, "tiene cheques con igual número:", NroCheque[0])
    quit()

archivo= open(csv_file, "r") # abre el archivo
lineas = csv.reader(archivo) # lee el archivo

# Verificacion de si tipo_cheque no se pasó como parámetro 
if tipo_cheque == "0": 
    for linea in lineas:
        if linea[-3] == dni: #si coincide el dni...
                if se_ingreso_estado: # si se ingreso estado...
                    if estado_cheque == linea[-1]: #si el estado coincide...
                        if se_ingreso_fecha: # si se ingreso fecha...
                            if fechas[0] < linea[-5] < fechas [1]: # si la fecha esta entre las fechas indicadas...
                                cheques_a_devolver.append(linea)
                                continue
                            else: #si la fecha no esta entre las indicadas...
                                continue
                        else: #si no se ingreso fecha...
                            cheques_a_devolver.append(linea)
                    else: #si no coincide el estado...
                        continue
                else: #si no se ingreso estado...
                    cheques_a_devolver.append(linea)

# Ejecución si se especificó el tipo_cheque
else: 
     for linea in lineas:
        if linea[-3] == dni: #si coincide el dni...
            if linea[-2] == tipo_cheque: # y ademas coincide el tipo de cheque...
                if se_ingreso_estado: # si se ingreso estado...
                    if estado_cheque == linea[-1]: #si el estado coincide...
                        if se_ingreso_fecha: # si se ingreso fecha...
                            if fechas[0] < linea[-5] < fechas [1]: # si la fecha esta entre las fechas indicadas...
                                cheques_a_devolver.append(linea)
                                continue
                            else: #si la fecha no esta entre las indicadas...
                                continue
                        else: #si no se ingreso fecha...
                            cheques_a_devolver.append(linea)
                    else: #si no coincide el estado...
                        continue
                else: #si no se ingreso estado...
                    cheques_a_devolver.append(linea)

archivo.close

if salida == "CSV":
    cheques_a_devolverCSV = []
    linea = []
    if len(cheques_a_devolver)==0:
        print("No se obtuvieron cheques.")
    else:  
        TIMESTAMPSACTUAL = str(datetime.now().timestamp())
        ar = open ( dni + TIMESTAMPSACTUAL + ".csv", "a", newline='')
        header = ['NumeroCuentaOrigen', 'NumeroCuentaDestino', 'Valor', 'FechaOrigen', 'FechaPago']
        archivoCSV = csv.writer(ar)  
        archivoCSV.writerow(header)
        for cheque in cheques_a_devolver:
            cuenta_origen = cheque[-8]
            cuenta_destino = cheque[-7]
            valor = cheque[-6]
            fecha_origen = cheque[-5]
            fecha_pago = cheque[-4]  
            data = [cuenta_origen, cuenta_destino, valor, fecha_origen, fecha_pago]
            archivoCSV.writerow(data)
        ar.close()

elif salida == "PANTALLA":
    for cheque in cheques_a_devolver:
        print("Los cheques son:", cheque)
    if len(cheques_a_devolver)==0:
        print("No se obtuvieron cheques.")

