import array as arr

def basic_ops(op, na, nb):
    if op == '1':
        print(na, "+", nb, "=", suma(na, nb))
        return(suma(na,nb))
        x = 1

    elif op == '2':           
        print(na, "-", nb, "=", resta(na, nb))
        return(resta(na, nb))
        x = 1
        
    elif op == '3':
        print(na, "AND", nb, "=", AND(na, nb))
        return(AND(na, nb))
        x = 1

    elif op == '4':
        print(na, "OR", nb, "=", OR(na, nb))
        return(OR(na, nb))
        x = 1


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b


def array_ops(Array1, Array2, OpSelector):  #argumentos de entrada: los dos arreglos y el numero de operacion
    OutArray=arr.array('i',[])    #define el arreglo de salida
    n=0

    if len(Array1)!=len(Array2):   #compara el tamaño de los arrays, si no son iguales, termina la funcion
        print('ERROR: Arreglos no son del mismo tamaño')
        return 0
    else:
        while n<len(Array1):   #inicia el ciclo para obtener los números de los arreglos
            if ((Array1[n]<128)and(Array1[n]>-128))and((Array2[n]<128)or(Array2[n]>-128)):    #comprueba que los números estén dentro de los límites
                y=basic_ops(OpSelector,int(Array1[n]),int(Array2[n]))    #llama la función de basic_ops y guarda su resultado en la variable y
                OutArray.append(y)   #agrega y al arreglo de salida
                n+=1    #suma 1 al iterador para continuar el ciclo
            else:
                print('ERROR: El número no puede ser mayor a 127 ni menor a -127')
                OutArray=0
                break
        return OutArray


print("Escoja una operación a realizar.")

print("1.Suma")
print("2.Resta")
print("3.AND")
print("4.OR")

x = 0
while (x == 0):

    operacion = input("Número de operación: ")
          
    if operacion in ('1', '2'):
        numa = float(input("Ingrese el primer número: "))
        numb = float(input("Ingrese el segundo número: "))

        if numa > 127 or numa < -127 or numb > 127 or numb < -127:
            print("Error: Los números utilizados se encuentran fuera del rango aceptable. Utilice números mayores a -127 y menores a 127")

        else:
            if operacion == '1':
                print(basic_ops(operacion, numa, numb))
                x = 1
                break
            elif operacion == '2':
                print(basic_ops(operacion, numa, numb))
                x = 1
                break
            else:
                print("Error")
                break


    elif operacion in ('3', '4'):
        numa = int(input("Ingrese el primer número: "))
        numb = int(input("Ingrese el segundo número: "))

        if numa > 127 or numa < -127 or numb > 127 or numb < -127:
            print("Error: Los números utilizados se encuentran fuera del rango aceptable. Utilice números mayores a -127 y menores a 127")

        else:
            if operacion == '3':
                print(basic_ops(operacion, numa, numb))
                x = 1
                break
            elif operacion == '4':
                print(basic_ops(operacion, numa, numb))
                x = 1
                break
            else:
                print("Error")
                break
    else:
        print("Este no es un típo de operación válido, ingrese un valor válido.")
        operacion = input("Número de operación: ")


        
        
print("OPERACIONES CON ARREGLOS")
print("Escoja una operación a realizar.")

print("1.Suma")
print("2.Resta")
print("3.AND")
print("4.OR")
choice = input("Número de operación: ")
    
if (choice!='1')and(choice!='1')and(choice!='1')and(choice!='1'):
    print('Este no es un típo de operación válido, ingrese un valor válido.')
choice = input("Número de operación: ")

Array1=arr.array('i',[])
Array2=arr.array('i',[])
cant1= input("Ingrese el número de elementos del primer arreglo: ")
print('Ingrese los números del arreglo:')
for i in range(int(cant1)):
    n1=int(input('Número:'))
    Array1.append(int(n1))

    
cant2= input("Ingrese el número de elementos del segundo arreglo: ")
print('Ingrese los números del arreglo:')
for i in range(int(cant2)):
    n2=int(input('Número:'))
    Array2.append(int(n2))
    
    

array_ops(Array1,Array2,choice)

