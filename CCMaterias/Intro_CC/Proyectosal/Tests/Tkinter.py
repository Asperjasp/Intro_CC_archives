import tkinter as tk
import customtkinter

########### TIKNTER


## Los Widget (Compontenetes ) Son hereditarios
root = tk.Tk() # Crea su interprete y un ejemplo dela clase Tk

root.geometry("1000x1000") # Tamaño de la ventana
root.title("Sudoku")
def menu(self):
        try:
            zystem("cls")
            print("---------------")
            print("-----MENU------")
            print("---------------")
            print("1.agregar Mascota:")
            print("2.listar Mascotas:")
            print("3.buscar mascota:")
            print("4.Estadistica:")
            print("5.salir")
            opc = int(input("Digite una opcion-:  "))
            if opc == 1:
                self.__digitarDatos()
            elif opc == 2:
                self.__listarDatos()
            elif opc == 3:
                self.__buscarDatos()
            elif opc == 4:
                self.__Estadistica()
            elif opc == 5:
                self.__salir()
                os._exit(1)
            else:
                self.__errorOpcion()
        except:
            print("error opcion (try)")
            system("pause")
            self.menu()
#tk.Grid() # Label con string vacia (Se usa para especifiicar la posición relativa de la etiqueta)

# No se muestran automaticamente necesitan un manejador de geometria
label = tk.Label(root, text="Sukoku", font=("Arial", 50))
label.pack(padx = 30, pady= 10)


textbox = tk.Text(root, font=("Arial", 25) , height="3") ## Puede scrollear con enter
textbox.pack()

''' Para una contraseña sería mejor una entrada'''
myentradada = tk.Entry(root)
myentradada.pack(padx= 2)

#Botones en Tkinter
Eleccion = tk.Menu (root)
Eleccion.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight= 1)
buttonframe.columnconfigure(1, weight= 1)
buttonframe.columnconfigure(2, weight= 1)
buttonframe.columnconfigure(3, weight= 1)
buttonframe.columnconfigure(4, weight= 1)
buttonframe.columnconfigure(5, weight= 1)
buttonframe.columnconfigure(6, weight= 1)
buttonframe.columnconfigure(7, weight= 1)
buttonframe.columnconfigure(8, weight= 1)

buttonframe.rowconfigure(0, height )


''' Grid takes the parameters row and column
#Sticky es para que los botones queden todos juntos, como la calculaadora, no los 3 botones de un tamaño n en el medio de la nada
# ASi es Sticki en el Oeste (W) y en el este (E)'''

# The buttons are going to be inside the button frame and the button frame is going to be inside the root
btn1 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn1.grid(row = 0, column=1 , sticky=tk.W+tk.E) 

btn2 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn2.grid(row = 0, column=2 , sticky=tk.W+tk.E) 

btn3 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn3.grid(row = 0, column=3 , sticky=tk.W+tk.E) 

btn4 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn4.grid(row = 0, column=4 , sticky=tk.W+tk.E) 

btn5 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn5.grid(row = 0, column=5 , sticky=tk.W+tk.E) 

btn6 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn6.grid(row = 0, column=6 , sticky=tk.W+tk.E) 

btn7 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn7.grid(row = 0, column=7 , sticky=tk.W+tk.E) 

btn8 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn8.grid(row = 0, column=6 , sticky=tk.W+tk.E) 
btn6 = tk.Button(buttonframe, text=" ", font=('Arial', 18))
btn6.grid(row = 0, column=6 , sticky=tk.W+tk.E) 


btn1 = tk.Butoon()

root.mainloop() # Puts everything on display and responds to use input