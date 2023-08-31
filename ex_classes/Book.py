class book():
    def __init__(self,title , author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        ano = int(input("qual o ano atual: "))
        return f"o nome do livro é {self.title} quem escreveu foi {self.author} e  { ano - self.year} anos que já foi lançado"
    

bo = book("harry potter", "J. K. Rowling" , 1997)
print(bo.get_age())