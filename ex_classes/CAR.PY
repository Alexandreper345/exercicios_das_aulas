class Car ():
    def __init__ (self,make ,model , year):
        self.make = make
        self.model = model
        self.year = year

    def  start_engine (self):
        return f"a marca do seu carro é {self.make}, o modelo do seu carro {self.model} do ano {self.year} e o seu o motor foi iniciado "
    
    @property
    def abelha(self):
        return self._make

    @abelha.setter
    def abelha(self , make):
        self._make = make

ca = Car('abelha' , 'bzzzz', 2003)

print(ca.start_engine())