class Employee():
    def __init__(self,name,position , salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def apply_raise(self):
        porcento = int(input("quanto % você quer de aumento: "))
        return f"o aumento do salario do funcionario é de {self.salary + ((self.salary * porcento)/100)}"
    
funci = Employee('ale' , "publico", 1500)

print(funci.apply_raise())