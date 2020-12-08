#1. Import Librerías
import string

#2. Constantes MAYUSCULAS
Cantidad_a=0
Lista_a= list()

#3. Funciones
def registrar_nota(notai):
    while True:
        nota=int(input(f"Ingrese la nota {notai}: "))
        if nota>=0 and nota<=10:
            return nota
        else: 
            print ("Nota inválida")

def datos_alumnos():
    for i in range(Cantidad_a):
        Alumno = {
        'Nombre':'',
        'Notas':[0,0,0],
        'Promedio':0
        }
        Alumno['Nombre']=input('Ingrese el nombre del alumno: ')
        Alumno['Notas'][0]=registrar_nota(1)
        Alumno['Notas'][1]=registrar_nota(2)
        Alumno['Notas'][2]=registrar_nota(3)
        Lista_a.append(Alumno)

def apro_repro():
    aprobados=0
    reprobados=0
    avg_total=0
    for i in range(Cantidad_a):
        Alumno=Lista_a[i]
        avg = sum(Alumno['Notas'])/len(Alumno['Notas'])
        Alumno['Promedio']=avg
        avg_total+=avg
        if avg <4:
            reprobados+=1
        else:
            aprobados+=1
    print(f"La cantidad de alumnos aprobados (avg>=4) es {aprobados}, y reprobados es {reprobados}")
    print(f"El promedio de nota del curso total es {avg_total/Cantidad_a}")
        
def Promedio(x):
    return x['Promedio']

def mayor_menor():
    Lista_sort=sorted(Lista_a, key=Promedio)
    print("El alumno con el promedio más alto fue: " + Lista_sort[-1]['Nombre'])
    print("El alumno con el promedio más bajo fue: " + Lista_sort[0]['Nombre'])

def buscar():
    texto_buscar=input('Ingrese el nombre del alumno a buscar o parte de su nombre: ')
    busqueda=list([alumno for alumno in Lista_a if alumno['Nombre'].upper().find(texto_buscar.upper())>=0])
    if len(busqueda)>0:
        print("La lista de coincidencias es:")
        print(busqueda)
    else:
        print("No hay coincidencias")

#4. Main

if __name__ == "__main__":

    Cantidad_a=int(input('Ingrese la cantidad de alumnos del curso: '))
    print("\n1. Registro de datos de los alumnos")
    datos_alumnos()
    print("\n2. Alumnos aprobados y reprobados")
    apro_repro()
    print("\n3. Alumnos mayor y menor promedio")
    mayor_menor()
    print("\n4. Buscar alumnos")
    buscar()
    pass # no realiza ninguna acción