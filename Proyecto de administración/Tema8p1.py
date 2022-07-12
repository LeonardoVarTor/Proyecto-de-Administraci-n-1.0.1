import numpy as np
print("Tema 8.1: La Naturaleza ded la estimación (Solo media, varianza y desviación estándar)")
print("Venid a escribir en el [] SEPARÁNDOLOS CON COMAS, ya no voy a perder el tiempo en esto")
s = [1,2,3,4,5]
media = np.mean(s)
varianza = np.var(s)
desviación = np.std(s)
print("La media es: ", media)
print("La varianza es: ", varianza)
print("La desviación estándar es: ", desviación )
print("Para más información consulte a kcalleros@epccj.edu.mx")
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema8p1

#Arreglar con matrices