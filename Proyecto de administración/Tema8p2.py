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
     ersdm = desviación/n**0.5

#miren, esto va as er muy facil, tan soloi van a durar unas cuantas horas, pun 1 día con esto >:(, patrañas, mentiras, falacias
     xme = xbarra - (z)*(ersdm)
     xma = xbarra + (z)*(ersdm)

     print("En intervalo de confinaza va desde ",xme,"a ",xma)

elif ans == 2:
     n = int(input("Valor del tamaño de la muestra: "))
     desviación = int(input("Valor de la desviación estandar: "))
     alfa = int(input("Valor de alfa en enteros(95% = 95): "))
     from scipy.special import ndtri

     alfa1 = alfa / 100
     za = (1 - alfa1) / 2
     z = ndtri(za)
     ersdm = desviación / n ** 0.5
     E = (z)*(ersdm)

     print("El error máximo de estimación es de ", E)

elif ans == 3:
     print("SOLAMENTE ES EN LAS OCASIONES QUE CONOCES LA DESVIACIÓN ESTÁNDAR")
     desviación = int(input("Valor de la desviación estándar: "))
     alfa = int(input("Valor de alfa en enteros(95% = 95): "))
     from scipy.special import ndtri
     alfa1 = alfa / 100
     za = (1 - alfa1) / 2
     z = ndtri(za)
     tn = ((z)*(desviación))**2

     print("El tamaño de la muestra es de ", tn)
else:
     print("#SaveEPCCJStudents")
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema8p2





     




