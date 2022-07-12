print("Tema 8.3: La naturaleza de la prueba de hipótesis")
print("Aquí se resolverá los planteamientos de la prueba de hipótesis")
print("Qué es la hipótesis nula(Ho): La hipótesis nula es aquella frase que nosotros queremos que no pase")
print("Qué es la hipótesis alternativa(Ha): La hipótesis alternativa es aquella que nosotrso queremos que pase")
print("Al obtener los resultados nosotros tendremos 4 opciones que usualmente utilizaremos 2 (si las quieren ver están en la pag. 364 y 365 del libro estadistica elemental johnson kuby): ")
print("Principalmente utilizaremos Fracasar en rechazar Ho y Rechazar Ho")
print("Cuando fracazamos en rechazar Ho es cuando nuestro valor p es mayor al valor alfa y la conclusión se tiene que redactar de la siguiente manera: ")
print("No hay suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
print("Cuando rechazamos Ho es cuando nuestro valor p es menor que alfa y la conclusión se tiene que redactar de la siguiente: ")
print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que (enunciado de la Ha)")
r = int(input("Quieres ver un ejemplo?(Sí=1/No=0): "))
if r == 1:
  print("Supongamos que queremos comprobar que la EPCCJ es una maravilla entonces su Ha es: La EPCCJ es una maravilla y el Ho sería: La EPCCJ es un asco")
  print("Investiga y resulta que usted concluyó que la escuela es un asco y sobrexplotadora por lo que fracazamos en rechazar Ho y concluimos en: ")
  print("Existe suficiente evidencia en el nivel de significancia de alfa para demostrar que la EPCCJ es un asco")
elif r == 0:
    S = int(input("Do you want to exit(Y=1/N=2)? "))
    if S == 1:
        import main
    else:
        import Tema8p3
else:
    from tkinter import *
    from tkinter import filedialog
    root = Tk()
    root.geometry("500x50")
    root.title("Hola")
    bruh = Label(root, text= "Esto solo es una rutina de mantenimiento para las personas que no saben leer indicaciones :)")
    bruh.pack()

    root.mainloop()

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema8p3

