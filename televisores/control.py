class Control:
    def __init__(self):
        self.tv = None
    
    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()
    
    def canalDown(self):
        self.tv.canalDown()
    
    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()
    
    def setCanal(self, newCanal):
        self.tv.setCanal(newCanal)
    
    def setVolumen(self, newVolumen):
        self.tv.setVolumen(newVolumen)
    
    def enlazar(self, tvHost):
        self.tv = tvHost
        tvHost.setControl(self)
    
    def getTv(self):
        return self.tv
    
    def setTv(self, newTV):
        self.tv = newTV