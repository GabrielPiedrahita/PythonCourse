import sys
import string

def Caesar(vl_plaint,vl_clave):
    vl_ciphert=""
    for letra in vl_plaint:
        if letra.isalpha():
            if letra.islower():
                vl_ciphert+= string.ascii_lowercase[(string.ascii_lowercase.index(letra)+vl_clave)%26]
            else:
                vl_ciphert+= string.ascii_uppercase[(string.ascii_uppercase.index(letra)+vl_clave)%26]
        else:
            vl_ciphert+=letra
    return vl_ciphert

arg=sys.argv
vl_lebarg=len(arg)

if vl_lebarg==1:
     print('No ha ingresado la clave')
elif vl_lebarg==2:
    vl_clave=int(arg[1])
    vl_plaint = input("Plain text:")
    vl_ciphert = Caesar(vl_plaint,vl_clave)
    print(vl_ciphert)
else:
    print('Ha ingresado demasiados parámetros')
