class CPF:
    value = ''

    def __init__(self,param: str):
        self.value = param

    def validate(self) -> bool:
        return True

cpf = CPF('xxxxxxxxxx')
print(cpf.value)
