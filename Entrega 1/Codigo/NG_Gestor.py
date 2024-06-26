
from openpyxl import Workbook
from datetime import datetime

from HR_GenerarObjetos import generarObjetos

class Gestor:
    def __init__(self) -> None:
        self._vinos = []
        self.cargar_vinos(generarObjetos())
        #! Manipulamos datos desde el gestor
        self.valores_tipos_archivos = ["Excel", "PDF", 'Mostrar Por Pantalla']
        self.valores_tipos_resenias = ["Reseñas Somelier", "Reseñas Amigos", "Reseñas Normales"]
    
    def cargar_vinos(self, vinos):
        for vino in vinos:
            self._vinos.append(vino)
    
    def generarRankingVinos(self, periodo, tipo, archivo):
        vinos = self.buscarVinosConReseniasEnPeriodo(periodo, tipo)
        puntajes = self.calcularPuntajeDeSomelierEnPeriodo(vinos, periodo)
        puntajes_ordenados = self.ordenarVinoPuntajeMayor(puntajes)
        datos_vinos = self.obtenerDatosVinoParaRanking(puntajes_ordenados[:10])
        if archivo == "Excel":
            self.exportarExcel(datos_vinos)
            
    def buscarVinosConReseniasEnPeriodo(self, periodo, tipo):
        vinos_cumplen = []
        for vino in self._vinos:
            if vino.tenesReseniasDeTipoEnPeriodo(periodo, tipo):
                #print(vino)
                vinos_cumplen.append(vino)
            else:
                continue
        return vinos_cumplen
    
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos, periodo):
        vinos_puntaje = []
        for vino in vinos:
            #print(vino)
            puntaje = vino.calcularPuntajeDeSomeleierEnPeriodo(periodo)
            vinos_puntaje.append([vino,puntaje])
        return vinos_puntaje

    
    def ordenarVinoPuntajeMayor(self, lista):
        for a in range(len(lista)):
            for b in range(len(lista)):
                if lista[a][1] > lista[b][1]:
                    menor = lista[b]
                    mayor = lista[a]
                    lista[a] = menor
                    lista[b] = mayor
        return lista
    
    def obtenerDatosVinoParaRanking(self, vinos):
        formatos = []
        for vino, promedio in vinos:
            nombre = vino.nombre
            calificacionSom = vino.notaCata
            calificacionGen = promedio
            precio = vino.precio
            datosBodega = vino.obtenerDatosBodega()
            bodega = datosBodega[0]
            varietales = self.obtenerPorcentajeVarietales(vino)
            """varietales = ''
            for varietal in vino.varietal:
                varietales += varietal.mostrarPorcentaje()"""
            region = datosBodega[1][0]
            pais = datosBodega[1][1]
            formatos.append([nombre, calificacionSom, calificacionGen, precio, bodega, varietales, region, pais])
        return formatos
    
    def obtenerPorcentajeVarietales(self, vino):
        varietales = ''
        for varietal in vino.varietal:
            varietales += varietal.mostrarPorcentaje()
        return varietales
    
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
    

if __name__ == '__main__':
    gestor = Gestor()
    # (fecha_d,fecha_h),tipo,archivo
    fecha_d = 1