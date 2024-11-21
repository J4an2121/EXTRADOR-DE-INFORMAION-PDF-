
import fitz #que permite abrir y leer archivos PDF.
import pandas as pd  #manipular datos en forma de tablas
from tkinter import filedialog # permite abrir una ventana para que el usuario seleccione archivos o carpetas.
import os #utas de archivos y carpetas en el sistema


#no permite abrir el archivo que necesitamos
ruta_archivo = filedialog.askopenfilename(title="Selecciona el archivo")
#ruta_archivo = r"C:\Users\neoki\OneDrive\Escritorio\iva.pdf"
 
#Se crea un DataFrame vacío con tres columnas 
df = pd.DataFrame(columns = ['Id', 'Factura', 'monto' ])
pos = 0 #se usa para mantener el índice de las filas.
 

with fitz.open(ruta_archivo) as doc: #abre el archivo PDF.

    texto = ""
    for page in doc:
        texto = page.get_text() #  permite  extrar el texto de cada página


        #Luego, se buscamos los  datos específicos dentro del texto extraído usando la función partition, que separa el texto en función de palabras clave.

        id = texto.partition(" No.  ")[2].partition(" ")[0].partition("/")[0][:-3].strip()
        fact = texto.partition("SERIE FACTURA")[2].partition(" ")[0][1:11].strip()
        texto_anterior = texto.partition("3125831")[0]
        lineas = texto_anterior.strip().splitlines()
        
        monto = lineas[-1].strip() if lineas else ""
        

        #print(id,fact,monto)
        df.loc[pos] = [id,fact,monto] 
        pos += 1
        #print("*************")
        #print(texto)
        #print("-------------")
 
ruta_salida = filedialog.askdirectory(title="Seleccione la carpeta de salida")
df.to_excel(os.path.join(ruta_salida, "Salida.xlsx"), index = False)
 
