num1 = float(input("qual o numero: "))
num2 = float(input("qual o numero: "))
num3 = float(input("qual o numero: "))

if num1 > num2 > num3:
    print(f"o {num1} é maior")
elif num2>num3>num1:
    print(f"o {num2} é maior")
else:
    print(f"o {num3} é maior")
