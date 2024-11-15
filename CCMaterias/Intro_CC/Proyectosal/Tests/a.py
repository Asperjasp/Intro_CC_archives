''' Las calorías vacías son las que proporcionan poco o ningún valor nutricional.
 Algunos ejemplos de alimentos con calorías vacías son las pop-tarts, los cereales con azúcar, las gaseosas, los donuts, y las golosinas.'''
import matplotlib.pyplot as plt  # Graficas 
import tkinter as tk # Interfaz gráfica
import customtkinter as Ctk # Mejorar interfaz
# Datos que ya tiene Sara para icoporar en el analisis
 # Nombre apodo cumpleaños, estatura, peso, IMC, Edad 

import openpyxl # Leer Excel 
import pandas as pd # Usar datos en dataframe (Matriz) y 
import numpy as np
global Dietatotal, Dietadesayuno, Dietalmuerzo, Dietacena
global DFali # Para que al usarlo en funciones no haya problemas ya que es el main dataframe
# Pandas necesita la dependencia de openpyxl para leer excel pip install openpyxl usa el coman oopenpyxl.load_workbook()
#Lista de datos de los alimentos nutricionales

BDali="../Dieta/Comidacol.xlsx" # Asegurate de tenerlo en carpeta de nombre Dieta y evitar nombres que empiecen con n para evitar saltos de lineas no pensados
Usuariospasados="../Dieta/Datosusuariospasados.xlsx" # Asegurate de tenerlo en carpeta de nombre Dieta y evitar nombres que empiecen con n para evitar saltos de lineas no pensados
try:
    DFali = pd.read_excel(BDali, sheet_name='comida', engine="openpyxl", index_col=False)  # Cabeceras en 0 por default 
except ImportError:
    print("Falta la dependencia 'openpyxl'. Instala la librería con 'pip install openpyxl'. ")
# try: #Past users
#         PU = pd.read_excel(Usuariospasados, engine="openpyxl", index_col=False)  # Cabeceras en 0 por default 
# except ImportError:
#     print("Falta la dependencia 'openpyxl'. Instala la librería con 'pip install openpyxl'. ")



################################################

# Datos = Extraerdatosnutricionales([[3,150]])
# for item in [[3,150], [5,1]]:
#         indice = item[0]
#         cantidad = item[1]
#         print(indice)
#         print(cantidad)
# print (Datos)

# print(Datos)




## print(DFali.index[1]  Para testear que saca  sigue indexando las filas desde 0 asi en el excel esten indexadas desde 1
# Mostrar las opciones
#print(DFali.iloc[0,0])"


## ########Pruebas #######

# Ya no ahce falta
def Opciones(): # FUNCIÓN: Imprime toda la lista de alimentos
    print("A continuación tiene la lista de alimentos\n")   #Muestra las opciones de comida
    ## Para que no salga una lista enorme de 1 columna  Hallamos la amxima longitud de la lsita con Dfali y la dividmos en 4 pedazos por ejemplo
    n = 4  # Número de partes
    total_filas = DFali.shape[0]
    filas_por_parte = total_filas // n
    for i in range(n):
        inicio = i * filas_por_parte
        fin = inicio + filas_por_parte if i != n - 1 else total_filas # Para que termine
        print(DFali.iloc[inicio:fin,0])   # Para que vaya en intervalos por ejemplo si el tamaño fuera 21 [1,5][6,10]..y el ultimo le añade el residuo [15,21]


def Opciones(): # FUNCIÓN: Imprime tooda la lista de alimentos
    print("A continuación tiene la lista de alimentos\n")   #Muestra las opciones de comida
    ## Para que no salga una lista enorme de 1 columna  Hallamos la amxima longitud de la lsita con Dfali y la dividmos en 4 pedazos por ejemplo
    n = 4  # Número de partes
    total_filas = DFali.shape[0]
    filas_por_parte = total_filas // n
    for i in range(n):
        inicio = i * filas_por_parte
        fin = inicio + filas_por_parte if i != n - 1 else total_filas # Para que termine
        print(DFali.iloc[inicio:fin,0])   # Para que vaya en intervalos por ejemplo si el tamaño fuera 21 [1,5][6,10]..y el ultimo le añade el residuo [15,21]

def Almacenarnuevo(nombre, calorias, proteinas, grasas, carbohidratos, colesterol): # Funcion que guarda un nuevo elemento en el excel
    # Verificar si el alimento ya existe en el DataFrame para evitar repetidos
    if nombre in DFali['Nombre'].values: ##  QUE VERIFIQUE EN LA LISTA DEL excel  .values
        print(f"El alimento {nombre} ya existe en la base de datos.")
        return
    # Crear un nuevo DataFrame con el nuevo alimento
    nuevo_alimento = pd.DataFrame({
    'Nombre': [nombre],  # Deben coincidir el nombre de los datos con la cabecera del excel a la hora de enviarlo a este 
    'Calorías (kcal)': [calorias],
    'Proteínas (g)': [proteinas],
    'Grasas (g)': [grasas],
    'Carbohidratos (g)': [carbohidratos],
    'Colesterol (mg)': [colesterol]
})
        # Añadir un índice para el nuevo alimento
    nuevo_alimento.index = [DFali.index.max() + 1] 

    # Añadir el nuevo alimento al DataFrame existente
    BFactuali = pd.concat([DFali, nuevo_alimento], ignore_index=False) ## Añade el nuevo elemento con sus caracteristicas al frame
    #https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat
    # Guardar el DataFrame actualizado en el archivo Excel
    BFactuali.to_excel(BDali, sheet_name='comida', index=True, engine="openpyxl")
    


def Introducirnuevo(): ## Recibe la información de nuevos alimentos en caso de necesitarse
    nombre = input("Introduce el nombre del alimento: ").capitalize()
    calorias = float(input("Introduce las calorías por 100g: "))
    proteinas = float(input("Introduce las proteínas (g): "))
    grasas = float(input("Introduce las grasas (g): "))
    carbohidratos = float(input("Introduce los carbohidratos (g): "))
    colesterol = float(input("Introduce la cantidad de colesterol (g): "))
    
    # Almacenar el nuevo alimento en el archivo Excel
    Almacenarnuevo(nombre, calorias, proteinas, grasas, carbohidratos,colesterol)

    print(f"{nombre} ha sido añadido a la base de datos. Gracias por su aporte.")

# Ejemplo de uso
def verificarnueva(): # Verificar si las opciones marcadas de si o ono con validas
    verificar = int(input())
    if (verificar != 0 and verificar != 1):
        return(-1) # Error 
    else:
        return verificar

def Preguntarnuevo(tipo):  # Para DEjar al usuario añadir comida nueva cuando quiera
    stop = True
    while(stop):
        print(f"Hay alguna comida en su {tipo} que no se encuentre en la lista si es asi digite 0 sino digite 1")
        verificacion = verificarnueva()
        if (verificacion == 0):
            Introducirnuevo()  ## Introduce nuevo elemento lo que le pide los datos y los guarda en el excel
        elif(verificacion == 1): # Cuando digite otro (entre ellos el 1) dejara de preguntar nuevo
            stop = False
        else:
            # Si no cumple puede imprimir verificacion y ver que da -1 para error de didgitación 
            print("Error de digitación Ingrese otro valor ")


def Dietausuario(Desayuno):
    
    while True:
        try:
            indice = int(input("Selecciona el índice del alimento que consumes (-1 para terminar): "))
        except: TypeError
        
        if indice == -1:
            break
        
        if (1 <= indice <= DFali.shape[0]): # Para saber el total de filas del excel
            cantidad = float(input("Introduce la cantidad aproximada que consumes (en gramos o ml): "))
            Desayuno.append([indice, cantidad]) # Añade a la lsita el indice de la lista que consume para analizar mas tarde
        else:
            print("Índice no válido. Por favor, intenta de nuevo.")    
        
    return Desayuno
def Caldesayuno(Dietadesayuno):
    Opciones()
    tipo = "Desayuno"
    Preguntarnuevo(tipo) #Le pregunta si hay algun nuevo elemento nuevo
    Dietadesayuno = Dietausuario(Dietadesayuno)
    return Dietadesayuno
def Calmuerzo(Dietalmuerzo):
    Opciones()
    tipo = "Almuerzo"
    Preguntarnuevo(tipo) #Le pregunta si hay algun nuevo elemento nuevo
    Dietalmuerzo = Dietausuario(Dietalmuerzo)
    return Dietalmuerzo
def Calcena(Dietacena):
    Opciones()
    tipo = "Cena"
    Preguntarnuevo(tipo) #Le pregunta si hay algun nuevo elemento nuevo
    Dietacena = Dietausuario(Dietacena)
    return Dietacena

# Iterar sobre cada alimento en la lista
def Extraerdatosnutricionales(Dietausu): # Encontrar el tamaño de todo 
    total_calorias = 0
    total_grasas = 0
    total_proteinas = 0
    total_carbohidratos = 0
    total_colesterol = 0
    resultados_nutricionales = []
    for item in Dietausu:
        indice = item[0]
        cantidad = item[1]
        if indice < len(DFali):
            alimento = DFali.iloc[indice-1] 
            total_calorias += alimento['Calorías (kcal)'] * (cantidad / 100)
            total_grasas += alimento['Grasas (g)'] * (cantidad / 100)
            total_proteinas += alimento['Proteínas (g)'] * (cantidad / 100)
            total_carbohidratos += alimento['Carbohidratos (g)'] * (cantidad / 100)
            total_colesterol += alimento['Colesterol (mg)'] * (cantidad / 100)
        else: 
            print(f"Indice {indice} no encontrado en el data frame")
    return [total_calorias, total_grasas, total_proteinas, total_carbohidratos, total_colesterol]

 # Mostrar la lista final con los resultados nutricionales
'''Para poder visualizar los datos que tengamos, estos se deben añadir a los ejes. La manera de hacerlo es mediante métodos de ploteo que trae el objeto Axes. El más básico de todos es plot,
   el cual crea un gráfico lineal y requiere los datos del eje X y Y como argumentos.
   
   Personalizar un Plot
   label='name' → pone una etiqueta al plot para saber a qué corresponde cada color
 (muy útil cuando vas a poner varias gráficas en un solo plot).
   '''
Categorias = ['Desayuno', 'Almuerzo', 'Cena', 'Total'] 
Subcategorias = ['Calorías (kcal)', 'Grasas (g)', 'Proteínas (g)', 'Carbohidratos (g)', 'Colesterol (mg)' ]
'''Para graficar
 Barras adyacentes : https://www.analyticslane.com/2022/07/05/graficos-de-barras-en-matplotlib/
 Documentación matplotlib https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide'''
def graficarcom(valornutriocionaldes, valornutriocionalal, valornutriocionalcen, valornutricionaltotal):
    # Crear un array de los valores para cada categoría
    data = np.array([valornutriocionaldes, valornutriocionalal, valornutriocionalcen, valornutricionaltotal])

    n = len(Categorias)
    x = np.arange(n)  # Posiciones para las categorías en el eje X
    width = 0.17  # Ancho de las barras

    # Crear la figura y el eje
    fig, ax = plt.subplots()

    # Graficar las barras para cada subcategoría
    for i in range(len(Subcategorias)):
        ax.bar(x + i * width - 2 * width, data[:, i], width=width, label=Subcategorias[i])

    # Etiquetas y título
    ax.set_xlabel('Comidas')
    ax.set_ylabel('Valores Nutricionales')
    ax.set_title('Valores Nutricionales por Comida')
    ax.set_xticks(x)
    ax.set_xticklabels(Categorias)
    ax.legend(loc='best')

    # Mostrar la gráfica
    plt.show()

# Llamar a la función con los datos

Categorias = ['Desayuno', 'Almuerzo', 'Cena', 'General']
Subcategorias = ['Calorías (kcal)', 'Grasas (g)', 'Proteínas (g)','Carbohidratos (g)', 'Colesterol (mg)' ]

# Crear el gráfico

def Dieta(): # Corre todo lo que consume el usuario  y lo guarda para analisis
 #Lista que contendra comida y cantidad TOTAL
    
# Listas  de  cada comida individual por el usuario
    Dietadesayuno =[] 
    Dietalmuerzo =[] 
    Dietacena =[] 
    Dietatotal= [] 

    Dietadesayuno = Caldesayuno(Dietadesayuno)
    Dietalmuerzo = Calmuerzo(Dietalmuerzo)
    Dietacena =Calcena(Dietacena)
    Dietatotal = Dietadesayuno + Dietalmuerzo + Dietacena
   
    # Extraer Datos nutricionales para graficar
    valornutriocionaldes = Extraerdatosnutricionales(Dietadesayuno)
    valornutriocionalal= Extraerdatosnutricionales(Dietalmuerzo)
    valornutriocionalcen= Extraerdatosnutricionales(Dietacena)

    valornutricionaltotal= [0,0,0,0,0]
    for i in range (len(Categorias) -1):
        valornutricionaltotal[i] = valornutriocionaldes[i]+ valornutriocionalal[i] + valornutriocionalcen[i]

    graficarcom(valornutriocionaldes, valornutriocionalal, valornutriocionalcen, valornutricionaltotal)

  

Dieta()

#     def analyze_selection(self, goal):
#         # Aquí es donde realizas el análisis en función de la selección del usuario.
#         print(f"Analizando datos para el objetivo: {goal}")
#         # Aquí se puede integrar con la lógica del proyecto.
#         # Por ejemplo, usando la función que creamos antes:
#         # datos = objetivos_ejercicio[goal]
#         # print(f"Calorías recomendadas: {datos['calorias_diarias']['mujeres']} kcal")
#         # O puedes redirigir al usuario a la siguiente sección del programa.
#         self.root.destroy()
#         # Aquí seguiría el código para la siguiente fase de la aplicación
#         # como mostrar una gráfica o alguna otra funcionalidad.



###########################################################################################33

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = HealthApp(root)
#     root.mainloop()
#





# def Recomendaciones():
#     df.plot(kind='bar')
# plt.title('Comparación de Nutrientes Consumidos vs Recomendados')
# plt.ylabel('Gramos')
# plt.show()

# '''
# On Linux, additionally you need to install the scrot application, as well as Tkinter:

# sudo apt-get install scrot

# sudo apt-get install python3-tk

# sudo apt-get install python3-dev'''
# # Scrot


# def calcular_ingesta_recomendada(edad, sexo, actividad_fisica):
#     # Datos de referencia según el perfil del usuario
#     if sexo == "masculino":
#         if actividad_fisica == "alta":
#             return 2500
#         else:
#             return 2000
#     else:
#         if actividad_fisica == "alta":
#             return 2000
#         else:
#             return 1600
# # Para contar iterativa mente las calorias  y etc     
# def repetir(lista, veces): #Para añadir el indice de la comida n veces y al final contar las calorias por la cantidad
#     # https://es.stackoverflow.com/questions/514254/repetir-n-veces-cada-elemento-de-una-lista-en-python
#     salida = []
#     for elemento in lista:
#         salida.extend([elemento] * veces)
#     return salida