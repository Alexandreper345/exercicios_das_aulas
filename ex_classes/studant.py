class Student():
    def __init__(self,name,age,grade = []): 
     self.name = name
     self.age = age
     self.grades = grade

    def caculate_media(self):
        lista = []
        for _ in self.grades:
            num = float(input("qual a suas notas: "))
            lista.append(num)
        return f"seu nome é {self.name}, sua idade é {self.age} anos e sua média é de {sum(lista) / len(self.grades)}"
    

lista = ["p" , "h"]
stand = Student('alexandre' , '18' , lista)
print(stand.caculate_media())    



#@property

#@funçao.setter
#@classmethod
#@cls