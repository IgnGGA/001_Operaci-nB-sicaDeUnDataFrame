def creandoUnDataFrame():
    import pandas as pd
    datos = [['Felipe',24,'Masculino',4.5],['Andrea',21,'Femenino',7.0],['Tomás',22,'Masculino',6.1],['Roberto',20,'Masculino',5.5]]
    df = pd.DataFrame(datos, columns=['Nombre','Edad','Genero','Calificación'])
    print(df)

creandoUnDataFrame()