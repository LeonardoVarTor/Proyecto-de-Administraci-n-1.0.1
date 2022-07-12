print("Tema 2.3: Medias de tendencia central")
print("Media(media aritmética): La media muestral se representa con xbarra y se encuentra la sumar todos los valores de la variable x y dividir la suma entre el número de dichos valores (el tamao muestral)")
print("Mediana: Valor de todos los datos que ocupan la posición media cuando los datos se clasifican en orden de acuerdo con su tamaño y se represente con x tilde")
print("Moda: Es el valor x que ocurre con más frecuencia")
print("Medio rango: Número exactamente a la mitad entre un dato de valor más bajo, L y un dato más alto, H. Se encuentra al promediar los valores bajos y altos")
print("Media = 1, Mediana = 2, Moda = 3 y Medio Rango = 4")
R = int(input("Qué desea calcular: "))
#Por favor ingrese los datos desde adentro
# Ejemplo para saber poner los datos de una sucesión: [6,3,8,5,3]
if R == 1:
    import numpy
    s = []
    xbarra = numpy.mean(s)
    print("La media de esta muestra es de: ", xbarra)
elif R == 2:
    import statistics
    s = []
    xtilde = statistics.median(s)
    print("La media de esta muestra es de: ", xtilde)
elif R == 3:
    from statistics import multimode
    s = []
    moda = multimode(s)
    print("La moda de la muestra es de: ", moda)
elif R == 4:
    a = float(input("Inserte el primer número de la sucesión: "))
    b = float(input("Inserte el último número de la sucesión: "))
    Mr = (a+b)/2
    print("El medio rango de esta muestra es de: ", Mr)
else:
    S = int(input("Usted quiere regresar? (S=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema2p3
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema2p3

