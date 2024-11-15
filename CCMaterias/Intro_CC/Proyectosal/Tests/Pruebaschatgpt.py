import tkinter as tk
class HealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selecciona tu motivo principal")
        
        # Crear un label de instrucciones
        self.label = tk.Label(root, text="Selecciona tu objetivo principal para hacer ejercicio:")
        self.label.pack(pady=10)
        
        # Variable para guardar la selección del usuario
        self.selected_goal = tk.StringVar()
        
        # Crear botones de radio para las opciones
        self.goals = {
            "Perder Peso": "perdida_peso",
            "Ganar Masa Muscular": "ganar_masa_muscular",
            "Mejorar Resistencia": "mejorar_resistencia",
            "Salud General": "mejorar_salud_general"
        }
        
        for text, value in self.goals.items():
            tk.Radiobutton(root, text=text, variable=self.selected_goal, value=value).pack(anchor="w")
        
        # Botón para confirmar la selección
        self.submit_button = tk.Button(root, text="Confirmar", command=self.confirm_selection)
        self.submit_button.pack(pady=20)
    
    def confirm_selection(self):
        selected_value = self.selected_goal.get()
        if selected_value:
            tk.messagebox.showinfo("Selección Confirmada", f"Has seleccionado: {selected_value}")
            # Aquí se puede pasar el valor seleccionado a otra función para análisis
            self.analyze_selection(selected_value)
        else:
            tk.messagebox.showwarning("Advertencia", "Por favor, selecciona un objetivo antes de continuar.")

    def analyze_selection(self, goal):
        # Aquí es donde realizas el análisis en función de la selección del usuario.
        print(f"Analizando datos para el objetivo: {goal}")
        # Aquí se puede integrar con la lógica del proyecto.
        # Por ejemplo, usando la función que creamos antes:
        # datos = objetivos_ejercicio[goal]
        # print(f"Calorías recomendadas: {datos['calorias_diarias']['mujeres']} kcal")
        # O puedes redirigir al usuario a la siguiente sección del programa.
        self.root.destroy()
        # Aquí seguiría el código para la siguiente fase de la aplicación
        # como mostrar una gráfica o alguna otra funcionalidad.



if __name__ == "__main__":
    root = tk.Tk()
    app = HealthApp(root)
    root.mainloop()