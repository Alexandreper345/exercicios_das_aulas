class TemperatureConverter():
    def __init__(self,celsius,Fahrenheit):
        self.celsius = celsius
        self.Fahrenheit = Fahrenheit

    def convesor_para_fahrenheit(self):
        return f"seu conversor para fahrenheit {((self.celsius * 9)/5)+32}"
    
    def convesor_para_celsius(self):
        return f"seu conversor para celsius {((self.Fahrenheit - 32 )*5)/9}"
    
temp = TemperatureConverter(30 , 80.6)

print(temp.convesor_para_fahrenheit())
print(temp.convesor_para_celsius())