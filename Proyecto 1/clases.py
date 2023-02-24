from typing import List

class Organismo():
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        
class Celda:
    def __init__(self, fila, columna, organismo=None):
        self.fila = fila
        self.columna = columna
        self.organismo = organismo
        self.viva = True if organismo else False
    
    def __str__(self):
        return f"Celda({self.fila}, {self.columna}): {self.organismo.nombre if self.organismo else 'N/A'} - {'Viva' if self.viva else 'Muerta'}"
    
    def esta_vacia(self):
        return self.organismo is None
    
    def matar(self):
        self.organismo = None
        self.viva = False
    
    def AsignarOrganismo(self, organismo):
        self.organismo = organismo
        self.viva = True

class Muestra:
    def __init__(self, codigo: str, descripcion: str, filas: int, columnas: int, celdasvivas: List[Celda]):
        self.codigo = codigo
        self.descripcion = descripcion
        self.filas = filas
        self.columnas = columnas
        self.celdasvivas = celdasvivas

    def celdasProsperas(self, organismo: Organismo) -> List[Celda]:
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

    def obtenerCelda(self, fila: int, columna: int) -> Celda:
        for celda in self.celdasvivas:
            if celda.fila == fila and celda.columna == columna:
                return celda
        return Celda(fila, columna)

class NodoMuestra:
    def __init__(self, muestra):
        self.muestra = muestra
        self.siguiente = None

class ListaMuestras:
    def __init__(self):
        self.primero = None
    
    def agregarMuestra(self, muestra):
        nuevonodo = NodoMuestra(muestra)
        if self.primero is None:
            self.primero = nuevonodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevonodo
    
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
            return False
    
    def buscarMuestra(self, codigo):
        actual = self.primero
        while actual is not None:
            if actual.muestra.codigo == codigo:
                return actual.muestra
            actual = actual.siguiente
        return None

class DatosMarte:
    def __init__(self):
        self.organismos = []
        self.muestras = []

    def agregarOrganismo(self, organismo):
        self.organismos.append(organismo)

    def agregarMuestra(self, muestra):
        self.muestras.append(muestra)

    def buscarMuestra(self, codigo):
        for muestra in self.muestras:
            if muestra.codigo == codigo:
                return muestra
        return None
