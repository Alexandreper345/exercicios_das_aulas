class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_ifo (self):
        return f"o nome da pessoa {self.name} e a sua idade é {self.age} anos"
    

per = Person('alexandre' , '18')

print(per.display_ifo())