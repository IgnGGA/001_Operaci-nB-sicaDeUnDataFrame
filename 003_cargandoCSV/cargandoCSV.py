def cargandoUnCSV():
    import pandas as pd
    datos = pd.read_csv('003_cargandoCSV\clientes.csv',encoding='latin-1',sep=';')
    print(datos)
    return(datos)
cargandoUnCSV()

verTiposDeDatos=cargandoUnCSV().dtypes
print(verTiposDeDatos)#Los datos de tipo OBJECT implican un string, INT64 un entero y FLOAT64 un decimal.