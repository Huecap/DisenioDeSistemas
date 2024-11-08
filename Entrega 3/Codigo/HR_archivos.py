from openpyxl import Workbook
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class InterfazExcel():
    
    def exportarExcel(self, lista):
        # Crear un nuevo libro de trabajo y seleccionar la hoja activa
        wb = Workbook()
        ws = wb.active
        # Escribir los encabezados en la primera fila
        encabezados = ["Nombre", "Calificación somelier", "Calificación general", "Precio sugerido", "Nombre de bodega", "Varietal", "Región", "País"]
        ws.append(encabezados)
        for fila in lista:
            ws.append(fila)
        #Guardar el archivo Excel
        wb.save('RankingVinos.xlsx')
 
 
class InterfazPDF():

    def crear_pdf_con_reportlab(self, nombre_archivo , datos):
        # Configuración de la página
        pdf = canvas.Canvas(nombre_archivo, pagesize=A4)
        ancho, alto = A4

        # Configuración de la fuente
        pdf.setFont("Helvetica", 12)

        # Crear un objeto TextObject para manejar el texto con saltos de línea
        text_object = pdf.beginText(100, alto - 100)  # Comienza en las coordenadas (100, alto - 100)
        text_object.setFont("Helvetica", 12)

        # Texto con saltos de línea (usando \n para representar los saltos)
        texto_con_saltos = datos.replace("\n", "<br/>")  # Reemplazar saltos de línea por <br/>

        # Agregar el texto línea por línea
        for linea in texto_con_saltos.split("<br/>"):
            text_object.textLine(linea)  # Añadir una línea de texto en el PDF

        # Dibujar el texto en el PDF
        pdf.drawText(text_object)

        # Agregar una línea
        pdf.line(100, alto - 120, 400, alto - 120)

        # Guardar y cerrar el PDF
        pdf.showPage()
        pdf.save()

# if __name__ == "__main__":

# Llamada a la función
    #crear_pdf_con_reportlab("ejemplo_reportlab.pdf", [["hOLA", "hOLA"]])