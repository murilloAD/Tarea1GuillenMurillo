import array as arr
import ipytest
ipytest.autoconfig()


def basic_ops(op, na, nb):
    if ((na < 128) and (na > -128)) and ((nb < 128) and (nb > -128)):
        if op == 1:
            return na + nb

        elif op == 2:
            return na - nb

        elif op == 3:
            return na & nb

        elif op == 4:
            return na | nb
        else:
            return 'La operación seleccionada no es válida'
    else:
        return 'El número no puede ser mayor a 127 ni menor a -127'    


def array_ops(Array1, Array2, OpSelector):
    OutArray = arr.array('i', [])
    n = 0

    if len(Array1) != len(Array2):
        print('ERROR: Arreglos no son del mismo tamaño')
        return 0
    elif (OpSelector > 4) or (OpSelector < 1):
        return 'La operación seleccionada no es válida'
    else:
        while n < len(Array1):
            if ((Array1[n] < 128) and (Array1[n] > -128)) and ((Array2[n] < 128) and (Array2[n] > -128)):
                y = basic_ops(OpSelector, int(Array1[n]), int(Array2[n]))
                OutArray.append(y)
                n += 1
            else:
                return 'El número no puede ser mayor a 127 ni menor a -127'
        return OutArray

%%run_pytest[clean]

def basicopsumavalor():
    assert basic_ops(1, 10, 5) == 15


def basicoprestavalor():
    assert basic_ops(2, 10, 5) == 5


def basicopandvalor():
    assert basic_ops(3, 10, 5) == 0


def basicoporvalor():
    assert basic_ops(4, 10, 5) == 15


def arrayopsumavalor():
    assert array_ops([70, 8, 24], [22, 0, 50], 1) == [92, 8, 74]


def arrayoprestavalor():
    assert array_ops([70, 8, 24], [22, 0, 50], 2) == [48, 8, -26]


def arrayopandvalor():
    assert array_ops([70, 8, 24], [22, 0, 50], 3) == [6, 0, 16]

def arrayoporvalor():
    assert array_ops([70, 8, 24], [22, 0, 50], 4) == [86, 8, 58]


def rangoerrorbasic():
    assert basic_ops(1, 300, 5) == 'El número no puede ser mayor a 127 ni menor a -127'


def rangoerrorarray():
    assert array_ops([-200, 8, 24], [22, 0, 50], 3) == 'El número no puede ser mayor a 127 ni menor a -127'


def operrorbasic():
    assert basic_ops(0, 4, 5) == 'La operación seleccionada no es válida'


def operrorarray():
    assert array_ops([7, 8, 24], [22, 0, 50], 6) == 'La operación seleccionada no es válida'