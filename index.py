# importa ttk que es la biblioteca que nos permite utilizar toda la interfaz gráfica
from tkinter import ttk
# importa todos los elementos de la interfaz gráfica, botones, listas, etc.
from tkinter import *

# importa la biblioteca para la conexión a la base de datos
import sqlite3

# utizaremos el paradigma POO para crear nuestras ventanas
# esta clase será la encargada de tener todos métodos de nuestras ventanas, agregar, editar y eliminar.
# tambien vamos a utilizar esta clase para crear nuestra ventana principal
class Product:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Adminimarket')
        
        # crea un frame como contenedor
        frame = LabelFrame(self.wind, text = 'Registrar Producto')
        frame.grid(row = 0, column = 1, columnspan = 3, pady = 20)

        # entrada de nombre
        Label(frame, text = 'Nombre Producto: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # entrada de precio
        Label(frame, text = 'Precio Producto: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # boton agregar producto
        ttk.Button(frame, text = 'Agregar Producto').grid(row = 3, columnspan = 2, sticky = W + E)


# esto será encargado de arrancar nuestra aplicación
if __name__ == '__main__':
    window = Tk()
    app = Product(window)
    window.mainloop()

