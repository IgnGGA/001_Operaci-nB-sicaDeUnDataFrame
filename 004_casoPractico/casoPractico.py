def importandoDatos():
    import pandas as pd
    datos=pd.read_csv('004_casoPractico\datos_pacientes.csv', encoding='latin-1', sep=';')
    return datos

#Información de la columna 'Monto_Deuda'.
#La fila con índice 651
#Las filas desde el índice 100 al 200, luego estas filas pero solo la columna 'RUT' y 'NOMBRE'
#Los pacientes que tienen previsión FONASA
#Los pacientes que tienen deuda mayor a $1.000.000

def desarrollo():
    datos=importandoDatos()
    print('Columna Deuda:\n',datos['Monto_Deuda'],'\n')
    print('Fila índice 651:\n',datos.loc[651],'\n')
    print('Filas índices 100-200:\n',datos.loc[100:200],'\n')
    print('Pacientes con FONASA:\n',datos.loc[datos['PrevisiÃ³n']=='FONASA'],'\n')
    print('Deudas mayores a $1.000.000\n',datos.loc[datos['Monto_Deuda']>1000000],'\n-------------------------------------')
desarrollo()