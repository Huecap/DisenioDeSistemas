
from openpyxl import Workbook
from datetime import datetime

from HR_GenerarObjetos import generarObjetos
from NG_PatronStrategy import * 
from HR_archivos import InterfazExcel, InterfazPDF

class Gestor:
    def __init__(self) -> None:
        self._vinos = []
        self._paises = generarObjetos()[1]
        self.cargar_vinos(generarObjetos()[0])
        #! Manipulamos datos desde el gestor
        self.valores_tipos_archivos = ["Excel", "PDF", 'Mostrar Por Pantalla']
        self.valores_tipos_resenias = ["Reseñas Somelier", "Reseñas Amigos", "Reseñas Normales"]
        # Estrategia 
        self._estrategiaGenerarResenia = None
        self._interfazExel = InterfazExcel()
        self._interfazPDF = InterfazPDF()
    
    @property
    def estrategiaGenerarResenia(self):
        return self._estrategiaGenerarResenia
    
    @estrategiaGenerarResenia.setter
    def estrategiaGenerarResenia(self, estrategia):
        self._estrategiaGenerarResenia = estrategia
    
    def cargar_vinos(self, vinos):
        for vino in vinos:
            self._vinos.append(vino)
        
    def cargar_paises(self, paises):
        for pais in paises:
            self._paises.append(pais)
    
    def generarRankingVinos(self, periodo:tuple, tipo:str, archivo:str):
        self.estrategiaGenerarResenia = self.crearEstrategia(tipo)
        datos_vinos = self.estrategiaGenerarResenia.generarRankingVinos(periodo, self._vinos, self._paises)
        if archivo == "Excel":
            self._interfazExel.exportarExcel(datos_vinos)
        elif archivo == "PDF":
            datos = ' ---- RANKING VINOS ---- \n \n \n \n'
            for fila in datos_vinos:
                for dato in fila:
                    datos += str(dato)
                datos += '\n\n\n'
            self._interfazPDF.crear_pdf_con_reportlab("datos_vinos.pdf", datos)

    # ! Crear la estrtegia 
    
    def crearEstrategia(self, tipoEstrategia:str) -> IEstrategiaResenia:
        if tipoEstrategia == "Reseñas Somelier":
            tipoResenia = EstrategiaReseniaSomelier()
        elif tipoEstrategia == "Reseñas Amigos":
            tipoResenia = EstrategiaReseniaSomelier()
        elif tipoEstrategia == "Reseñas Normales":
            tipoResenia = EstrategiaReseniaSomelier()
        print(tipoResenia)
        return tipoResenia
    
        
        
    # ! Importar la clase strategy

if __name__ == '__main__':
    gestor = Gestor()
    # (fecha_d,fecha_h),tipo,archivo
    fecha_d = 1
    for n in gestor._paises:
        print(n)