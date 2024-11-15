import tkinter
import customtkinter as custk

custk.set_appearance_mode("System") #Modos (default System )(light) (dark)
custk.set_default_color_theme("green")  ## Temas blue (default)

root = custk.CTk()
root.geometry("200 X 200") 
#Es de custk pq la ventana se creo con custom
#instanciado objeto tipo ventaja custk

def button_function():
    print("button pressed")



button = custk.CTkButton(master=root,font=("Arial", 23),text="Sudoku ", command=(button_function))

button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
 ## el argumento de relx va de 0 a 1 y es el % del alineamiento en PANTALLA COMPLETA
root.mainloop()