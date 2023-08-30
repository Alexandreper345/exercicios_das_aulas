l1 =  float(input("qual o l1: "))
l2 = float(input("qual o l2: "))
l3 = float(input("qual o l3: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("pode forma um triangulo")
else:
    print("nao pode forma triangulo")