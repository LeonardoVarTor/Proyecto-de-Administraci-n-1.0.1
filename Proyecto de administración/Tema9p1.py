print("Tema 9.1: Inferencias en torno a la media con la desviación estandar desconocida")
print("Sabías que William Gosset estudió matemáticas y química en la Universidad de Oxford y al graduarse ocupó una plaza en la Cervecería Guinness, en Dublín. En 1905, se reunió con Karl Pearson para discutir sus problemsa estadísticos y un año después, con la aprobación de Guinness, fue a trabajar al laboratorio Biométrico de Pearson y bla bla bla, escribió muchos ensayos, bla bla bla, usó el seudónimo de Student, blablabla y así es como aruinó nuestras vidas como estudiantes. FIN")
print("La desviación estándar se ඞtituirá por el valor s y en lugar de calcular el valor z* se calculará el valor t*")
ans = int(input("Ingrese que tema quiere abarcar(Intervalo_de_confianza (1) o Prueba_de_hipótesis(2)): "))
if ans == 1:
    xbarra = float(input("Ingrese el valor de xbarra: "))
    n = int(input("Ingrese el número de muestras: "))
    s = float(input("Introduce el valor s: "))
    alf = float(input("Introduce el valor de alfa(resta 1 - alfa si es necesario): "))
    gl = n - 1
    alfa = alf/2
    import scipy.stats
    a = scipy.stats.t.ppf(q=alfa, df=gl)
    pos = abs(a)
    sn = s / (n**0.5)
    E = pos * sn
    Mme = xbarra - E
    Mma = xbarra + E
    print("El intervalo de confianza va de ", Mme, "a", Mma)
elif ans == 2:
    c =int(input("La situación es de una o 2 colas?(poner 1 o 2): "))
    if c == 1:
        Ha = int(input("Nuestra hipótesis alternativa es mayor o menor(mayor 1/menor 0)?: "))
        if Ha == 0:
            from scipy import stats

            xbarra = float(input("Introduce el valor de xbarra: "))
            mu = float(input("Introduce el valor de la media: "))
            s = float(input("Introduce el valor s: "))
            n = int(input("Introduce el tamaño de la muestra: "))
            alfa = float(input("Introduce el valor de alfa: "))
            gl = n - 1
            te = (xbarra - mu) / (s / n ** 0.5)
            p = 1 - stats.t.cdf(x=te, df=gl)
            if p > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        elif Ha == 1:
            from scipy import stats

            xbarra = float(input("Introduce el valor de xbarra: "))
            mu = float(input("Introduce el valor de la media: "))
            s = float(input("Introduce el valor s: "))
            n = int(input("Introduce el tamaño de la muestra: "))
            alfa = float(input("Introduce el valor de alfa: "))
            gl = n - 1
            te = (xbarra - mu) / (s / n ** 0.5)
            p = 1 - stats.t.cdf(x=te, df=gl)
            pv = 1 - p
            if pv > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Jajajajajajajajjajajajajajjajajjajajajajjajaja, xd")
            import webbrowser
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif c == 2:
        from scipy import stats

        xbarra = float(input("Introduce el valor de xbarra: "))
        mu = float(input("Introduce el valor de la media: "))
        s = float(input("Introduce el valor s: "))
        n = int(input("Introduce el tamaño de la muestra: "))
        alfa = float(input("Introduce el valor de alfa: "))
        gl = n - 1
        te = (xbarra - mu) / (s / n ** 0.5)
        p = 1 - stats.t.cdf(x=te, df=gl)
        pp = 1 - p
        pv = 2 * pp
        if pv > alfa:
            print("Fracasar en rechazar Ho")
            print("No existe suficietne evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Rechazar Ho")
            print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        S = int(input("Do you want to exit(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema9p1
else:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema9p1

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema9p1







