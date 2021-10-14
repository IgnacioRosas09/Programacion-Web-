libros = [
    {'Titulo': 'El principito', 'Año': 1943 },
    {'Titulo': 'El arte de la guerra', 'Año': 1772 },
    {'Titulo': 'La ciudad de las vestias', 'Año': 2002 },
    {'Titulo': 'El Hobbit', 'Año': 1984 },
    {'Titulo': 'La grieta', 'Año': 2007 }
]

# libros.sort()
# No podemos comparar objetos sin decir algo más sobre ellos
# libros.sort(key = 'Año')
# Sort 

def ftitulo (libro):
    return (libro) ['Titulo'].upper()
def fanio (libro):
    return libro ['Año']

# print (ftitulo(libros[0]))
# print (fanio(libros[0]))

print (libros)
print ()

# print ('Libros ordenados por año: ')
# libros.sort(key = fanio)
# print (libros)

# print ('Libros ordenados por título: ')
# libros.sort(key = ftitulo)
# print (libros)

libros.sort(key = lambda libro:libro ['Año'])
for libro in libros:
    print (f"El libro {libro ['Titulo']} fue publicado en {libro ['Año']}")
# print (libros)

libros.sort(key = lambda libro:libro ['Titulo'])



# print (libros)