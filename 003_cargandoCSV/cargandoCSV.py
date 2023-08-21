def cargandoUnCSV():
    import pandas as pd
    datos = pd.read_csv('003_cargandoCSV\clientes.csv',encoding='latin-1',sep=';')
    print(datos)
    return(datos)
cargandoUnCSV()

verTiposDeDatos=cargandoUnCSV().dtypes#Los datos de tipo OBJECT implican un string, INT64 un entero y FLOAT64 un decimal.
extraerColumna=cargandoUnCSV()['RUT']#Para vicualizar solo una columna debemos llamar al dataframe, y agregar entre corchetes el nombre la columna de interes
extraerFila=cargandoUnCSV().loc[658]
extrayendoFilas=cargandoUnCSV().loc[100:105]
print(extrayendoFilas)