print("Tema 11.3: Inferencias concernientes a tablas de contingencia")
print("Qué desea calcular? (1 = Prueba de hipótesis de independencia o 2 = Prueba de homogeneidad)")
Answere = int()
if Answere == 1:
    # Prueba independiente
    alfa = float(input("Introduce el nivel de significancia: "))
    print("filas = Vertical")
    print("Columnas = Horizontal")
    F = int(input("Inserte el número de filas: "))
    C = int(input("Inserte el número de columnas: "))

    matrix = []
    print("Introduce los datos en orden (de izquierda a derecha hasta terminar): ")

    for i in range(F):  # A for loop for row (filas) entries
        a = []
        for j in range(C):  # A for loop for column (columnas) entries
            a.append(float(input()))
        matrix.append(a)

    import numpy as np

    matrixx = np.matrix(matrix)
    SFila = matrixx.sum(axis=1, dtype='float')
    SColumna = matrixx.sum(axis=0, dtype='float')
    Matrixx = np.array(matrix)
    Total_Matrix = np.sum(Matrixx)

    print(SFila)
    print("////////////////////////////////////////////////////////////")
    print(SColumna)
    print("////////////////////////////////////////////////////////////")
    print(Total_Matrix)
    print("////////////////////////////////////////////////////////////")

    import numpy as np

    VEF = np.array(SFila)
    VEC = np.array(SColumna)
    VETM = np.array(Total_Matrix)
    Valores_Esperados = (VEC / VETM) * VEF
    print(Valores_Esperados)
    print("////////////////////////////////////////////////////////////")

    Valores_Esperadoss = np.array(Valores_Esperados)
    Chi2 = ((Matrixx - Valores_Esperadoss) ** 2) / Valores_Esperadoss
    print(Chi2)
    print("////////////////////////////////////////////////////////////")
    Chii2 = np.array(Chi2)
    Chi2_Original = np.sum(Chii2)
    print(Chi2_Original)
    print("////////////////////////////////////////////////////////////")

    from scipy.stats.distributions import chi2

    gl = (C - 1)
    pp = chi2.sf(Chi2_Original, gl)
    if pp > alfa:
        print("Fracasar en rechazar Ho: ", pp)
    else:
        print("Rechazar Ho", pp)
elif Answere == 2:
    # Prueba independiente
    alfa = float(input("Introduce el nivel de significancia: "))
    print("filas = Vertical")
    print("Columnas = Horizontal")
    F = int(input("Inserte el número de filas: "))
    C = int(input("Inserte el número de columnas: "))

    matrix = []
    print("Introduce los datos en orden (de izquierda a derecha hasta terminar): ")

    for i in range(F):  # A for loop for row (filas) entries
        a = []
        for j in range(C):  # A for loop for column (columnas) entries
            a.append(float(input()))
        matrix.append(a)

    import numpy as np

    matrixx = np.matrix(matrix)
    SFila = matrixx.sum(axis=1, dtype='float')
    SColumna = matrixx.sum(axis=0, dtype='float')
    Matrixx = np.array(matrix)
    Total_Matrix = np.sum(Matrixx)

    print(SFila)
    print("////////////////////////////////////////////////////////////")
    print(SColumna)
    print("////////////////////////////////////////////////////////////")
    print(Total_Matrix)
    print("////////////////////////////////////////////////////////////")

    import numpy as np

    VEF = np.array(SFila)
    VEC = np.array(SColumna)
    VETM = np.array(Total_Matrix)
    Valores_Esperados = (VEC / VETM) * VEF
    print(Valores_Esperados)
    print("////////////////////////////////////////////////////////////")

    Valores_Esperadoss = np.array(Valores_Esperados)
    Chi2 = ((Matrixx - Valores_Esperadoss) ** 2) / Valores_Esperadoss
    print(Chi2)
    print("////////////////////////////////////////////////////////////")
    Chii2 = np.array(Chi2)
    Chi2_Original = np.sum(Chii2)
    print(Chi2_Original)
    print("////////////////////////////////////////////////////////////")

    from scipy.stats.distributions import chi2

    gl = (C - 1) * (F - 1)
    pp = chi2.sf(Chi2_Original, gl)
    if pp > alfa:
        print("Fracasar en rechazar Ho: ", pp)
        print("Según el nivel de significancia la prueba es independiente")
    else:
        print("Rechazar Ho", pp)
        print("Según el nivel de significancia la prueba es dependiente")
else:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema11p3

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema11p3









