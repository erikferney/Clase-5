import sys

try:
	import Tkinter as tk
except ImportError:
	raise ImportError("Se requiere el modulo Tkinter")

class UI(tk.Frame):
	def __init__(self, parent=None):
		self.parent = parent

root = tk.Tk()
etiqueta = tk.Label(root, text="Hola mundo grafico desde Python!!!")
etiqueta.pack()
root.mainloop()