from xml.dom import minidom
from clases import *
from celdaviva import *    
import rejillas as reji
import grafica as grafi

if __name__ == "__main__":
    
   

    ruta = input("Ingrese la ruta del archivo: ")
    archivo = open(ruta, "r")


    doc = minidom.parse(archivo)

    organismos = doc.getElementsByTagName("organismo")
    muestras = doc.getElementsByTagName("muestra")

    for organismo in organismos:
        codigo = organismo.getElementsByTagName("codigo")[0].firstChild.data
        nombre = organismo.getElementsByTagName("nombre")[0].firstChild.data
        print(f"Codigo: {codigo}, Nombre: {nombre}")

    for muestra in muestras:
        codigo = muestra.getElementsByTagName("codigo")[0].firstChild.data
        descripcion = muestra.getElementsByTagName("descripcion")[0].firstChild.data
        filas = muestra.getElementsByTagName("filas")[0].firstChild.data
        columnas = muestra.getElementsByTagName("columnas")[0].firstChild.data

        print("-------------------------------------------")
        print(f"Codigo: {codigo}, Descripcion: {descripcion}, {filas}, {columnas}")
        nueva_rejilla= reji.rejilla(int(columnas),int(filas))

        celdas_vivas = muestra.getElementsByTagName("celdaViva")
        for celda_viva in celdas_vivas:
            fila = celda_viva.getElementsByTagName("fila")[0].firstChild.data
            columna = celda_viva.getElementsByTagName("columna")[0].firstChild.data
            codigo_organismo = celda_viva.getElementsByTagName("codigoOrganismo")[0].firstChild.data

            print("-------------------------------------------")
            print(f"Celda Viva - {fila}, {columna}, Codigo de Organismo: {codigo_organismo}")
    grafi.crear_archivo_dot()
    

