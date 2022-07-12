#Prueba de hipótesis con el valor p
sus = int(input("La situación es de una o de dos colas? :) "))
if sus == 1:
    x = float(input("Introducir el valor x: "))
    n = int(input("Introducir el número de muestras: "))
    pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
    alfa = float(input("Introduce el valor de alfa: "))
    p = x/n
    q = 1-p
    z = (p-pp)/((p*q)/n)**2
    from scipy.special import ndtri
    p = ndtri(z)
    if p > alfa:
        print("Fracasar en rechazar Ho: ", p)
    else:
        print("Rechazar Ho")
elif sus == 2:
    x = float(input("Introducir el valor x: "))
    n = int(input("Introducir el número de muestras: "))
    pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
    alfa = float(input("Introduce el valor de alfa: "))
    p = x / n
    q = 1 - p
    z = (p - pp) / ((p * q) / n) ** 2
    from scipy.special import ndtri
    p = ndtri(z)
    pv = 2*p
    if pv > alfa:
        print("Fracasar en rechazar Ho: ", p)
    else:
        print("Rechazar Ho")
else:
    print(">:(")
#Método clásico, que es eso, tu puedes hacer una gráfica

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema8p5





