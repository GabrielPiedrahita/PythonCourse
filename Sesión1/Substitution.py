import sys
arg=sys.argv

def substituir(vl_plaint,vl_clave):
    vl_ciphert=""
    asccii_min=97
    asccii_may=65
    indice=0
    for i in vl_plaint:
        char_plaint=i
        asccii_plaint=ord(char_plaint)
        if (asccii_plaint>=65 and asccii_plaint<=90) or (asccii_plaint>=97 and asccii_plaint<=122):
            if asccii_plaint<97:
                #mayúscula
                char_replace=vl_clave[asccii_plaint-asccii_may]
                if ord(char_replace)>90:
                    char_replace=char_replace.upper()
            else:
                #minúscula
                char_replace=vl_clave[asccii_plaint-asccii_min]
                if ord(char_replace)<97:
                    char_replace=char_replace.lower()
            vl_ciphert=vl_ciphert[:indice] + char_replace + vl_ciphert[indice:] #vl_ciphert.replace(char_plaint,char_replace)
            indice+=1
    return vl_ciphert

def substituirV2(vl_plaint,vl_clave):
    diccionario = {}
    i=0
    vl_ciphert=""
    for indice in range(0, 25):
        diccionario[i+65]=vl_clave[indice]
        diccionario[i+97]=vl_clave[indice]
        i+=1
    for i in vl_plaint:
        asccii_plaint=ord(i)
        if asccii_plaint in diccionario:
            vl_ciphert+= diccionario[asccii_plaint]
        else:
            vl_ciphert+=i
    return vl_ciphert

import string
def substituirV3(vl_plaint,vl_clave):
    vl_ciphert=""
    for i in vl_plaint:
        if i.isalpha():
            if i.islower():
                vl_ciphert+= vl_clave[string.ascii_lowercase.index(i)].lower()
            else:
                vl_ciphert+= vl_clave[string.ascii_uppercase.index(i)]
        else:
            vl_ciphert+=i
    return vl_ciphert


vl_lebarg=len(arg)

if vl_lebarg==1:
     print('No ha ingresado la clave')
elif vl_lebarg==2:
    vl_clave=arg[1]
    vl_levclave=len(vl_clave)
    if vl_levclave==26:
        vl_plaint = input("Plain text:")
        vl_ciphert = substituirV3(vl_plaint,arg[1])
        print(vl_ciphert)
    else:
        print('Clave inválida. No contiene la longitud requerida')  
else:
    print('Ha ingresado demasiados parámetros')

