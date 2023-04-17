def nuevoTema (Tema):
    print("\n----", Tema, "---- \n")

if __name__ == "__main__":

    nuevoTema ("operadores ariméticos")
    print ("operador suma, 5+3: ", 5+3)
    print ("operador resta, 10-2:", 10-2)
    print ("operador multiplicación, 3*3:", 3*3)
    print ("operador división, 20/3: ", 20/3)
    print ("operador división entera, 20//3: ", 20//3)
    print ("operador módulo, 20%3: ", 20%3)
    print ("operador cambio de signo, -3:, -3 ")
    print ("operador exponente, 5 ** 5:", 5**5)

    #Este es un comentario de una línea.
    '''Este es un comentario
    de varias líneas 
    jeje'''
    nuevoTema ("operadores lógicos")
    print ("\n--and--\n")
    print ("True and True: ", True and True) #operador lógico and
    print ("True and False: ", True and False) 
    print ("False and True: ", False and True)
    print ("False and False: ", False and False)
    print ("\n---or---\n")
    print ("True or True: ", True or False)
    print ("True or False:", True or False)
    print ("False or True: ", False or True)
    print ("False or False: ", False or False)
    print ("\n---not---\n")
    print ("not True: ", not True)
    print ("not False: ", not False)
    nuevoTema ("operadores de comparación")
    print ("1=1", 1==1)
    print ("2!=3", 2!=3)
    print ("3<5", 3<5)
    print ("4<=4", 4<=4)
    print ("4>2", 4>2)
    print ("5>=1", 5>=1)

    nuevoTema ("Variables")
    variable1 = 10
    _variable2 = 6.2547
    Variable3 = "Pepe"
    nombreVariable=8 #notación de java, que funciona
    nombre_variable = 34.2 #notación python
    print(variable1, _variable2, Variable3, nombreVariable, nombre_variable)

    a, b, c= 5, 10.8, "Hola"
    print(a)
    print (b)
    print (c)

    nuevoTema ("Enteros")

    w=105
    x=12394678932
    y=-59
    z=0b00100111010
    h=0xff
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema ("Flotantes")
    x=12.390
    print(x, type(x))
    y=-3483.20
    print(y, type(y))

    nuevoTema ("Números complejos")
    x=-46j
    y=12+45j
    z=2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema ("Booleanos")
    lis=[5]
    print(lis,"is", bool (lis))

    nuevoTema("Listas")
    a=[10, 20.5, "Python List"]
    print (a)
    print (a[1])
    a[1]="Hola"
    print(a)

    nuevoTema("Tumplas")
    t=(2, "tupla",1+10j)
    print(t)
    print(t[1])
    #t[1]="Hola" #Operación no válida en Tuplas.
    #print(t)

    nuevoTema ("Cadenas")
    cadena1="Esto es una cadena"
    cadena2="Esto también es una cadena"
    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))

    cadenaMultilinea ='''Esto es una cadena
    de varias línea     con tabulares y 
    saltos
    de 
    línea'''
    print(cadenaMultilinea, type(cadenaMultilinea))

    cadena3="hola"*5 #multiplica el texto :o
    print (cadena3)

    nuevoTema ("Sets")

    conjunto={10,20,30,40,10,50}
    print(conjunto)

    nuevoTema ("Diccionarios")
    diccionario ={"nombre": "Michelle",
                "Edad": 25,
                "Teléfono": 2345789}
    print(diccionario)
    print(diccionario["nombre"])


