from datetime import datetime
from sqlite3 import Timestamp
import sys
import csv
parametros = sys.argv

if len (parametros) >1:
    dni = parametros[1]
    salida= parametros[2]
    tipo_cheque = parametros[3]

print(sys.argv)

archivo= open('test.csv', 'r') # abre el archivo
lineas = csv.reader(archivo) # lee el archivo


for linea in lineas:
    if linea[-3] == dni:
        if linea[1] == tipo_cheque:
            print(linea[-2])
            break
    else:
        print("No existe el DNI")
        break

archivo.close

if salida =='CSV':
    TIMESTAMPSACTUAL = str(datetime.now().timestamp())
    ar = open (dni + TIMESTAMPSACTUAL + '.csv', 'a')
    archivoCSV = csv.writer(ar)
    archivoCSV.writerow(linea)
    ar.close()
elif salida == 'TXT':
    ar = open (dni + '.txt', 'a')
    archivoTXT = csv.writer(ar)
    archivoTXT.writerow(linea)
    ar.close()
    