import pandas as pd
import os

# listo la ruta del archivo a leer
list_path = os.listdir("C:/")
if len(list_path) > 0:
    #mostramos la cantidad de archivos detectados
    print("Archivos detectados --> " + str(len(list_path)))
    # confirmamos accion
    confirmar=input("¿Generar fichero?S/N")
    if (confirmar=="S"):
        for file_ in list_path:
            if(file_ != ".DS_Store"):
                #leemos el fichero excel e indicamos columnas a transformar en JSON
                data = pd.read_excel("C:/"+ file_,usecols="A:B")
                data.to_json(path_or_buf= file_+'.json',orient='records')
        else:
            print("Fin del proceso")