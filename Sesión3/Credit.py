#1. Import Librerías
import string

#2. Constantes 
Num_Tarjeta= ""

#FUnción recurrente para sumar la cantidad de digitos de un número
def sumar_digitos(num):
    if (num==(num%10)):
        return num
    else:
        return (num%10)+ sumar_digitos(int(num/10))

#3. Funciones
def validar_tar():
    Reverse_Num_Tarjeta = Num_Tarjeta[::-1]
    suma=0
    for i in range(1,len(Reverse_Num_Tarjeta),2):
        suma+=sumar_digitos(int(Reverse_Num_Tarjeta[i])*2)
    for i in range(0,len(Reverse_Num_Tarjeta),2):
        suma+=int(Reverse_Num_Tarjeta[i])
    if (suma%10)==0:
        return True
    else:
        return False

def tipo_tarjeta():
    if Num_Tarjeta.startswith("34") or Num_Tarjeta.startswith("37"):
        return "AMEX"
    elif Num_Tarjeta.startswith("51") or Num_Tarjeta.startswith("52") or Num_Tarjeta.startswith("53") or Num_Tarjeta.startswith("54") or Num_Tarjeta.startswith("55"):
        return "MASTERCARD"
    elif Num_Tarjeta.startswith("4"):
        return "VISA"
    else:
        return "INVALID"
    
#4. Main

if __name__ == "__main__":
    Num_Tarjeta=input("Ingrese el número de la tarjeta: ")
    if validar_tar():
        print(tipo_tarjeta())
    else:
        print("INVALID")
    pass # no realiza ninguna acción