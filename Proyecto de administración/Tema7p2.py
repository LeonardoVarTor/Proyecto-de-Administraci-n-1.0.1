print("Tema 7.2: La distribución muestral de medias muestrales")
print("Distribución muestral de medias muestrales (DMMM): Sitodas las posibles muestras aleatoras, cada una de tamaño n, se toman de cualquier población con media μ y una desviación estándar σ, entonces el DMMM tendrá lo siguiente:")
print("1. Una media μ xbarra es igual a μ")
print("2. Una desviación estandar σ xbarra es igual a σ/√n")
print("Más aún, si la población muestreada tiene una distribución normal, entonces la distribución muestral de xbarra también será normal para muestras de todos los tamaños")
print("El error estandar de la media (σ xbarra): La desviación estándar de la distribución muestral de las medias muestrales")
print("Teorema central del límite (TCL): La distribución muestral de las medias muestrales recordará más estrechamente la distribución normal conforme aumenta el tamaño de la mestra")

print("Para sacar la tabla de extensiones para xbarra puedes calcularlo usando el tema 5.2")
Resp = int(input("Desea calcular el error estándar de la media? (Sí = 1, No = 2)"))
if Resp == 1:
    σ = float(input("Ingrese el valor de σ: "))
    n = float(input("Ingrese el valor de n: "))
    σxbarra = σ/(n**0.5)
    print("El error estándar de la media es igual a ", σxbarra)
else:
    S = int(input("Seguro que quieres salir(Sí=1/No=2)? "))
    if S == 1:
        import main
    else:
        import Tema7p2

