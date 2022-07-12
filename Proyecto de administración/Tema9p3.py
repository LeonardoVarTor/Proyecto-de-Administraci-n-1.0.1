print("Tema 9.3: Inferencias en torno a la varianza y la desviación estándar")
print("Las inferencias en torno a la varianza de una población con distribución normal usan las distribuciones ji/chi cuadrada (X^2 es la letra minúscula ji)")

print("Propiedades de la distribución ji cuadrada")
print("1. X^2 es no negativa en valor; es 0 con valor positivo")
print("2. X^2 no es simétrica; está sesgada a la derecha")
print("3. X^2 está distribuida de modo que forma una familia de distribuciones, una distribución separada para cada diferente número de grados de libertad")

print("Las suposiciones para inferencias acerca de la varianza σ^2 o desviación estándar σ. La población muestreada tiene distribución normal")
print("Recuerda: Si te ponen desviación estándar esos datos los elevas al cuadrado para sacar la varianza")
print("Calcular x^2 = 1 o Calcular la prueba de hipótesis = 2")
Ra = int(input("Qué de sea calcular? "))
if Ra == 1:
    a = int(input("El área es de 1 o 2 colas? "))
    if a == 1:
        print("Asociada con la cola izquierda = 1 o Asociada con la cola derecha = 2")
        c = int(input("Por cuál lado está asociada la cola? "))
        if c == 1:
            gl = float(input("Introduce los grados de libertad: "))
            área = float(input("Introduce el área: "))
            from scipy.stats import chi2
            critical = chi2.ppf(área, gl)
            print("El valor de X^2 es: ", critical)
        elif c == 2:
            gl = float(input("Introduce los grados de libertad: "))
            área = float(input("Introduce el área: "))
            arr = 1 - área
            from scipy.stats import chi2
            critical = chi2.ppf(arr, gl)
            print("El valor de X^2 es: ", critical)
        else:
            S = int(input("Do you want to exit(Y=1/N=2)? "))
            if S == 1:
                import main
            else:
                import Tema9p3
    elif a == 2:
        gl = float(input("Introduce los grados de libertad: "))
        área = float(input("Introduce el área: "))
        from scipy.stats import chi2
        critical1 = chi2.ppf(área/2, gl)
        arr = 1 - área/2
        critical2 = chi2.ppf(arr, gl)
        print("Los valores de X^2 son de", critical1, "y", critical2)
    else:
        S = int(input("Do you want to exit(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema9p3

elif Ra == 2:
    c = int(input("La situación es de 1 o 2 colas? "))
    if c == 1:
        print("Mayor = 1, Menor = 2")
        h = int(input("La hipótesis alternativa es mayor o menor? "))
        if h == 1:
            n = int(input("Introduce el valor n: "))
            s2 = float(input("Introduce el valor s^2: "))
            σ2 = float(input("Introduce el valor σ^2: "))
            alfa = float(input("Introduce el nivel de significancia: "))
            gl = n-1
            x2e = (gl*s2)/σ2
            from scipy.stats.distributions import chi2
            p = chi2.sf(x2e, gl)
            print("El valor p es", p)
            if p > alfa:
                print("Fracasar en rechazar Ho: ", p)
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        elif h == 2:
            n = int(input("Introduce el valor n: "))
            s2 = float(input("Introduce el valor s^2: "))
            σ2 = float(input("Introduce el valor σ^2: "))
            alfa = float(input("Introduce el nivel de significancia: "))
            gl = n - 1
            x2e = (gl * s2) / σ2
            from scipy.stats.distributions import chi2
            pp = chi2.sf(x2e, gl)
            p = 1-pp
            print("El valor p es", p)
            if p > alfa:
                print("Fracasar en rechazar Ho: ", p)
                print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Veo que ya tienes X^2 en el problema")
            c = int(input("La situación es de 1 o 2 colas? "))
            if c == 1:
                print("Mayor = 1, Menor = 2")
                h = int(input("La hipótesis alternativa es mayor o menor? "))
                if h == 1:
                    n = int(input("Introduce el valor n: "))
                    x2 = float(input("Introduce el valor de X^2 estrella: "))
                    alfa = float(input("Introduce el nivel de significancia: "))
                    gl = n - 1
                    from scipy.stats.distributions import chi2

                    p = chi2.sf(x2, gl)
                    print("El valor p es", p)
                    if p > alfa:
                        print("Fracasar en rechazar Ho: ", p)
                        print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
                    else:
                        print("Rechazar Ho")
                        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
                elif h == 2:
                    n = int(input("Introduce el valor n: "))
                    x2 = float(input("Introduce el valor de X^2 estrella: "))
                    alfa = float(input("Introduce el nivel de significancia: "))
                    gl = n - 1
                    from scipy.stats.distributions import chi2

                    pp = chi2.sf(x2, gl)
                    p = 1 - pp
                    print("El valor p es", p)
                    if p > alfa:
                        print("Fracasar en rechazar Ho: ", p)
                        print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
                    else:
                        print("Rechazar Ho")
                        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
                else:
                    print("Todos se divierten y juegan y tienen buenas calificaciones, por mi parte no juego ni me divierto y tengo malas calificaciones, por qué?")
            elif c == 2:
                n = int(input("Introduce el valor n: "))
                x2 = float(input("Introduce el valor de X^2 estrella: "))
                alfa = float(input("Introduce el nivel de significancia: "))
                gl = n - 1
                from scipy.stats.distributions import chi2
                p = chi2.sf(x2, gl)
                pe = 2 * p
                print("El valor p es", pe)
                if pe > alfa:
                    print("Fracasar en rechazar Ho")
                    print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
                else:
                    print("Rechazar Ho")
                    print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")

    elif c == 2:
        print("Recuerda: Si te ponen desviación estándar esos datos los elevas al cuadrado para sacar la varianza")
        n = int(input("Introduce el valor n: "))
        s2 = float(input("Introduce el valor s^2: "))
        σ2 = float(input("Introduce el valor σ^2: "))
        alfa = float(input("Introduce el nivel de significancia: "))
        gl = n - 1
        x2e = (gl * s2) / σ2
        from scipy.stats.distributions import chi2

        pp = chi2.sf(x2e, gl)
        p = 2 * pp
        if p > alfa:
            print("Fracasar en rechazar Ho: ", p)
            print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Rechazar Ho", p)
            print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        print("Por qué?")
else:
    print("Por favor, ingresa correctamente lo que se te pide. Ya no puedo  soportarlo más")
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema9p3










    



