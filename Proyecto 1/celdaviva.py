#Clase para organismo y obtener sus datos
class CeldaViva:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    #def __str__(self):
        #return f"Celda({self.fila}, {self.columna}): {self.organismo.nombre if self.organismo else 'N/A'} - {'Viva' if self.viva else 'Muerta'}"
    def ObtenerFila(self):
        return self.fila
    
    def ObtenerColumna(self):
        return self.columna
        
class NodoCeldaViva:

    def __init__(self, columna, fila):
        self.Vivo = CeldaViva(fila, columna)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.Vivo.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.Vivo.ObtenerColumna()

    def SetFila(self, fila):
        self.Vivo.fila = fila

    def SetColumna(self, columna):
        self.Vivo.columna = columna


class ColaCeldaViva:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregarMuestra(self, columna, fila):
        nuevonodo = NodoCeldaViva(columna, fila)
        if self.cabeza == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        else:
            self.cola.Siguiente = nuevonodo
            self.cola = nuevonodo
            
            
    def SetLimite(self, fila, columna):
        self.limitevertica = fila    
        self.limitehorizontal = columna
        
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
            
            if CeldaContrario.BuscarPosicion(fila+1, columna-1):
                print("Auxiliar en:\nFila: "+str(auxiliar.ObtenerFila())+ " Columna: " + str(auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+1)+" Columna: "+str(columna-1))
                
                if fila+2 < self.limitevertica and columna-2 >= 0:
                    CeldaContrario.eliminarMuestra((fila+1), (columna-1))
                    self.MoverAuxiliar(auxiliar, fila+2, columna-2)
                self.MoverAuxiliar(auxiliar, fila+2, columna+2)
                auxiliar.SetFila = fila+1
                auxiliar.SetColumna = columna-1
            auxiliar = auxiliar.Siguiente
            
    def BuscarPosicion(self, fila, columna):
        auxiliar = self.cabeza
        while auxiliar != None:
            if auxiliar.ObtenerFila() == fila and auxiliar.ObtenerColumna() == columna:
                return True
            auxiliar = auxiliar.Siguiente
        return False

    def eliminarMuestra(self, fila, columna):
        auxiliar = self.cabeza
        anterior = None
        while auxiliar != None:
            if (auxiliar.ObtenerFila() == fila and auxiliar.ObtenerColumna() == columna):
                if auxiliar == self.cabeza:
                    self.cabeza = auxiliar.Siguiente
                    auxiliar.Siguiente = None
                else:
                    anterior.Siguiente = auxiliar.Siguiente
                    auxiliar.Siguiente = None
                    if (auxiliar == self.cola):
                        self.cola = anterior
                return
            anterior = auxiliar
            auxiliar = auxiliar.Siguiente

    def MoverAuxiliar(self, Vivo, NuevaFila, NuevaColumna):
        Vivo.SetFila(NuevaFila)
        Vivo.SetColumna(NuevaColumna)