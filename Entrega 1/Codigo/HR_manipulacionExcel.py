
"""import openpyxl

# Abre el archivo XLSX
libro = openpyxl.load_workbook(filename="BonVino - Modelo de Dominio 1-1.xlsx")

# Accede a hojas específicas (opcional)
hoja = libro['Hoja1']  # Suponiendo que tus datos estén en Hoja1

# Itera a través de filas y celdas
for fila in hoja.iter_rows():
    for celda in fila:
        print(celda.value)  # Accede al valor en cada celda

# (Opcional) Modifica los datos o crea nuevas hojas usando métodos Openpyxl

# Guarda los cambios (opcional)
libro.save(filename="Archivo.xlsx")  # Sobrescribe el archivo original
"""



if __name__ == "__main__":
    pass