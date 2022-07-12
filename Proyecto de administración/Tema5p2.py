print("Tema 5.2: Distribuciones de probabilidad de una variable aleatoria discreta")
print("Media y varianza de una distribución de probabilidad discreta")
print("1. xbarra es la media de la muestra")
print("2. s^2 y s son la varianza y la desviación estándar de la muestra, respectivamente")
print("3. xbarra, s^2 y s se llaman estadísticos muestrales")
print("4. μ (letra griega mu minúscula) es la media de la población")
print("5. σ^2 (sigma al cuadrado) es la varianza de la población")
print("6. σ (letra griega sigma minúscula) es la desviación estándar de la población")
print("7. μ, σ^2 y σ se llaman parámetros poblacionales. (Un parámetro es una constante; μ, σ^2 y σ por lo general son valores desconocidos en los problemas estadísticos reales. ")
print("Más o menos la única en que se conoce es en problemas de libro de texto configurados con el propósito de aprendizaje y comprensión.")
print("Usted puede hacer la tabla y lo calcula con una calculadora")
R = int(input("Are you ready? Y = 1 "))
if R == 1:
    import main
else:
    print("No esperaba a que encontraras esto, bueno sí")
    print("Por favor de convertir las fracciones en decimales")
    print("Introduce el valor de x con s respectivo P(x)")
    x1 = float(input("Introduce el valor de x1: "))
    Px1 = float(input("Introduce el valor de P(x1): "))
    x2 = float(input("Introduce el valor de x2: "))
    Px2 = float(input("Introduce el valor de P(x2): "))
    x3 = float(input("Introduce el valor de x3: "))
    Px3 = float(input("Introduce el valor de P(x3): "))
    x4 = float(input("Introduce el valor de x4: "))
    Px4 = float(input("Introduce el valor de P(x4): "))
    xPx1 = x1*Px1
    xPx2 = x2*Px2
    xPx3 = x3*Px3
    xPx4 = x4*Px4
    μ = xPx1 + xPx2 + xPx3 + xPx4
    xc1 = x1**2
    xc2 = x2**2
    xc3 = x3**2
    xc4 = x4**2
    cxPx1 = xc1*Px1
    cxPx2 = xc2 * Px2
    cxPx3 = xc3 * Px3
    cxPx4 = xc4 * Px4
    σc1 = cxPx1 + cxPx2 + cxPx3 + cxPx4
    σc = (σc1)-(μ**2)
    σ = σc**0.5
    print("La μ es igual a : ", μ)
    print("La σ^2 es igual a: ", σc)
    print("La σ es igual a: ", σ)

    #Ejemplo de la 5.25 (introduce los datos correspondientes o pon en x 0,1,2,3,4 y en P(x) solo son 0.2 y tendría que salir 2,2 y 1.4142135623730951)
    #print("No esperaba a que encontraras esto, bueno sí")
    #print("Esto solo acepta decimales")
    #print("Introduce el valor de x con s respectivo P(x)")
    #x1 = float(input("Introduce el valor de x1: "))
    #Px1 = float(input("Introduce el valor de P(x1): "))
    #x2 = float(input("Introduce el valor de x2: "))
    #Px2 = float(input("Introduce el valor de P(x2): "))
    #x3 = float(input("Introduce el valor de x3: "))
    #Px3 = float(input("Introduce el valor de P(x3): "))
    #x4 = float(input("Introduce el valor de x4: "))
    #Px4 = float(input("Introduce el valor de P(x4): "))
    #x5 = float(input("Introduce el valor de x5: "))
    #Px5 = float(input("Introduce el valor de P(x5): "))
    #xPx1 = x1 * Px1
    #xPx2 = x2 * Px2
    #xPx3 = x3 * Px3
    #xPx4 = x4 * Px4
    #xPx5 = x5 * Px5
    #μ = xPx1 + xPx2 + xPx3 + xPx4 + xPx5
    #xc1 = x1 ** 2
    #xc2 = x2 ** 2
    #xc3 = x3 ** 2
    #xc4 = x4 ** 2
    #xc5 = x5 ** 2
    #cxPx1 = xc1 * Px1
    #cxPx2 = xc2 * Px2
    #cxPx3 = xc3 * Px3
    #cxPx4 = xc4 * Px4
    #cxPx5 = xc5 * Px5
    #σc1 = cxPx1 + cxPx2 + cxPx3 + cxPx4 + cxPx5
    #σc = (σc1) - (μ ** 2)
    #σ = σc ** 0.5
    #print("La μ es igual a : ", μ)
    #print("La σ^2 es igual a: ", σc)
    #print("La σ es igual a: ", σ)
    #puedes añadir tadas las que se te den la gana, pero las debes que escribir
#Arreglar con matrices
    Ra = int(input("Quieres regresar?: Y=1, N = Cualquier número"))
    if Ra == 1:
        import main
    else:
        import Tema5p2






