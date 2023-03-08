#Clase para organismo y obtener sus datos  
'''class Muestra:
    def __init__(self, codigo: str, descripcion: str, filas: int, columnas: int, celdasvivas):
        self.codigo = codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas
        self.celdasvivas = celdasvivas

    def celdasProsperas(self, organismo: Organismo):
        celdasprosperas = []
        for fila in range(self.filas):
            for columna in range(self.columnas):
                celda = self.obtener_celda(fila, columna)
                if not celda.tiene_organismo() and celda.puede_prosperar(organismo):
                    celdasprosperas.append(celda)
        return celdasprosperas

    def asignarOrganismo(self, fila, columna, organismo):
        celda = self.BuscarCelda(fila, columna)
        if celda is None:
            raise ValueError("La celda no existe en la muestra")
        if celda.organismo is not None:
            raise ValueError("La celda ya tiene un organismo asignado")
    
        celda.organismo = organismo
        self.ActualizarEstado()

    def actualizarMuestra(self):
        celdas_vivas = [celda for celda in self.celdas if celda.estado == "viva"]
        posiciones_vivas = {(celda.fila, celda.columna) for celda in celdas_vivas}
        posiciones_adyacentes = {(fila, columna) for (f, c) in posiciones_vivas for fila in range(f-1, f+2) for columna in range(c-1, c+2)}
        posiciones_muertas = posiciones_adyacentes - posiciones_vivas
        for (fila, columna) in posiciones_muertas:
            celda = self.BuscarCelda(fila, columna)
            if celda is not None:
                organismo_prosperan = [org for org in self.organismos if org.codigo]


    def muestraModificable(self) -> bool:
        for fila in range(self.filas):
            for columna in range(self.columnas):
                celda = self.obtenerCelda(fila, columna)
                if not celda.tiene_organismo() and celda.habitat_disponible():
                    return True
        return False

    def obtenerCelda(self, fila: int, columna: int):
        for celda in self.celdasvivas:
            if celda.fila == fila and celda.columna == columna:
                return celda
        return CeldaViva(fila, columna)


class NodoMuestra:

    def __init__(self, columna, fila):
        self.Vivo = Muestra(fila, columna)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.Vivo.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.Vivo.ObtenerColumna()

    def SetFila (self, fila):
        self.Vivo.Fila = fila

    def SetColumna (self, columna):
        self.Vivo.Columna = columna


class ColaMuestras:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregarMuestra(self, columna, fila):
        nuevonodo = NodoMuestra(columna, fila)
        if self.cabeza == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        else:
            self.cola.Siguiente = nuevonodo
            self.cola = nuevonodo
            
    def Imprimir(self):
        auxiliar = self.cabeza
        while auxiliar != None:
            print("Fila: " + str(auxiliar.ObtenerFila()))
            print("Columna: " + str(auxiliar.ObtenerColumna()))
            auxiliar = auxiliar.Siguiente
            
    def buscarMuestra(self, CeldaContrario):
        auxiliar = self.cabeza
        while auxiliar != None:
            fila = auxiliar.ObtenerFila()
            columna = auxiliar.ObtenerColumna()
            
            if CeldaContrario.BuscarPosicion(fila+1, columna+1):
                print("Auxiliar en:\nFila: "+str(auxiliar.ObtenerFila())+ " Columna: " + str(auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+1)+" Columna: "+str(columna+1))
            auxiliar = auxiliar.Siguiente
            
    def BuscarPosicion(self, fila, columna):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.ObtenerFila() == fila and auxiliar.ObtenerColumna() == columna:
                return True
            auxiliar = auxiliar.Siguiente
        return False
 
    def eliminarMuestra(self, codigo):
        if self.primero is None:
            return False
        elif self.primero.muestra.codigo == codigo:
            self.primero = self.primero.siguiente
            return True
        else:
            actual = self.primero
            while actual.siguiente is not None:
                if actual.siguiente.muestra.codigo == codigo:
                    actual.siguiente = actual.siguiente.siguiente
                    return True
                actual = actual.siguiente
            return False'''
    
