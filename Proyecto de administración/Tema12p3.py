print("Tema 12.3: Aplicaciones de la ANOVA de un solo factor")
alfa = float(input("Introduce el nivel de significancia: "))
print("Si la table no tiene números y la matrix sigue introduce el número 0")
print("filas = Horizontal")
print("Columnas = Vertical")
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
SColumna = matrixx.sum(axis=0, dtype='float')

Matrixx = np.array(matrix)
countf = Matrixx > 0
ContarF = countf.sum(axis=0, dtype='float')

Scolum = np.array(SColumna)
ColumF = np.array(ContarF)
print(matrixx)
print(SColumna)
print(ContarF)
print("////////////////////////////////////////////////////////////")
n = ContarF.sum()
N = np.array(n)
print(n)
print("////////////////////////////////////////////////////////////")
#Perdón por el nombre tan tonto
e2 = Matrixx.sum()
E2 = np.array(e2)
print(e2)
Ex2 = (Matrixx**2)
eX2 = Ex2.sum()
EX2 = np.array(eX2)
print(eX2)
print("////////////////////////////////////////////////////////////")
ss_total = EX2 - ((E2**2)/N)
SS_Total = np.array(ss_total)
print(ss_total)
print("////////////////////////////////////////////////////////////")
#SS factor
ss_factorf = (Scolum**2)/ColumF
Ss_factof = ss_factorf.sum()
sS_Facts = np.array(Ss_factof)
ss_factor = sS_Facts- ((E2**2)/N)
SS_Factor = np.array(ss_factor)
print(ss_factor)
print("////////////////////////////////////////////////////////////")
#SS error
ss_error = EX2 - sS_Facts
SS_Error = np.array(ss_error)
print(ss_error)
print("////////////////////////////////////////////////////////////")
#Grados de libertad
gl_factor = C-1
Gl_Factor = np.array(gl_factor)
gl_total = N-1
gl_error = N-C
Gl_Error = np.array(gl_error)
print(gl_factor)
print(gl_total)
print(gl_error)
print("////////////////////////////////////////////////////////////")
#ms
ms_factor = SS_Factor/Gl_Factor
Ms_Factor = np.array(ms_factor)
ms_error = SS_Error/Gl_Error
Ms_Error = np.array(ms_error)
print(ms_factor)
print(ms_error)
print("////////////////////////////////////////////////////////////")
#ANOVA
print("Tabla ANOVA")
madremiawilly = np.array([['Fuente','Gl','SS','SS'],
                 ['Factor',Gl_Factor,SS_Factor,Ms_Factor],
                 ['Error',Gl_Error,SS_Error,Ms_Error]])
print(madremiawilly)
print("////////////////////////////////////////////////////////////")
#Estadístico de prueba
f_estrella = Ms_Factor/Ms_Error
F_Estrella = f_estrella
print(f_estrella)
print("////////////////////////////////////////////////////////////")
import scipy.stats
p = 1 - scipy.stats.f.cdf(F_Estrella, Gl_Factor-1, Gl_Error-1 )

if p > alfa:
    print("Fracasar en rechazar Ho: ", p)
else:
    print("Rechazar Ho", p)
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema12p3


