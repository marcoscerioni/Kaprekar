# Colores para imprimir en la terminal.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Verifica si todos los dígitos son iguales.
def allEqual(n):
    s = str(n)
    if len(set(s)) == 1:
        return True
    else:
        return False


# Da el máximo valor de un número dado.
def max_number(n):
    s = str(n)
    digits = sorted(s, reverse=n > 0)
    return int(''.join(digits))


# Da el mínimo valor de un número dado.
def min_number(n):
    s = str(n)
    digits = sorted(s)
    return int(''.join(digits))


# Agrega 0 a una lista
def addZero(n):
    s = str(n)
    digits = sorted(s)
    digits.append('0')
    return int(''.join(digits))

count = 1
while count:
    number = input(bcolors.OKGREEN + "Ingrese un número de 4 dígitos,"
                                        "que no sean los 4 iguales: ")
    try:
        number = int(number)
        isInt = 1
    except:
        isInt = 0
    if isInt and len(str(number)) == 4 and not allEqual(number):
        count = 0
    else:
        count = 1
        print(bcolors.OKBLUE + "Número incorrecto. ")

print(bcolors.HEADER + bcolors.BOLD + "Elegiste el número: ", str(number))

new_number = number
pasos = 0
print("\nPasos    Máximo número     Mínimo número    Resultado Resta")

while (new_number != 6174):
    if len(str(new_number)) < 4:
        new_number = addZero(new_number)
    new_number = max_number(new_number) - min_number(new_number)
    pasos += 1
    print(pasos, "          ", max_number(new_number), "            ",
    min_number(new_number), "           ", new_number)

print("\nSe necesitaron ", pasos,  " pasos para resolverlo")
