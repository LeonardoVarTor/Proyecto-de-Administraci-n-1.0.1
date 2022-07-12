print("Tema 13.1: Análisis de correlación lineal ")
Respuesta = int(input("Qué desea calcular (Covarianza = 1, Coeficiente de correlación lineal = 2): "))
if Respuesta == 1:
    print("filas = Horizontal")
    print("Columnas = Vertical")

    Fx = 1
    Cx = int(input("Cuántos datos desea introducir? "))
    matrixxx = []
    print("Introduce los datos de las x: ")

    for i in range(Fx):
        a = []
        for j in range(Cx):
            a.append(float(input()))
        matrixxx.append(a)
    import numpy as np

    matrixx = np.array(matrixxx)

    matrixyy = []
    print("Introduce los datos de las y: ")

    for i in range(Fx):
        a = []
        for j in range(Cx):
            a.append(float(input()))
        matrixyy.append(a)
    import numpy as np

    matrixy = np.array(matrixyy)

    xsumatrix = matrixx.sum(1)
    xsmatrix = np.array(xsumatrix)
    ysumatrix = matrixy.sum(1)
    ysmatrix = np.array(ysumatrix)
    xbarrax = xsmatrix / Cx
    xbarraxx = np.array(xbarrax)
    xbarray = ysmatrix / Cx
    xbarrayy = np.array(xbarray)

    restax = matrixx - xbarraxx
    xresta = np.array(restax)
    restay = matrixy - xbarrayy
    yresta = np.array(restay)
    multiplicacion = xresta * yresta
    multirray = np.array(multiplicacion)
    sumulti = multirray.sum(1)
    Covarian = sumulti / (Cx - 1)
    Covarinza = np.array(Covarian)
    print("La covarianza es de: ",Covarinza)

elif Respuesta == 2:
    sx = float(input("Introduce el valor Sx: "))
    sy = float(input("Introduce el valor Sy: "))
    print("filas = Horizontal")
    print("Columnas = Vertical")

    Fx = 1
    Cx = int(input("Cuántos datos desea introducir? "))
    matrixxx = []
    print("Introduce los datos de las x: ")

    for i in range(Fx):
        a = []
        for j in range(Cx):
            a.append(float(input()))
        matrixxx.append(a)
    import numpy as np

    matrixx = np.array(matrixxx)

    matrixyy = []
    print("Introduce los datos de las y: ")

    for i in range(Fx):
        a = []
        for j in range(Cx):
            a.append(float(input()))
        matrixyy.append(a)
    import numpy as np

    matrixy = np.array(matrixyy)

    xsumatrix = matrixx.sum(1)
    xsmatrix = np.array(xsumatrix)
    ysumatrix = matrixy.sum(1)
    ysmatrix = np.array(ysumatrix)
    xbarrax = xsmatrix / Cx
    xbarraxx = np.array(xbarrax)
    xbarray = ysmatrix / Cx
    xbarrayy = np.array(xbarray)

    restax = matrixx - xbarraxx
    xresta = np.array(restax)
    restay = matrixy - xbarrayy
    yresta = np.array(restay)
    multiplicacion = xresta * yresta
    multirray = np.array(multiplicacion)
    sumulti = multirray.sum(1)
    Covarian = sumulti / (Cx - 1)
    Covarinza = np.array(Covarian)
    sxsy = sx*sy
    Coeficiente = Covarinza/sxsy
    print("El coeficiente de correlación lineal es de: ",Coeficiente)
else:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema13p1
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema13p1