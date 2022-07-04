from datetime import datetime
from sqlite3 import Timestamp
import sys
import csv
#obtengo parametros
parametros = sys.argv

#declaro variables
dni=0
salida=0
tipo_cheque=0
estado_cheque=0
fechas=[0,0]
se_ingreso_fecha = False
se_ingreso_estado = False

if len(parametros) > 1:
    dni = parametros[1]
    salida= parametros[2]
    tipo_cheque = parametros[3]
    if len(parametros) > 4: #si se pidio el estado...
        estado_cheque = parametros[4]
        se_ingreso_estado = True
        if len(parametros) > 5: #si se pidio el rango de fechas...
            rango_fecha = parametros[5]
            se_ingreso_fecha = True
            # en el siguiente se crea una lista con los segundos desde 1970 de las dos fechas ingresadas... se utiliza datetime, split, y list comprehension
            # quedo muy ilegible, pido disculpas.
            fechas = [datetime(fecha.split("-")[2],fecha.split("-")[1],fecha.split("-")[0]).timestamp() for fecha in rango_fecha.split(":")]
else:
    print("Ingrese bien los parametros!")

print("Los argumentos pasados fueron: ",sys.argv) #para verificar nomas, despues se borra.
print("Los datos obtenidos fueron: ",dni, salida, tipo_cheque, estado_cheque, fechas) #para verificar nomas, despues se borra.

archivo= open('test.csv', 'r') # abre el archivo
lineas = csv.reader(archivo) # lee el archivo

cheques_a_devolver = []
NroCheque = []

for linea in lineas:
    if linea[-3] == dni: #si coincide el dni...        
        NroCheque.append(linea[0])

if len(NroCheque) != len(set(NroCheque)):
    print("El DNI:", dni, "tiene dos cheques iguales con nro:", NroCheque[0])
    quit()

archivo= open('test.csv', 'r') # abre el archivo
lineas = csv.reader(archivo) # lee el archivo

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

if salida =='CSV':
    TIMESTAMPSACTUAL = str(datetime.now().timestamp())
    ar = open (dni + TIMESTAMPSACTUAL + '.csv', 'a')
    archivoCSV = csv.writer(ar)
    archivoCSV.writerows(cheques_a_devolver)
    ar.close()
elif salida == "CONSOLA":
    for cheque in cheques_a_devolver:
        print("Los cheques son:", cheque)
    if len(cheques_a_devolver)==0:
        print("No se obtuvieron cheques.")