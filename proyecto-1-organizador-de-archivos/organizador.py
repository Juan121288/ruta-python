import os
import shutil
# Metodos consultados :help(os.mkdir) #help(os.makedirs) #help(os.path.isdir) 
# Explicacion de construccion de funcion :Despues de for in () -->if os.path.isdir() --> implementar continue despues
# para ver el contenido de la carpeta: print(os.listdir('test_carpeta')) 
archivos =  (os.listdir('test_carpeta'))
# for in para recorrer y mover cada archivo segun su extension
for archivo in (archivos):            #print(archivo) para ver cada archivo de 'archivos'
    ruta_origen = 'test_carpeta/' + archivo
# os.path.isdir() para saltar cada carpeta y pasar el siguiente archivo
    if os.path.isdir(ruta_origen):
        continue
# .startswith() para ignorar archivos que empiecen con '.'
    if archivo.startswith('.'):
        continue
# variable para dividir el nombre en dos segun la extencion '.' y seleccionarla [1]
    partes = archivo.split('.')       #print(partes) para ver una lista que divide el nombre del archivo por '.'
    extension = partes[-1] # [-1] --> para agarrar la ultima parte de la lista y no unicamente la segunda
    print(extension)
# ruta_origen = 'test_carpeta/' + archivo ---> desplazda a la linea 9 para agregar os.path.isdir() y .startwitch()
# Mover archivos 'pdf' o 'txt' a la carpeta documentos, si no existe la crea
    if (extension == 'pdf') or (extension == 'txt'):
        print(f'{archivo} movido a "documentos"') #print('Este archivo va en "documentos"') --> antiguo nombre
        os.makedirs('test_carpeta/documentos', exist_ok=True)
        shutil.move(ruta_origen, 'test_carpeta/documentos')
# Mover archivos 'jpg' a la carpeta fotos, si no existe la crea
    elif extension == 'jpg':
        print(f'{archivo} movido a "fotos"') #print('Este archivo va en "fotos"') --> antiguo nombre
        os.makedirs('test_carpeta/fotos', exist_ok=True)
        shutil.move(ruta_origen, 'test_carpeta/fotos')
# Mover archivos los archivos restantes a la carpeta otros, si no existe la crea
    else:
        print(f'{archivo} movido a "otros"') #print('Este archivo va en "fotos"') --> antiguo nombre
        os.makedirs('test_carpeta/otros', exist_ok=True)
        shutil.move(ruta_origen, 'test_carpeta/otros')