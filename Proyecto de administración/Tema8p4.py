print("Tema 8.4: Prueba de hipótesis de la media con la desviación estándar conocida")
resp = int(input("El problema es de 1 o 2 colas?(1 cola = 1/2 colas = 2): "))
if resp == 1:
    Ha = int(input("Nuestra hipótesis alternativa es mayor o menor(mayor 1/menor 0)?: "))
    if Ha == 0:
        import scipy.stats as st
        n = int(input("Introduce el número de muestras: "))
        xbarra = float(input("Introduce el valor de xbarra: "))
        media = float(input("Introduce el valor de la media: "))
        desv = float(input("Introduce el valor de la desviación estándar: "))
        alfa = float(input("Introduce el valor de alfa(resta 1- alfa si es necesario): "))
        ze = (xbarra - media) / (desv / n ** 0.5)
        p = st.norm.cdf(ze)
        print("El valor z* es de", p)
        if p > alfa:
            print("Fracasar en rechazar Ho: ", p)
            print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Rechazar Ho")
            print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    elif Ha == 1:
        import scipy.stats as st

        n = int(input("Introduce el número de muestras: "))
        xbarra = float(input("Introduce el valor de xbarra: "))
        media = float(input("Introduce el valor de la media: "))
        desv = float(input("Introduce el valor de la desviación estandar: "))
        alfa = float(input("Introduce el valor de alfa(resta 1- alfa si es necesario): "))
        ze = (xbarra - media) / (desv / n ** 0.5)
        p = st.norm.cdf(ze)
        pv = 1 - p
        print("El valor z* es de", p)
        if pv > alfa:
            print("Fracasar en rechazar Ho: ", p)
            print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Rechazar Ho")
            print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        print("Buenas :D")
elif resp == 2:
    import scipy.stats as st
    n = int(input("Introduce el número de muestras: "))
    xbarra = float(input("Introduce el valor de xbarra: "))
    media = float(input("Introduce el valor de la media: "))
    desv = float(input("Introduce el valor de la desviación estandar: "))
    alfa = float(input("Introduce el valor de alfa(resta 1 - alfa si es necesario): "))
    ze = (xbarra - media) / (desv / n ** 0.5)
    p1 = st.norm.cdf(ze)
    p = p1*2
    print("El valor z* es de", p)
    if p > alfa:
        print("Fracasar en rechazar Ho: ", p)
        print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        print("Rechazar Ho")
        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
else:
    print("Adiós :P")

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema8p4

