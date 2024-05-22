
from openpyxl import Workbook

class Gestor:
    def __init__(self) -> None:
        self._vinos = []
        pass
    
    def generarRankingVinos(self, periodo, tipo, archivo):
        #(fecha_d,fecha_h),tipo,archivo
        vinos = self.buscarVinosConReseniasEnPeriodo(periodo, tipo)
        puntajes = self.calcularPuntajeDeSomelierEnPeriodo(vinos, periodo)
        puntajes_ordenados = self.ordenarVinos(puntajes)
        self.exportarExcel(puntajes_ordenados[:10])
    
    def buscarVinosConReseniasEnPeriodo(self, periodo, tipo):
        vinos_cumplen = {}
        for vino in self._vino:
            if vino.tenesReseniasDeTipoEnPeriodo(periodo, tipo):
                vinos_cumplen[vino.nombre] = [vino.nombre, vino.precio, vino.obtenerDatosBodega(), vino.obtenerVarietal()]
        
        return vinos_cumplen
    
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos, periodo):
        vinos_puntaje = []
        for vino in vinos:
            puntaje = vino.calcularPuntajeDeSomeleierEnPeriodo(periodo)
            vinos_puntaje.append([vino,puntaje])
        return vinos_puntaje
        pass
    """     resenias_vino.append(vino.obtenerReseniasDeTipoEnPeriodo(periodo, tipo))
            datos_bodega = vino.datos
            vinos_datos{vino:[resenias_vino, vino.nombre, vino.precio]}
            """
    def calcularPuntajeDeSomelierEnPeriodo():
        pass
    
    def ordenarVinos(self, lista):
        for a in range(len(lista)):
            for b in range(len(lista)):
                if lista[a][1] > lista[b][1]:
                    menor = lista[b]
                    mayor = lista[a]
                    lista[a] = menor
                    lista[b] = mayor
        return lista
    
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
    pass