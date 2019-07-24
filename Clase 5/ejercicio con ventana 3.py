import sys

try:
	import Tkinter as tk
except ImportError:
	raise ImportError("Se requiere el modulo Tkinter")

def funcion():
	print "Hello World!!!"

root = tk.Tk()
etiqueta = tk.Button(root, text="Aceptar", command=funcion)
etiqueta.pack()
root.mainloop()