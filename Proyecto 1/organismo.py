#Clase para organismo y obtener sus datos
class Organismo():
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        
    def ObtenerCodigo(self):
        return self.codigo 
    
    def ObtenerNombre(self): 
        return self.nombre 
    
#Clase Nodo para la clase Organismo
class NodoOrganismo:
    
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.siguiente = None
        
    def ObtenerCodigo(self):
        return self.codigo.ObtenerCodigo()
    
    def ObtenerNombre(self):
        return self.nombre.ObtenerNombre()
    
    def SetFila (self, fila):
        self.Ficha.Fila = fila

    def SetColumna (self, columna):
        self.Ficha.Columna = columna
    
class ColaOrganismo():
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def Imprimir(self):
        auxiliar = self.cabeza
        while auxiliar != None:
            print("Codigo: " + str(auxiliar.ObtenerCodigo()))
            print("Nombre: " + str(auxiliar.ObtenerNombre()))
            auxiliar = auxiliar.siguiente