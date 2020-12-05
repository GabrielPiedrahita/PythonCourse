#Problema1
vl_kil = input("Ingrese la cantidad de Kilómetros recorridos: ")
vl_lit = input("Ingrese la cantidad de litros de combustible gastados: ")
vl_res=float(vl_kil)/float(vl_lit)
print("El consumo por kilómetro es de ", vl_res)

#Problema2
from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática "))
B = int(input("Ingrese el coeficiente de la variable lineal "))
C = int(input("Ingrese el término independiente "))
x1= 0
x2= 0
if A!=0:
    if ((B**2)-4*A*C) < 0:
        print("La ecuación no tiene solución real")
    else:
        x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
        x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
        if x1==0 and x2==0:
            print("Solución: x=%4.3f"%x1)
        else:
            print("Solución: x1=%4.3f y x2=%4.3f"%(x1,x2))
else:
    if B!=0:
        x=-C/B
        print("Solución: x=%4.3f"%x)
    else:
        if C!=0:
            print("La ecuación no tiene solución")
        else:
            print("La ecuación tiene infinitas soluciones")