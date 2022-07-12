print("Tema 6.2: La distribución normal estándar")
import scipy.stats as st
C = int(input("El área area va a la izquierda o a la derecha (1) o está en el centro(2), encontrar el valor z acotada (3)(Ejemplo ejercicio 6.31) o el valor z en toda la gráfica (4)(Ejemplo ejercicio 6.34)? "))
if C == 1:
    LA = int(input("El área esta a la derecha(1) o a la izquierda(0)? "))
    if LA == 0:
        z = float(input("Introduce el valor de z: "))
        p = st.norm.cdf(z)
        print("El área bajo la curva es de: ", p)
    elif LA == 1:
        z = float(input("Introduce el valor de z: "))
        p = st.norm.cdf(z)
        R = 1 - p
        print("El área bajo la curva es de: ", R)
    else:
        S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema6p2
elif C == 2:
    z1 = float(input("Introduce el valor de z con área hacia la izquerda: "))
    z2 = float(input("Introduce el valor de z con área hacia la derecha: "))
    p1 = st.norm.cdf(z1)
    p2 = st.norm.cdf(z2)
    p = p2-p1
    print("El área bajo la curva es de: ", p)
elif C == 3:
    LA = int(input("El área esta a la derecha(1) o a la izquierda(0)? "))
    if LA == 0:
        p = float(input("Introduce el valor p: "))
        R = 0.5000-p
        z = st.norm.ppf(R)
        print("El valor z es de: ", z)
    elif LA == 1:
        p = float(input("Introduce el valor de p: "))
        R = 0.5000+p
        z = st.norm.ppf(R)
        print("El valor z es de: ", z)
    else:
        S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema6p2
elif C == 4:
    LA = int(input("El área esta a la derecha(1) o a la izquierda(0)? "))
    if LA == 0:
        p = float(input("Introduce el valor p: "))
        z = st.norm.ppf(p)
        print("El valor z es de: ", z)
    elif LA == 1:
        p = float(input("Introduce el valor de p: "))
        pp = 1-p
        z = st.norm.ppf(pp)
        print("El valor z es de: ", z)
    else:
        S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema6p2

else:
    S = int(input("Seguro que quieres salir(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema6p2
S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema6p2


