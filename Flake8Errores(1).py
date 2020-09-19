import numpy as np
# F401 'numpy as np' imported but unused

x= input("Ingrese un número entero para determinar si es par o impar:")
# E225 missing whitespace around operator

if x % 2 == 0:   
    # W291 trailing whitespace
    print("El número que usted ha ingresado es un número par")
else:
    print("El número que usted ha ingresado es un número impar")