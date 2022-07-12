print("Tema 7.3: Aplicación de la distribución muestral de medias muestrales (DMMM)")
print("Calcular el valor z = 1, Calcular la probabilidad = 2, Calcular los límites de la media (xbarra) = 3")
Res = int(input("Introduce el tema  que desea ver: "))
if Res == 1:
    xbarra = float(input("Introduce el valor de xbarra: "))
    μxbarra = float(input("Introduce el valor de μ xbarra: "))
    σ = float(input("Introduce el valor de σ: "))
    n = int(input("Introduce el valor n: "))
    z = (xbarra-μxbarra)/(σ/(n**0.5))
    print(" El valor z es ", z)
elif Res == 2:
    xbarra1 = float(input("Introduce el valor de xbarra 1: "))
    xbarra2 = float(input("Introduce el valor de xbarra 2: "))
    μxbarra = float(input("Introduce el valor de μ xbarra: "))
    σ = float(input("Introduce el valor de σ: "))
    n = int(input("Introduce el valor n: "))
    z1 = (xbarra1 - μxbarra) / (σ / (n ** 0.5))
    z2 = z = (xbarra2-μxbarra)/(σ/(n**0.5))
    import scipy.stats as st
    p1 = st.norm.cdf(z1)
    p2 = st.norm.cdf(z2)
    re = p2 - p1
    print("La probabilidad es igual a", re)
elif Res == 3:
    z1 = float(input("Introduce el valor de z1: "))
    z2 = float(input("Introduce el valor de z2: "))
    μxbarra = float(input("Introduce el valor de μ xbarra: "))
    σ = float(input("Introduce el valor de σ: "))
    n = int(input("Introduce el valor n: "))
    xbarra1 = μxbarra - (z1*(σ/(n**0.5)))
    xbarra2 = μxbarra - (z2 * (σ / (n ** 0.5)))
    print("Los limites son ", xbarra1, "y", xbarra2)
else:
    S = int(input("Seguro que quieres salir(Sí=1/No=2)? "))
    if S == 1:
        import main
    else:
        import Tema7p3
S = int(input("Seguro que quieres salir(Sí=1/No=2)? "))
if S == 1:
    import main
else:
    import Tema7p3

