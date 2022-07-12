print("Tema 11.2: Inferencias concernientes o experimentos multinomiales")
print("Experimento multinomial")
print("1. n ensayos independientes")
print("2. Los resultados de cada ensayo se puede clasificar en una sola de las k posibles celdas")
print("3. Existe una probabilidad asociado a cada celda y estas son constantes en el experimento (P1+P2+...+Pk=1)")
print("4. El experimento resultará en k frecuencias acomuladas donde cada O es el número de veces que el resultado de ensaayo que en dicho celda particular")
print("Calcular la Frecuencia Acomulada: ")
print("Ei = n*pi")

Pruebas = int(input("Las frecuencias esperadas son iguales o desiguales? (Sí=1/No=2)"))
if Pruebas == 1:
    print("Frecuencias observadas y prueba de hipótesis")
    alfa = float(input("Introduce el nivel de significancia: "))
    F = 1
    C = int(input("Cuántos datos desea introducir? "))
    matrix = []
    print("Introduce los datos: ")

    for i in range(F):
        a = []
        for j in range(C):
            a.append(float(input()))
        matrix.append(a)
    import numpy as np

    np_matriz = np.array(matrix)
    Total_Observado = np_matriz.sum(1)
    Valor_Esperado = (Total_Observado / C)

    import numpy

    Observado = numpy.array(matrix)
    Observado_Esperado = Observado - Valor_Esperado

    Observado_Esperado_Cuadrado_Esperado = ((Observado_Esperado) ** 2) / Valor_Esperado

    TotalT = Observado_Esperado_Cuadrado_Esperado.sum(1)

    from scipy.stats.distributions import chi2

    gl = (C - 1)
    p = chi2.sf(TotalT, gl)
    if p > alfa:
        print("Fracasar en rechazar Ho: ", p)
        print("Las frecuencias observadas no son significativamente diferentes de los esperados")
        print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")

    else:
        print("Rechazar Ho", p)
        print("Las frecuencias observadas son significativamente diferentes de los valores esperados")
        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
elif Pruebas == 2:
    print("Prueba de hipótesis")
    alfa = float(input("Introduce el nivel de significancia: "))
    F = 1
    C = int(input("Cuántos datos desea introducir? "))
    matrix = []
    print("Introduce los datos en orden: ")

    for i in range(F):
        a = []
        for j in range(C):
            a.append(float(input()))
        matrix.append(a)

    print("Introduce las frecuencias esperadas en orden: ")
    Fi = 1
    Ci = C
    matrix = []

    for i in range(Fi):
        b = []
        for j in range(Ci):
            b.append(float(input()))
        matrix.append(b)

    import numpy as np

    np_matriz = np.array(matrix)
    Total_Observado = np_matriz.sum(1)

    Valor_Esperado = (Total_Observado / C)
    ValorEsperado = (Total_Observado * Valor_Esperado)

    import numpy

    Observado = numpy.array(matrix)
    Observado_Esperado = Observado - ValorEsperado

    Observado_Esperado_Cuadrado_Esperado = ((Observado_Esperado) ** 2) / ValorEsperado

    TotalT = Observado_Esperado_Cuadrado_Esperado.sum(1)

    from scipy.stats.distributions import chi2

    gl = (C - 1)
    pp = chi2.sf(TotalT, gl)
    if pp > alfa:
        print("Fracasar en rechazar Ho: ", pp)
        print("No existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
    else:
        print("Rechazar Ho", pp)
        print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")

else:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema11p2

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema11p2
