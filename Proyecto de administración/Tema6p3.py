print("Tema 6.3: Aplicaciones de las distribuciones normales")
print("Probabilidad con curva estándar = 1, probabilidad bajo cualquier curva normal = 2, encontrar el percentil(valor x) = 3, encontrar la desviación estándar = 4")
P = int(input("Qué desea calcular? "))
if P == 1:
    import scipy.stats as st
    x1 = float(input("Ingrese el valor x1: "))
    μ1 = float(input("ingrese el valor μ1: "))
    σ1 = float(input("Ingrese el valor σ1: "))
    z1 = (x1-μ1)/σ1
    x2 = float(input("Ingrese el valor x2: "))
    μ2 = float(input("ingrese el valor μ2: "))
    σ2 = float(input("Ingrese el valor σ2: "))
    z2 = (x2-μ2)/σ2
    p1 = st.norm.cdf(z1)
    p2 = st.norm.cdf(z2)
    Pp = p2 - p1
    print("La probabilidad es de ", Pp)
elif P == 2:
    C = int(input("El área es hacia la izquierda(1) o derecha(2)? "))
    if C == 1:
        import scipy.stats as st
        x = float(input("Ingrese el valor x: "))
        μ = float(input("ingrese el valor μ: "))
        σ = float(input("Ingrese el valor σ: "))
        z = (x - μ) / σ
        p = st.norm.cdf(z)
        print("La probabilidad es de ", p)
    elif C == 2:
        import scipy.stats as st
        x = float(input("Ingrese el valor x: "))
        μ = float(input("ingrese el valor μ: "))
        σ = float(input("Ingrese el valor σ: "))
        z = (x - μ) / σ
        p = st.norm.cdf(z)
        r = 1 - p
        print("La probabilidad es de ", r)
    else:
        import Tema6p3
elif P == 3:
    z = float(input("Ingrese el valor z: "))
    μ = float(input("ingrese el valor μ: "))
    σ = float(input("Ingrese el valor σ: "))
    x = μ + (σ*z)
    print("El valor x es de: ", x)
elif P == 4:
    whatif = int(input("x y μ juntas(1) o separadas(2)? "))
    if whatif == 1:
        z = float(input("Ingrese el valor z: "))
        xμ = float(input("Ingrese el valor x - μ"))
        σ = (xμ) / z
        print("La desviación estándar es: ", σ)
    elif whatif == 2:
        z = float(input("Ingrese el valor z: "))
        x = float(input("Ingrese el valor x: "))
        μ = float(input("ingrese el valor μ: "))
        σ = (x - μ) / z
        print("La desviación estándar es: ", σ)
    else:
        S = int(input("Do you want to exit(Y=1/N=2)? "))
        if S == 1:
            import main
        else:
            import Tema6p3
else:
    print("Con que quieres encontrar la media, verdad?")
    z = float(input("Ingrese el valor z: "))
    x = float(input("Ingrese el valor x: "))
    σ = float(input("Ingrese el valor σ: "))
    μ = x -(z*σ)
    print("La media es de: ", μ)

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema6p3




