import sys
# x = input ('x: ')
# y = input ('y: ')

# print (f'{x} / {y} = {x/y}')

try:
    x = int (input ('x: '))
    y = int (input ('y: '))
except ValueError:
    print ('Error de valor')
    sys.exit(1)

try:
    resultado = x / y
except ZeroDivisionError:
    print('Error al dividir por 0')
    sys.exit(1)

print (f'{x} / {y} = {resultado}')