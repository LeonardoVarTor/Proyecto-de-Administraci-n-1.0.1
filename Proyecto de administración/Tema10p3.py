print("Tema 10.3: Inferencias concernientes a la diferencia entre medias usando 2 muestras independientes")
print("Mira, creo que esto ya no lo voy a explicar por lo que solo te daré la prueba de hipótesis y el intervalo de confainza, vale? ")
print("Intervalo de confianza = 1 y Prueba de hipótesis = 2")
r = int(input("Qué cosa quiere calcular? "))
if r == 1:
    x1 = float(input("Introduce el valor de x1: "))
    x2 = float(input("Introduce el valor de x2: "))
    alfa = float(input("Introduce el valor de alfa: "))
    s1 = float(input("Introduce el valor de s1: "))
    s2 = float(input("Introduce el valor de s2: "))
    n1 = int(input("Introduce el valor de n1: "))
    n2 = int(input("Introduce el valor de n2: "))
    if n2>n1:
        m = x1-x2
        mm = abs(m)
        gl = n1-1
        import scipy.stats
        t = scipy.stats.t.ppf(q=(alfa/2), df=gl)
        tt = abs(t)
        e1 = (s1**2)/n1
        e2 = (s2**2)/n2
        e = (e1+e2)**0.5
        Inmas = mm + (tt*e)
        Inmen = mm - (tt*e)
        print("El intervalo de confianza es desde ",Inmen, "a", Inmas)
    else:
        m = x1 - x2
        mm = abs(m)
        gl = n2 - 1
        import scipy.stats
        t = scipy.stats.t.ppf(q=(alfa / 2), df=gl)
        tt = abs(t)
        e1 = (s1**2)/n1
        e2 = (s2**2)/n2
        e = (e1+e2)**0.5
        Inmas = mm + (tt*e)
        Inmen = mm - (tt*e)
        print("El intervalo de confianza es desde ",Inmen, "a", Inmas)
elif r == 2:
    re = int(input("Es una situación de 1 o 2 colas? "))
    if re == 1:
        x1 = float(input("Introduce el valor de x1: "))
        x2 = float(input("Introduce el valor de x2: "))
        m1 = float(input("Introduce el valor de m1: "))
        m2 = float(input("Introduce el valor de m2: "))
        s1 = float(input("Introduce el valor de s1: "))
        s2 = float(input("Introduce el valor de s2: "))
        n1 = int(input("Introduce el valor de n1: "))
        n2 = int(input("Introduce el valor de n2: "))
        alfa = float(input("Introduce el valor de alfa: "))
        xx = x1 - x2
        x = abs(xx)
        mm = m1 - m2
        m = abs(mm)
        que = (s1 ** 2) / n1
        so = (s2 ** 2) / n2
        queso = (que + so) ** 0.5
        te = (x - m) / queso
        if n2 > n1:
            gl = n1 - 1
            from scipy import stats

            p = 1 - stats.t.cdf(x=te, df=gl)
            p = 1 - stats.t.cdf(x=te, df=gl)
            print("EL valor de p es: ", p)
            if p > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            gl = n2 - 1
            from scipy import stats

            p = 1 - stats.t.cdf(x=te, df=gl)
            p = 1 - stats.t.cdf(x=te, df=gl)
            print("EL valor de p es: ", p)
            if p > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    elif re == 2:
        x1 = float(input("Introduce el valor de x1: "))
        x2 = float(input("Introduce el valor de x2: "))
        m1 = float(input("Introduce el valor de m1: "))
        m2 = float(input("Introduce el valor de m2: "))
        s1 = float(input("Introduce el valor de s1: "))
        s2 = float(input("Introduce el valor de s2: "))
        n1 = int(input("Introduce el valor de n1: "))
        n2 = int(input("Introduce el valor de n2: "))
        alfa = float(input("Introduce el valor de alfa: "))
        xx = x1 - x2
        x = abs(xx)
        mm = m1 - m2
        m = abs(mm)
        que = (s1 ** 2) / n1
        so = (s2 ** 2) / n2
        queso = (que + so) ** 0.5
        te = (x - m) / queso
        if n2 > n1:
            gl = n1 - 1
            from scipy import stats

            p = 1 - stats.t.cdf(x=te, df=gl)
            p = 1 - stats.t.cdf(x=te, df=gl)
            juan = 2*p
            print("EL valor de p es: ", juan)
            if juan > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            gl = n2 - 1
            from scipy import stats

            p = 1 - stats.t.cdf(x=te, df=gl)
            p = 1 - stats.t.cdf(x=te, df=gl)
            pp = 2*p
            print("EL valor de p es: ", pp)
            if pp > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
else:
    print("Qué hora es?")
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema10p3