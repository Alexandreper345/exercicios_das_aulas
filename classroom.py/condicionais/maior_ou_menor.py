n1 = float(input("digite um número: "))
n2 = float(input("digite segundo número: "))
n3 = float(input("digite terceito número: "))

if n1 > n2 and n1 > n3:
    print(f"o {n1} é maior ")
if n1 < n2 and n1 <n3:
    print(f"o {n1} é menor ") 
if n2 > n1 and n2 > n3:
    print(f' o {n2} é maior')
if n2 < n1 and n2 < n3:
    print(f"o {n2} é menor ")
if n3 > n1 and n3 > n2:
    print(f"o {n3} é maior")
else:
    print(f"o {n3} é menor ")