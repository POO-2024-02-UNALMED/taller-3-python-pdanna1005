class TV:
    def __init__(self, marca, estado):
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None
        self.marca = marca
        self.estado = estado
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, newMarca):
        self.marca = newMarca
    
    def getCanal(self):
        return self.canal
    
    def setCanal(self, newCanal):
        if newCanal >= 1 and newCanal <= 120:
            self.canal = newCanal
    
    def getPrecio(self):
        return self.precio 
    
    def setPrecio(self, newPrecio):
        self.precio = newPrecio 
    
    def getVolumen(self):
        return self.volumen 
    
    def setVolumen(self, newVolumen):
        if newVolumen >= 0 and newVolumen <= 7:
            self.volumen = newVolumen 
    
    def getControl(self):
        return self.control
    
    def setControl(self, newControl):
        self.control = newControl 
    
    @classmethod
    def getNumTV(cls):
        return TV.numTV
    
    @classmethod
    def setNumTV(cls, newNumTV):
        TV.numTV = newNumTV 
    
    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False 
    
    def getEstado(self):
        return self.estado 
    
    def canalUp(self):
        if self.canal < 120 and self.estado == True:
            self.canal = self.canal + 1
    
    def canalDown(self):
        if self.canal > 1 and self.estado == True:
            self.canal = self.canal - 1
    
    def volumenUp(self):
        if self.volumen < 7 and self.estado == True:
            self.volumen = self.volumen + 1
    
    def volumenDown(self):
        if self.estado == True and self.volumen > 0:
            self.volumen = self.volumen - 1
    