class Control:
    def __init__(self):
        self.tv = tv 
    
    def turnOn(self):
        tv.turnOn()
    
    def turnOff(self):
        tv.turnOff()
    
    def canalUp(self):
        tv.canalUp()
    
    def canalDown(self):
        tv.canalDown()
    
    def volumenUp(self):
        tv.volumenUp()
    
    def volumenDown(self):
        tv.volumenDown()
    
    def setCanal(self, newCanal):
        tv.setCanal(newCanal)
    
    def setVolumen(self, newVolumen):
        tv.setVolumen(newVolumen)
    
    def enlazar(self, tvHost):
        self.tv = tvHost
        tvHost.setControl(self)
    
    def getTV(self):
        return self.tv
    
    def setTV(self, newTV):
        self.tv = newTV