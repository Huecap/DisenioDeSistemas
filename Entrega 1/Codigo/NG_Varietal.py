from NG_TipoUva import TipoUva

class Varietal:
    
    def __init__(self, descripcion:str, porcentaje_composicion:list) -> None:
        """Metodo creador de Varietal

        :param descripcion: Descripcion del varietal
        :type descripcion: str
        :param porcentaje: Lista que contiene tuplas con el tipo de uva y el porcentaje [("Chardonnay", 70)]
        :type porcentaje: list[tuple(TipoUva, int)]
        """
        self._descripcion = descripcion
        self._porcentaje_composicion = porcentaje_composicion
        
    def conocerTipoUva(self):
        tipos_uva = []
        for uva in self._porcentaje_composicion:
            tipos_uva.append(uva[0].nombre)
        return tipos_uva
    
    def esDeTipoUva(self, tipo):
        for uva in self._porcentaje_composicion:
            if uva[0] == tipo:
                return True
        return False
    
    def obtenerPorcentaje(self):
        mensaje = ''
        for uva in self._porcentaje_composicion:
            mensaje += f'- Uva: {uva[0].nombre} {uva[1]}% \n'
        return mensaje
    
if __name__ == "__main__":
    uvas_argentinas = [
    "Malbec",
    "Bonarda",
    "Cabernet Sauvignon",
    "Chardonnay",
    "Merlot",
    "Syrah",
    "Sauvignon Blanc",
    "Torrontés",
    "Pinot Noir",
    "Semillón"
]
    descripciones = ["Muy buena"]
    instancias_uvas = []
    for uva in uvas_argentinas:
        instancias_uvas.append(TipoUva(uva,"Muy buena"))
    
    varietal1 = Varietal("Malbec", [(instancias_uvas[0], 80), (instancias_uvas[1], 20)])
    print(varietal1.mostrarPorcentaje())
    print(varietal1.esDeTipoUva(instancias_uvas[2]))
    print(varietal1.conocerTipoUva())