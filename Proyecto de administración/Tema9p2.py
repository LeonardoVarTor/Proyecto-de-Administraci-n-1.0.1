print("Tema 9.2: Inferencias entorno a la probabilidad binomial de éxito")
rasputin = int(input("Cuál tema quieres saber?(intervalo de confianza para p(1),tamaño de la muestra para estimar p sin información previa(2),tamaño de la muestra para estimar p con información previa(3) o el Estadístico de Prueba(4)): "))
if rasputin == 1:
    # intervalo de confianza para p
    pera = int(input("Se tiene el valor p?(Sí(1)/No(2)): "))
    if pera == 1:
        p = float(input("Introduce dell valor p: "))
        q = 1 - p
        n = int(input("Introduce el número de muestras: "))
        alfa = float(input("Introduce el valor de alfa: "))
        from scipy.special import ndtri
        za = (alfa) / 2
        z = ndtri(za)
        lafldsmdfr = ((p * q) / n) ** 0.5
        E = (z) * (lafldsmdfr)
        Pme = p - E
        Pemex = p + E
        print("En intervalo de confinaza va desde ", Pme, "a ", Pemex)
    elif pera == 2:
        x = float(input("Introduce el valor x(la cantidad de la muestra que padece diferente a la muestra total): "))
        n = int(input("Introduce el número de muestras: "))
        alfa = float(input("Introduce el valor de alfa: "))
        from scipy.special import ndtri
        p = x / n
        q = 1 - p
        za = (alfa) / 2
        z = ndtri(za)
        lafldsmdfr = ((p * q) / n) ** 0.5
        E = (z) * (lafldsmdfr)
        Pme = p - E
        Pemex = p + E
        print("En intervalo de confinaza va desde ", Pme, "a ", Pemex)
    else:
        print("Esto aqui, y, esto aqui. Perfecto, y aqui tenemos, la Thunder Sword. Que quita... que a pasado? Ha caido, un trueno? A no no no, que es la Thunder Sword esta... escucho fuego, no fastidies que se me quema la casa otra vez. No fastidies, no fastidies, no fastidies. QUE DICES!?! QUE DICES!?! PERO QUE NARICES?!? N-no! Que leches, que quequequequequequeque... nonono, cubo de agua, cubo de agua! Cubo de... Que? Nonononono no no no mi casa! Mi casa! Oi, por dios que esta pasando ultimamente con mis casas! Que- que me muero! Que me muero! Que no, que no! Que se me quema la casa, que se me quema la... Hay por dios que se me to... Hay por dios que se me quema toda la casa. HOY POR DIOS LA-PTFA- ALFOMBRA! ME CAGO EN TODO LO CAGABLE MI- NO HAGAIS UNA ESPADA SWO- Su madre! NOOOOOO, MI CASA TIO!!! Que desaparece, que desaparece mi casa! Que desaparece... Que desparece mi casa! Que desaparece mi casa! No, mi casa! Noo! Mi casa! NUUU! TOO- No fastidies, no fastidies! Nofastidiesnofastidiesnofastidiesnofastidies. Mi casa no, mi casa no, mi casa no! Que dices, quedicesquedicesquedicesquedice- quedice- Noo, va, Nooooo. Nooooo, Nooooooo.")
elif rasputin == 2:
    # tamaño de la muestra para estimar p sin información previa
    from scipy.special import ndtri
    alfa = float(input("Introduce el valor de alfa: "))
    E = float(input("Introduce el valor del error máximo: "))
    p = 0.5
    q = 0.5
    za = (alfa) / 2
    z = ndtri(za)
    np1 = z ** 2
    np2 = p * q
    np3 = E ** 2
    n = (np1 * np2) / np3
    print("El tamaño de la muestra es de ", n)
elif rasputin == 3:
    # tamaño de la muestra para estimar p con información previa
    from scipy.special import ndtri
    alfa = float(input("Introduce el valor de alfa: "))
    E = float(input("Introduce el valor del error máximo: "))
    p = float(input("Introduce el valor p: "))
    q = 1 - p
    za = (alfa) / 2
    z = ndtri(za)
    np1 = z ** 2
    np2 = p * q
    np3 = E ** 2
    n = (np1 * np2) / np3
    print("El tamaño de la muestra es de ", n)
elif rasputin == 4:
    # Prueba de hipótesis con el valor p
    sus = int(input("La situación es de una o de dos colas? :) "))
    if sus == 1:
        Ha = int(input("Nuestra hipótesis alternativa es mayor o menor(mayor 1/menor 0)?: "))
        if Ha == 0:
            x = float(input("Introducir el valor x: "))
            n = int(input("Introducir el número de muestras: "))
            pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
            alfa = float(input("Introduce el valor de alfa: "))
            p = x / n
            q = 1 - p
            z = (p - pp) / (((p * q) / n) ** 0.5)
            print(z)
            import scipy.stats as st
            p = st.norm.cdf(z)
            if p > alfa:
                print("Fracasar en rechazar Ho: ", p)
            else:
                print("Rechazar Ho", p)
        elif Ha == 1:
            x = float(input("Introducir el valor x: "))
            n = int(input("Introducir el número de muestras: "))
            pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
            alfa = float(input("Introduce el valor de alfa: "))
            p = x / n
            q = 1 - p
            z = (p - pp) / ((p * q) / n) ** 0.5
            import scipy.stats as st
            p = st.norm.cdf(z)
            pv= 1-p
            if pv > alfa:
                print("Fracasar en rechazar Ho: ", p)
            else:
                print("Rechazar Ho")
        else:
            import webbrowser
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=9Jow8pV2fBI")
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
        pv = 2 * p
        if pv > alfa:
            print("Fracasar en rechazar Ho: ", p)
        else:
            print("Rechazar Ho")
    else:
        print(">:(")
else:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema9p2

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema9p2