class fijura:
    def __int__(self,largo,ancho,radio,altura):
        self.largo=largo
        self.ancho=ancho
        self.radio=radio
        self.altura=altura

def getLargo(self):
   return self.largo
def setLargo(self,largo):
   self.largo=largo

def getAncho(self):
   return self.ancho
def setAncho(self,ancho):
   self.ancho=ancho

def getRadio(self):
   return self.radio
def setRadio(self,radio):
   self.radio=radio

def getAltura(self):
   return self.altura
def setAltura(self,altura):
   self.altura=altura

def getInfo(self):
   print(f"Largo; {self.getLargo()}, Ancho; {self.getAncho()},Altura; {self.getAltura()},Radio; {self.getRadio()}, ")
      

class rectangulo(fijura):
  def __init__(self,largo,ancho):
    super().__init__(largo,ancho)
    self.largo=largo
    self.ancho=ancho

def getInfo(self):
   print(f"Largo; {self.getLargo()}, Ancho; {self.getAncho()}")

def calcular_area(self):
    return self.largo * self.ancho

class Circulo(fijura):
  def __init__(self,radio):
    super().__init__(radio)
    self.radio=radio
    

def getInfo(self):
   print(f"Radio; {self.getRadio()}")
def calcular_area(self):
     import math
     return math.pi * (self.radio ** 2)

class Triangulo(fijura):
  def __init__(self,altura,ancho):
    super().__init__(altura,ancho)
    self.altura
    self.ancho=ancho

def getInfo(self):
   print(f"Altura; {self.getAltura()}, Ancho; {self.getAncho()}")

def calcular_area(self):
    return (self.ancho * self.altura) / 2