from abc import ABC, abstractmethod


class IEstrategiaResenia(ABC):
        
    @abstractmethod
    def generarRankingVinos(self, periodo:tuple, vinos:list, paises:list) -> None:
        pass
    
    @abstractmethod
    def buscarVinosConReseniaEnPeriodo(self, perido:tuple, tipo:str) -> list:
        pass
    
    @abstractmethod
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos:list, perido:tuple) -> list:
        pass
    
    @abstractmethod
    def ordenarVinoPuntajeMayor(self, puntajes:list) -> list:
        pass
    
    @abstractmethod
    def obtenerDatosVinoParaRanking(self, puntajes_ordenados:list) -> list:
        pass
  
# ! ESTE TENEMOS QUE PONER  
class EstrategiaReseniaSomelier(IEstrategiaResenia):

    def generarRankingVinos(self, periodo:tuple, vinos:list, paises:list) -> list:
        vinos = self.buscarVinosConReseniaEnPeriodo(vinos, periodo)
        puntajes = self.calcularPuntajeDeSomelierEnPeriodo(vinos, periodo)
        puntajes_ordenados = self.ordenarVinoPuntajeMayor(puntajes)
        datos_vinos = self.obtenerDatosVinoParaRanking(puntajes_ordenados[:10], paises)
        return datos_vinos 
    

    def buscarVinosConReseniaEnPeriodo(self,vinos:list, periodo:tuple) -> list:
        vinos_cumplen = []
        for vino in vinos:
            if vino.tenesReseniasDeTipoEnPeriodo(periodo, "Reseñas Somelier"):
                #print(vino)
                vinos_cumplen.append(vino)
            else:
                continue
        return vinos_cumplen
    
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos:list, periodo:tuple) -> list:
        vinos_puntaje = []
        for vino in vinos:
            #print(vino)
            puntaje = vino.calcularPuntajeDeSomelierEnPeriodo(periodo)
            vinos_puntaje.append([vino,puntaje])
        return vinos_puntaje
    
    def ordenarVinoPuntajeMayor(self, puntajes:list) -> list:
        for a in range(len(puntajes)):
            for b in range(len(puntajes)):
                if puntajes[a][1] > puntajes[b][1]:
                    menor = puntajes[b]
                    mayor = puntajes[a]
                    puntajes[a] = menor
                    puntajes[b] = mayor
        return puntajes
    
    def obtenerDatosVinoParaRanking(self, puntajes_ordenados:list, paises:list) -> list:
        formatos = []
        for vino, promedio in puntajes_ordenados:
            nombre = vino.nombre
            calificacionGen = vino.notaCata
            calificacionSom = promedio
            precio = vino.precio
            datosBodega = vino.obtenerDatosBodega() #  nombre de la bodega y nombre de la region
            bodega = datosBodega[0]
            region = datosBodega[1]
            pais = self.obtenerPaisRegion(region, paises)
            # varietales = self.obtenerPorcentajeVarietales(vino)
            varietales = vino.obtenerPorcentajeVarietales()
            """varietales = ''
            for varietal in vino.varietal:
                varietales += varietal.mostrarPorcentaje()"""
            #region = datosBodega[1][0]
            #pais = datosBodega[1][1]
            formatos.append([nombre, calificacionSom, calificacionGen, precio, bodega, varietales, region, pais])
        return formatos
    
    def obtenerPaisRegion(self, region, paises):
        for pais in paises:
            #for provincia in pais._provincias:
               if pais.esTuRegion(region):
                #print(pais.nombre)
                return pais._nombre
                

        #print(pais.nombre)
    
    
    
    """def obtenerPorcentajeVarietales(self, vino):
        varietales = ''
        for varietal in vino.varietal:
            varietales += varietal.mostrarPorcentaje()
        return varietales"""    

class EstrategiaReseniaAmigos(IEstrategiaResenia):
    def generarRankingVinos(self, periodo:tuple, vinos:list, paises:list) -> list:
        pass 

    def buscarVinosConReseniaEnPeriodo(self,vinos:list, periodo:tuple) -> list:
        pass
    
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos:list, periodo:tuple) -> list:
        pass     
    def ordenarVinoPuntajeMayor(self, puntajes:list) -> list:
        pass 
    def obtenerDatosVinoParaRanking(self, puntajes_ordenados:list, paises:list) -> list:
        pass
   
    def obtenerPaisRegion(self, region, paises):
        pass
    
    
class EstrategiaReseniaNormal(IEstrategiaResenia):
        

    def generarRankingVinos(self, periodo:tuple, vinos:list, paises:list) -> list:
        pass 

    def buscarVinosConReseniaEnPeriodo(self,vinos:list, periodo:tuple) -> list:
        pass
    
    def calcularPuntajeDeSomelierEnPeriodo(self, vinos:list, periodo:tuple) -> list:
        pass     
    def ordenarVinoPuntajeMayor(self, puntajes:list) -> list:
        pass 
    def obtenerDatosVinoParaRanking(self, puntajes_ordenados:list, paises:list) -> list:
        pass
   
    def obtenerPaisRegion(self, region, paises):
        pass