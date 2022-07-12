print("Bienvenido al programa evitador de estres de administración")

print("Existen 8 temas que se pueden seleccionar: Tema 8.1(escribe 8.1), 8.2, 8.3, 8.4, 9.1, 9.2, sz (escribe 2) y TDBTS (escribe 1). Para más información escriba 0")

tema = float(input("Seleccione el tema/comando que desea iniciar: "))
if tema == 0:
    print("Este rpograma existe solo para resolver algunos posibles problemas, si la escuela da tiempos e podrá tomar todos los temas ;D)")
    print("Tienes que escribir solo el número del tema (Ejemplo: 8.1,8.2,8.3)")
    print("Coming soon...")
    print("Tema 8.1: La Naturaleza ded la estimación (Solo media, varianza y desviación estandar)")
    print("Tema 8.2: Estimación de la media con la desviación estandar conocida")
    print("Tema 8.3: La naturaleza de la prueba de hipótesis")
    print("Tema 8.4: Prueba de hipótesis de la media con la desviación estandar conocida")
    print("Tema 9.1: Inferencias en torno a la media con la desviación estandar desconocida")
    print("Tema 9.2: Inferencias entorno a la probabilidad binomial de éxito")
    print("sz: Signo Zodiacal (escribe el número 2)")
    print("TDBTS: Test de BTS (escribe el número 1)")
    print("Coming soon...")
    # Error: 'numpy.float64' object is not callable
    # Error: la verdad no se, pero era para instalat lass librerías
    # Error: x valor no está definido
    # SyntaxError: EOL while scanning string literal
    #SyntaxError: Non-UTF-8 code starting with '\xc3' in file C:\Proyecto de administración\La aberración.py on line 288, but no encoding declared; see https://python.org/dev/peps/pep-0263/ for details
elif tema == 8.1:
    import numpy as np

    print("Tema 8.1: La Naturaleza ded la estimación (Solo media, varianza y desviación estandar)")
    print("Venid a escribir en el [] SEPARANDOLOS CON COMAS, ya no voy a perder el tiempo en esto")
    s = [1, 2, 3, 4, 5]
    media = np.mean(s)
    varianza = np.var(s)
    desviación = np.std(s)
    print("La media es: ", media)
    print("La variana es: ", varianza)
    print("La desviacióne standar es: ", desviación)
    print("Para más información consulte a kcalleros@epccj.edu.mx")
elif tema == 8.2:
    print("Tema 8.2: Estimación de la media con la desviación estandar conocida")
    ans = int(input("Qué desea seleccionar(Intervalo_de_confianza(1), El_error_máximo_de_estimación(2) o Determinación_de_l_tamaño_muestral(3))?"))

    if ans == 1:
        n = int(input("Valor del tamaño de la muestra: "))
        xbarra = float(input("Valor de xbarra: "))
        desviación = float(input("Valor de la desviación estandar: "))
        alfa = int(input("Valor de alfa en enteros(95% = 95): "))
        from scipy.special import ndtri

        alfa1 = alfa / 100
        za = (1 - alfa1) / 2
        z = ndtri(za)
        ersdm = desviación / n ** 0.5

        # miren, esto va as er muy facil, tan soloi van a durar unas cuantas horas, pun 1 día con esto >:(, patrañas, mentiras, falacias
        xme = xbarra - (z) * (ersdm)
        xma = xbarra + (z) * (ersdm)

        print("En intervalo de confinaza va desde ", xme, "a ", xma)

    elif ans == 2:
        n = int(input("Valor del tamaño de la muestra: "))
        desviación = int(input("Valor de la desviación estandar: "))
        alfa = int(input("Valor de alfa en enteros(95% = 95): "))
        from scipy.special import ndtri

        alfa1 = alfa / 100
        za = (1 - alfa1) / 2
        z = ndtri(za)
        ersdm = desviación / n ** 0.5
        E = (z) * (ersdm)

        print("El error máximo de estimación es de ", E)

    elif ans == 3:
        print("SOLAMENTE ES EN LAS OCACIONES QUE CONOCES LA DESVIACIÓN ESTANDAR")
        desviación = int(input("Valor de la desviación estandar: "))
        alfa = int(input("Valor de alfa en enteros(95% = 95): "))
        from scipy.special import ndtri

        alfa1 = alfa / 100
        za = (1 - alfa1) / 2
        z = ndtri(za)
        ersdm = desviación / n**0.5
        tn = ((z) * (desviación)) ** 2

        print("El temaño de la muestra es de ", tn)
    else:
        print("por favor llame a la policía me están matando")
        print("Huye simba, huye lejos y nunca regreses")
        print( "Auxilio, los docentes de la EPCCJ nos explotan constantemente, no nos dan vacaciones, lo unico que les importa es ver arder el mundo :'(")
        print("#SaveEPCCJStudents")

elif tema == 8.3:
    print("Tema 8.3: La naturaleza de la prueba de hipótesis")
    print("Aquí se resolverá los planteamientos de la prueba de hipótesis")
    print("Qué es la hipótesis nula(Ho): La hipótesis nula es aquella frase que nosotros queremos que no pase")
    print("Qué es la hipótesis alternativa(Ha): La hipótesis alternativa es aquella que nosotrso queremos que pase")
    print("Al obtener los resultados nosotros tendremos 4 opciones que usualmente utilizaremos 2 (si las quieren ver están en la pag. 364 y 365 del libro estadistica elemental johnson kuby): ")
    print("Principalmente utilizaremos Fracazar en rechazar Ho y Rechazar Ho")
    print("Cuando fracazamos en rechazar Ho es cuando nuestro valor p es mayor al valor alfa y la conclusión se tiene que redactar de la siguiente manera: ")
    print("No hay suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    print("Cuando rechazamos Ho es cuando nuestro valor p es menor que alfa y la conclusión se tiene que redactar de la siguiente: ")
    print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    r = int(input("Quieres ver un ejemplo?(Sí=1/No=0): "))
    if r == 1:
        print("Supongamos que queremos comprobar que la EPCCJ es una maravilla entonces su Ha es: La EPCCJ es una maravilla y el Ho sería: La EPCCJ es un asco")
        print("Investiga y resulta que usted concluyó que la escuela es un asco y sobrexplotadora por lo que fracazamos en rechazar Ho y concluimos en: ")
        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que la EPCCJ es un asco")
    elif r == 0:
        print("Lo siento, pero no mames, estoy explicando tranquilamente para que solamente no quieres leer esto?. Bueno, vete ya >:(.")
    else:
        from tkinter import *
        from tkinter import filedialog

        root = Tk()
        root.geometry("500x50")
        root.title("Hola")
        bruh = Label(root,
                     text="Esto solo es una rutina de mantenimiento para las personas que no saben leer indicaciones :)")
        bruh.pack()

        root.mainloop()
elif tema == 8.4:
    print("Tema 8.4: Prueba de hipótesis de la media con la desviación estandar conocida")
    print("Recuerda siempre usar las ___ para escribir un espacio (Ejemplo: Las personas son = Las_personas_son)")
    resp = int(input("El problema es de 1 o 2 colas?(1 cola = 1/2 colas = 2): "))
    if resp == 1:
        Ha = int(input("Nuestra hipótesis alternativa es mayor o menor(mayor 1/menor 0)?: "))
        if Ha == 0:
            import scipy.stats as st

            n = int(input("Introduce el número de muestras: "))
            xbarra = float(input("Introduce el valor de xbarra: "))
            media = float(input("Introduce el valor de la media: "))
            desv = float(input("Introduce el valor de la desviación estandar: "))
            alfa = float(input("Introduce el valor de alfa(resta 1- alfa si es necesario): "))
            ze = (xbarra - media) / (desv / n ** 0.5)
            p = st.norm.cdf(ze)
            print("El valor z* es de", p)
            if p > alfa:
                print("Fracazar en rechazar Ho: ", p)
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
                print("Fracazar en rechazar Ho: ", p)
                print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Q CHAO")
    elif resp == 2:
        import scipy.stats as st

        n = int(input("Introduce el número de muestras: "))
        xbarra = float(input("Introduce el valor de xbarra: "))
        media = float(input("Introduce el valor de la media: "))
        desv = float(input("Introduce el valor de la desviación estandar: "))
        alfa = float(input("Introduce el valor de alfa(resta 1 - alfa si es necesario): "))
        ze = (xbarra - media) / (desv / n ** 0.5)
        p1 = st.norm.cdf(ze)
        p = p1 * 2
        print("El valor z* es de", p)
        if p > alfa:
            print("Fracazar en rechazar Ho: ", p)
            print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Rechazar Ho")
            print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        print("Sabes dónde te veo dentro de 10 años?, dentro de una caja, BAJO TIERRA")

elif tema == 9.1:
    print("Tema 9.1: Inferencias en torno a la media con la desviación estandar desconocida")
    print("Sabías que William Gosset estudió matemáticas y química en la Universidad de Oxford y al graduarse ocupó una plaza en la Cervecería Guinness, en Dublín. En 1905, se reunió con Karl Pearson para discutir sus problemsa estadísticos y un año después, con la aprobación de Guinness, fue a trabajar al laboratorio Biométrico de Pearson y bla bla bla, escribió muchos ensayos, bla bla bla, usó el seudónimo de Student, blablabla y así es como aruinó nuestras vidas como estudiantes. FIN")
    print("La desviación estandar se ඞtituirá por el valor s y en lugar de calcular el valor z* se calculará el valor t*")
    ans = int(input("Ingrese que tema quiere abarcar(Intervalo_de_confianza (1) o Prueba_de_hipótesis(2)): "))
    if ans == 1:
        c = int(input("Ingrese la cantidad de colas (1 o 2): "))
        if c == 1:
            import scipy.stats

            xbarra = float(input("Ingrese el valor de xbarra: "))
            n = int(input("Ingrese el número de muestras: "))
            s = float(input("Introduce el valor s: "))
            alfa = float(input("Introduce el valor de alfa(resta 1 - alfa si es necesario): "))
            gl = n - 1
            alfa2 = alfa / 2
            t = scipy.stats.t.ppf(q=1 - alfa2, df=gl)
            sn = s / (n ** 0.5)
            E = t * sn
            Mme = xbarra - E
            Mma = xbarra + E
            print("El intervalo de confianza va de ", Mme, "a", Mma)
        elif c == 2:
            import scipy.stats

            xbarra = float(input("Ingrese el valor de xbarra: "))
            n = int(input("Ingrese el número de muestras: "))
            s = float(input("Introduce el valor s: "))
            alfa = float(input("Introduce el valor de alfa(resta 1 - alfa si es necesario): "))
            gl = n - 1
            alfa2 = alfa / 2
            t = scipy.stats.t.ppf(q=1 - alfa2 / 2, df=gl)
            sn = s / (n ** 0.5)
            E = t * sn
            Mme = xbarra - E
            Mma = xbarra + E
            print("El intervalo de confianza va de ", Mme, "a", Mma)
        else:
            print("Cuantas veces te he dicho que escribas un 1 o un 2, no un 3, no un 4, NO US 5. SOLO ES UN 1 O UN 2 >:(")
    elif ans == 2:
        c = int(input("La situación es de una o 2 colas?(poner 1 o 2): "))
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
                    print("Fracazar en rechazar Ho")
                    print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
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
                    print("Fracazar en rechazar Ho")
                    print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
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
                print("Fracazar en rechazar Ho")
                print("No existe suficiene evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
            else:
                print("Rechazar Ho")
                print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
        else:
            print("Oye, ¿quieres jugar videojuegos? Pues yo sí quiero. No he visto la luz del sol en años. Vamos a jugar League of Legends. ¿Te suena familiar? Debería ¡es genial! Sí gratis. Para eso sí te alcanza ¿no? Si tuvieras amigos seguro ya estarían jugando. ¿Y tú qué esperas? Comienza a jugar y haz amigos de verdad. Te mostrare como funciona. Comienzas por elegir un campeón, y creeme, hay muchos. Y si te gusta uno que se ve increíble, pero odias su bigotito, no hay problema, puedes vestirlo con diferentes aspectos. Quiero que mi pirata sea mas como de anime- A eso me referia, caballero. La verdadera diversión comienza cuando empiezas a jugar. La accíon es epica y sin limites, con estrategias y todo, solo observa. Hay muchas formas de vencer al enemigo. Espadas, arco, magia, dientes.")
            print("¿Aún tienes problemas? Ve a la tienda y compra algo. Se que solo es culpa de los objetos y no tu inherente falta de habilidad. Hay 5 roles que podras dominar, y mas de 100 campeones, y 200 objetos. Así que, haz tus calculos, son como 1 millón de combinaciones, aunque soy, malo en matematicas. No hay problema si eres casual, encajaras muy bien con los otros novatos. Pero si quieres un desafío, este es tu lugar. Tendras la oportunidad de demostrar ese poder que llevas en tu interior. Asciende en las clasificatorias y perfecciona a tu campeón. Hablamos de desarrollo personal solo que en el lugar de cocinar o aprender una carrera, ¡Lo haras en League of Legends! Prioridades: solo piensa en la gloria que te espera. Formaras parte de esta enorme comunidad. La gente ama este juego.")
            print("¿Recuerdas lo que es amar? Yo no he sentido nada en años. Lo que trato de decirte es que, League of Legends te cambiara. ¿Que estas esperando? Rapido, este video ya casi termina. No dejes pasar la oportunidad. Este podria volverse tu juego favorito. Todos los días llegan jugadores nuevos. No permitas que te dejen atras. La diversión comienza ahora. League of Legends, descargalo y juegalo ya")
    else:
        print("Sabias que el profesor Luis Alfonso es Caraveo Balderas? o que este respectivo maestro se involucró en un proyecto de investigación con financiamiento interno: Inferencia Estadística sobre parámetros de sistemas de ecuaciones diferenciales, Clave USO315006042. Fecha inicial:31/01/2019. Fecha final: 17/12/2021 (Duración de 34 meses, Universidad de Sonora en la División de ciencias exactas y naturales)?")

elif tema == 9.2:
    print("Tema 9.2: Inferencias entorno a la probabilidad binomial de éxito")
    rasputin = int(input("Cuál tema quieres saber?(intervalo de confianza para p(1),tamaño de la muestra para estimar p sin información previa(2),tamaño de la muestra para estimar p con información previa(3) o el Estadístico de Prueba(4)): "))
    if rasputin == 1:
        # intervalo de confianza para p
        pera = int(input("Se tiene el valor p?(Sí(1)/No(2)): "))
        if pera == 1:
            p = float(input("Intyroduce dell valor p: "))
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
            x = float(
                input("Introduce el valor x(la cantidad de la muestra que padece diferente a la muestra total): "))
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
                n = int(input("Introducir el número de muestas: "))
                pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
                alfa = float(input("Introduce el valor de alfa: "))
                p = x / n
                q = 1 - p
                z = (p - pp) / (((p * q) / n) ** 0.5)
                print(z)
                import scipy.stats as st

                p = st.norm.cdf(z)
                if p > alfa:
                    print("Fracazar en rechazar Ho: ", p)
                else:
                    print("Rechazar Ho", p)
            elif Ha == 1:
                x = float(input("Introducir el valor x: "))
                n = int(input("Introducir el número de muestas: "))
                pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
                alfa = float(input("Introduce el valor de alfa: "))
                p = x / n
                q = 1 - p
                z = (p - pp) / ((p * q) / n) ** 0.5
                import scipy.stats as st

                p = st.norm.cdf(z)
                pv = 1 - p
                if pv > alfa:
                    print("Fracazar en rechazar Ho: ", p)
                else:
                    print("Rechazar Ho")
            else:
                import webbrowser

                webbrowser.open_new_tab("https://www.youtube.com/watch?v=9Jow8pV2fBI")
        elif sus == 2:
            x = float(input("Introducir el valor x: "))
            n = int(input("Introducir el número de muestas: "))
            pp = float(input("Introduce el valor p normal(el que te pone el problema usualmente): "))
            alfa = float(input("Introduce el valor de alfa: "))
            p = x / n
            q = 1 - p
            z = (p - pp) / ((p * q) / n) ** 2
            from scipy.special import ndtri

            p = ndtri(z)
            pv = 2 * p
            if pv > alfa:
                print("Fracazar en rechazar Ho: ", p)
            else:
                print("Rechazar Ho")
        else:
            print(">:(")
    else:
        print("Mira tio, tu saabes como hacer una gráfica de este tema, por lo que para en el método clásico puedes hacerlo a mano, yo no estaré aquí para investigar como se hacen las gráficas, tenemos como 10 exámenes regresando de vacaciones u 11 y si no quieres el tema anterior te tengo esto: Albion Online es un MMORPG no lineal en el que escribes tu propia historia sin limitarte a seguir un camino prefijado, explora un amplio mundo abierto con cinco biomas únicos, todo cuanto hagas tendrá su repercusión en el mundo, con su economía orientada al jugador de Albion los jugadores crean prácticamente todo el equipo a partir de los recursos que consiguen, el equipo que llevas define quien eres, cambia de arma y armadura para pasar de caballero a mago o juego como una mezcla de ambas clases, aventúrate en el mundo abierto y haz frente a los habitantes y las criaturas de Albion, inicia expediciones o adéntrate en mazmorras en las que encontraras enemigos aun mas difíciles, enfréntate a otros jugadores en encuentros en el mundo abierto, lucha por los territorios o por ciudades enteras en batallas tácticas, relájate en tu isla privada donde podrás construir un hogar, cultivar cosechas, criar animales, únete a un gremio, todo es mejor cuando se trabaja en grupo. Adéntrate ya en el mundo de Albion y escribe tu propia historia.")

elif tema == 2:
    import tkinter

    print("Signo Zodiacal")
    from tkinter import *

    sz = Tk()
    sz.geometry("980x100")
    sz.title("Signo Zodiacal")
    sz.configure(background="navy")
    A = tkinter.Label(sz, text="Virgo", bg="navy", fg="White")
    A.pack()
    B = Label(sz,
              text="No te pongas tantas pruebas a ti mismo: a veces te exiges demasiado, y eso no es bueno ni para ti ni para los que te rodean. Debes de pasar a la acción pero desde la calma y el disfrute.",
              bg="navy", fg="White")
    B.pack()
    B2 = Label(sz,
               text="El estrés es muy malo, y últimamente llega a tu vida con demasiada frecuencia. Controla. Esto no aplica para los alumnos de la EPCCJ.",
               bg="navy", fg="White")
    B2.pack()
    C = Label(sz,
              text="Libera el estres y aprueba este proyecto con un 10, gracias a esto mejorará tu cuerpo, alma y las personas que te rodean serán más felices.",
              bg="navy", fg="White")
    C.pack()
    sz.mainloop()
elif tema == 1:
    import socket
    import sys

    Dox_owo = socket.gethostname()
    ip = socket.gethostbyname(Dox_owo)
    print("Jajajaja, el nombre de tu pc es: " + Dox_owo)
    print("Y tu dirección de IP es: " + ip)
    print("Escaneando")
    obj = socket.gethostbyname(ip)
    try:
        for port in range(1, 150):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = s.connect_ex((ip, port))
            if resultado == 0:
                print("El puerto {} está abierto".format(port))
                print("Recopilando datos y mandandolos a la nube...")
            s.close()
    except:
        print("\n Saliendo..")
        sys.exit(0)
    # Solamente usted podrá ver esto, no hay servidores porque están caros :(
else:
    import socket
    import sys

    Dox_owo = socket.gethostname()
    ip = socket.gethostbyname(Dox_owo)
    print("Jajajaja, el nombre de tu pc es: " + Dox_owo)
    print("Y tu dirección de IP es: " + ip)
    print("Escaneando")
    obj = socket.gethostbyname(ip)
    try:
        for port in range(1, 150):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = s.connect_ex((ip, port))
            if resultado == 0:
                print("El puerto {} está abierto".format(port))
                print("Recopilando datos y mandandolos a la nube...")
            s.close()
    except:
        print("\n Saliendo..")
        sys.exit(0)

    # Solamente usted podrá ver esto, no hay servidores porque están caros :(
    