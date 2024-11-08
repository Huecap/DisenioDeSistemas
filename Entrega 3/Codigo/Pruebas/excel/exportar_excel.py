import json
from openpyxl import Workbook

# Cargar los datos del archivo JSON
with open('vinos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

lista = []
for fila in data:
    lista.append([fila.get("nombre", ""),
        fila.get("calificacion_somelier", ""),
        fila.get("calificacion_general", ""),
        fila.get("precio_sugerido", ""),
        fila.get("nombre_bodega", ""),
        fila.get("varietal", ""),
        fila.get("region", ""),
        fila.get("pais", "")])
print(lista)


# Crear un nuevo libro de trabajo y seleccionar la hoja activa
wb = Workbook()
ws = wb.active

# Escribir los encabezados en la primera fila
encabezados = ["Nombre", "Calificación somelier", "Calificación general", "Precio sugerido", "Nombre de bodega", "Varietal", "Región", "País"]
ws.append(encabezados)
for fila in lista:
    ws.append(fila)


#Guardar el archivo Excel
wb.save('vinos.xlsx')