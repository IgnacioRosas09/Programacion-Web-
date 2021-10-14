def decora (f):
    def envuelve ():
        print ('Estoy a punto de ejecutar la función')
        f ()
        print ('Terminé de ejecutar la función')
    return envuelve

@decora
def hola ():
    print ('Hola mundo!')

hola ()