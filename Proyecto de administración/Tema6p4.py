print("Tema 6.4: Notación")
print("Identificar z(α)")
C = int(input("El área es de 1 o 2 colas? "))
if C == 1:
    from scipy import stats
    z = float(input("Introduce el valor alfa: "))
    za = stats.norm.ppf(1 - z)
    print("El área bajo la curva es de: ", za)
elif C == 2:
    from scipy.special import ndtri

    alfa = float(input("Introduce el valor de alfa: "))
    za = 1 - (alfa / 2)
    z = ndtri(za)
    print("El área bajo la curva es de: ", z)

else:
    S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema6p4

S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema6p4