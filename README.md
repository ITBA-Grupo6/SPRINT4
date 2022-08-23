# SPRINT4
Sprint 4 del Full Stack Developer Challenge

Problemática:

Se quiere poder consultar los cheques que tiene emitidos y depositados en suscuentas un determinado cliente, pudiendo estar estos 
pendientes, aprobado o rechazado. 
Para esto la problemática a resolver es que se tiene que obtener la información desde un archivo.
Por lo que dado un script en Python se solicita que se puedan ingresar lassiguientes acciones por línea de comando y se visualicen
los resultados porpantalla.

Requerimientos específicos:
  1. El script de Python se debe llamar listado_chesques.py
  2. El orden de los argumentos son los siguientes: 
    a. Nombre del archivo csv.
    b. DNI del cliente donde se filtraran.
    c. Salida: PANTALLA o CSV
    d. Tipo de cheque: EMITIDO o DEPOSITADO
    e. Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
    f. Rango fecha: xx-xx-xxxx:yy-yy-yyyy. (Opcional)
    
  3. Si para un DNI dado un número de cheque de una misma cuenta se repite se debe mostrar el error por pantalla, indicando que ese 
  es el problema.

  4. Si el parámetro “Salida” es PANTALLA se deberá imprimir por pantalla todoslos valores que se tienen, y si “Salida” es CSV se 
  deberá exportar a un csv con las siguientes condiciones:
    a. El nombre de archivo tiene que tener el formato<DNI><TIMESTAMPS ACTUAL>.csv
    b. Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.

    Ejemplos para verificar el punto (3.) y (4.): 

      Para verificar si se repite un nro. de cheque por PANTALLA:     
        python3 .\listado_cheques.py test.csv 40998788 PANTALLA EMITIDO
      Para verificar si se repite un nro. de cheque por CSV:
        python3 .\listado_cheques.py test.csv 40998788 CSV EMITIDO
      En ambos casos se muestra por pantalla> 
        El DNI: 40998788 tiene cheques con igual número: 0005

      Para verificar salida por PANTALLA:
        python3 .\listado_cheques.py test.csv 1617591371 PANTALLA EMITIDO
      Para verificar salida por CSV: 
        python3 .\listado_cheques.py test.csv 1617591371 CSV EMITIDO
      La estructura del archivo CSV generado es de tipo: 
        NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago
        23123132,12312312,5000,1617591371,1617591371
        23123132,12312312,5000,1617591371,1617591371

  5. Si el estado del cheque no se pasa, se deberán imprimir los cheques sin filtrar por estado.

    Ejemplos para verificar el punto (5.): 

      Para verificar salida por PANTALLA:
        python3 .\listado_cheques.py test.csv 1617591371 PANTALLA
      Para verificar salida por CSV: 
        python3 .\listado_cheques.py test.csv 1617591371 CSV
  
