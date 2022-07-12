print("Tema 10.2: Inferencias concernientes a la diferencia de medias usando 2 muestras dependientes")

print("Sí 2 muestras son dependientes, lso datos se consideran datos apareados (Comparación directa)")
print("Diferencia apareada: d = x1 - x2")
print("Distribución muestral dbarra")
print("En este tipo de distribuciones muestrales vamos a usar la t de Student")
print("Tiene una distribución normal con desviación estándar σd desconocida")
print("Intervalo de confianza para diferencias de medias (Muestras dependientes):")
print("dbarra = Md, Md = Distribución de Student")
print("dbarra +- t(gl,alfa/2)(sd/√n)")
print("Prueba de hipótesis")
print("t* = (dbarra -Md)/(sd/√n")
print("Sí = 1, No = 2")
quest = int(input("Desea continuar? "))
if quest == 1:
    print("Intervalo de confianza = 1, Prueba de hipótesis = 2")
    Pre = int(input("Qué es lo que desea calcular? "))
    if Pre == 1:
        print("Sí = 1, No = 2")
        dat = int(input("El problema tiene todos los datos principales o no tiene los datos principales? "))
        if dat == 1:
            dbarra = float(input("Introduce el valor de dbarra: "))
            sd = float(input("Introduce el valor de sd: "))
            n = int(input("Introduce el número de muestras: "))
            alfa = float(input("Introduce el valor de alfa: "))
            gl = n - 1
            alfa2 = alfa / 2
            import scipy.stats

            a = scipy.stats.t.ppf(q=alfa2, df=gl)
            t = abs(a)
            s = sd / (n ** 0.5)
            E = t * s
            Me = dbarra - E
            Ma = dbarra + E
            print("El intervalo de confianza va de ", Me, "a", Ma)
        elif dat == 2:
            Σd = float(input("Introduce el valor de Σd: "))
            Σd2 = float(input("Introduce el valor de Σd^2: "))
            n = int(input("Introduce el valor de n: "))
            alf = float(input("Introduce el valor de alfa: "))
            gl = n - 1
            alfa = alf / 2
            import scipy.stats

            a = scipy.stats.t.ppf(q=alfa, df=gl)
            t = abs(a)
            sd = ((Σd2 - (((Σd) ** 2) / n)) / gl) ** 0.5
            s = sd / (n ** 0.5)
            E = t * s
            dbarra = Σd / n
            Me = dbarra - E
            Ma = dbarra + E
            print("El intervalo de confianza va de ", Me, "a", Ma)
        else:
            S = int(input("Do you want to exit(Y=1/N=2)? "))
            if S == 1:
                import main
            else:
                import Tema10p2

    elif Pre == 2:
        cola = int(input("La situación es de 1 cola o 2? "))
        if cola == 1:
            from scipy import stats
            dbarra = float(input("Introduce el valor de dbarra: "))
            µd = float(input("Introduce el valor de µd: "))
            sd = float(input("Introduce el valor de Sd: "))
            n = int(input("Introduce el valor de n: "))
            alfa = float(input("Introduce el valor de alfa: "))
            te = (dbarra-µd)/(sd/(n**0.5))
            gl = n-1
            p = 1 - stats.t.cdf(x=te, df=gl)
            print("EL valor de p es: ",p)
            if p > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")

        elif cola == 2:
            from scipy import stats

            dbarra = float(input("Introduce el valor de dbarra: "))
            µd = float(input("Introduce el valor de µd: "))
            sd = float(input("Introduce el valor de Sd: "))
            n = int(input("Introduce el valor de n: "))
            alfa = float(input("Introduce el valor de alfa: "))
            te = (dbarra - µd) / (sd / (n ** 0.5))
            gl = n - 1
            p = 1 - stats.t.cdf(x=te, df=gl)
            pv = 2 * p
            print("El valor de p es: ",pv)
            if pv > alfa:
                print("Fracasar en rechazar Ho")
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Yo sinceramente no creo en el siglo zodiacal")
            import webbrowser
            webbrowser.open_new_tab("https://www.lavanguardia.com/horoscopo/signos-zodiaco-virgo/horoscopo-diario")
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema10p2









    


