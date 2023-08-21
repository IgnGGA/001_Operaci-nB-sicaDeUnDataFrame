def importacionDatos():
    import pandas as pd
    datos = pd.read_csv('datos_pacientes.csv', encoding='utf-8', sep=';')
    print(datos)

importacionDatos()