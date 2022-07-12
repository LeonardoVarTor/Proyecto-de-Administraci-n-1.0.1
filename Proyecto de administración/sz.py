import tkinter

print("Signo Zodiacal")
from tkinter import *
sz = Tk()
sz.geometry("980x100")
sz.title("Signo Zodiacal")
sz.configure(background= "navy")
A = tkinter.Label(sz, text= "Virgo", bg="navy", fg="White")
A.pack()
B = Label(sz, text = "No te pongas tantas pruebas a ti mismo: a veces te exiges demasiado, y eso no es bueno ni para ti ni para los que te rodean. Debes de pasar a la acción pero desde la calma y el disfrute.",  bg="navy", fg="White")
B.pack()
B2 = Label(sz, text="El estrés es muy malo, y últimamente llega a tu vida con demasiada frecuencia. Controla. Esto no aplica para los alumnos de la EPCCJ.", bg="navy", fg="White")
B2.pack()
C = Label(sz, text = "Libera el estres y aprueba este proyecto con un 10, gracias a esto mejorará tu cuerpo, alma y las personas que te rodean serán más felices.", bg="navy", fg="White")
C.pack()
sz.mainloop()