def cargandoUnCSV():
    import pandas as pd
    datos = pd.read_csv('003_cargandoCSV\clientes.csv',encoding='latin-1',sep=';')
    print(datos)
    return(datos)
cargandoUnCSV()

verTiposDeDatos=cargandoUnCSV().dtypes#Los datos de tipo OBJECT implican un string, INT64 un entero y FLOAT64 un decimal.
extraerColumna=cargandoUnCSV()['RUT']#Para vicualizar solo una columna debemos llamar al dataframe, y agregar entre corchetes el nombre la columna de interes
extraerFila=cargandoUnCSV().loc[658]#Con .loc(n) podemos revisar la fila de interes
extrayendoFilas=cargandoUnCSV().loc[100:105]#Con .loc(m:n) podemos revisar el rango de filas de interes
extraerValor=cargandoUnCSV().loc[658]['FECHA_NAC']#Con .loc[m][n], al igual que en una matriz, veremos el dato de la fila m y la columna n
extraervalorFiltrado=cargandoUnCSV().loc[cargandoUnCSV()['TIPO_CLIENTE']=='A']#De esta forma llamara al dataframe y solo mostrara las filas que tengan ese valor en la columna indicada
print(extrayendoFilas)