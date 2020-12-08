#opción 1
while True:
    t=int(input("Ingrese la altura de la pirámide: "))
    if t>0 and t<=8:
        for i in range (t):
            print (" "*(t-(i+1))+"#"*(i+1))
        break
    else: 
        print ("Valor inválido")
#opción 2
while True:
    t=int(input("Ingrese la altura de la pirámide: "))
    if t>0 and t<=8:
        for i in range (t):
            print (('#'*t).replace('#',' ',t-(i+1)))
        break
    else: 
        print ("Valor inválido")
