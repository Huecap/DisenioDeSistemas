import random
from datetime import date, datetime
from NG_Resenias import Resenia
from NG_Maridaje import Maridaje
from NG_Varietal import Varietal
# from NG_Bodega import Bodega



class Vino():
    def __init__(self, aniada:str, imagen_etiqueta:bin, nombre:str, nota_de_cata_bodega:float, precio_ARS:float, maridaje:Maridaje, varietal:Varietal, bodega:object):
        self._aniada = aniada
        self._imagen = imagen_etiqueta #Cambie el nombre
        self._nombre  = nombre 
        self._notaCata  = nota_de_cata_bodega
        self._precioArs  = precio_ARS
        self._resenias = []
        self._maridaje = maridaje 
        self._varietal = varietal 
        self._bodega = bodega
        
    
    # Getters 
    @property    
    def aniada(self):
        return self.__aniada
    
    @property    
    def varietal(self):
        return self._varietal
    
    @property 
    def imagen(self):
        return self._imagen 
    
    @property
    def nombre(self):
        return self._nombre 
    
    @property
    def notaCata(self):
        return self._notaCata 
    
    @property
    def precio(self):
        return self._precioArs  
    
    # Setters
    @imagen.setter
    # ! Agregar Validaciones 
    def imgaen(self, imagen):
        self._imagen  = imagen
        
    @notaCata.setter
    def image(self, notaCata):
        self._notaCata  = notaCata
    
    @precio.setter
    def precio(self, precio:float):
        self._precioArs  = precio 
    

    def __str__(self) -> str:
        mensaje = f'\n--- Vino {self._nombre } --- \n'
        mensaje += f'- Añada = {self._aniada} \n'
        mensaje += f'- Nota Cata = {self._notaCata} \n'
        mensaje +=  f'- Precio = {self._precioArs} (Pesos Argentinos)\n'
        mensaje +=  f'- Cantidad de resenias = {len(self._resenias)} \n'
        return mensaje
    

    def reseniarPremium(self, resenia:tuple):
        """Permite agregar una reseña de un somelier al vino

        :param resenia: Tupla 2 valores (comentario:str, puntaje:float)
        :type resenia: tuple
        """
        # Tecnicamente al momento de crear la resenia, tendría que tomar la fecha del día
        # TODO - Verificar metodo para poder cargar resenias desde un archivo
        fecha = datetime.now()
        resenia = Resenia(self, resenia[0], resenia[1], True, fecha)
        self._resenias.append(resenia)
    
    def reseniarUsuario(self, resenia:tuple):
        """Permite agregar una reseña normal al vino

        :param resenia: Tupla 2 valores (comentario:str, puntaje:float)
        :type resenia: tuple
        """
        fecha = datetime.now()
        resenia = Resenia(self, resenia[0], resenia[1], False, fecha)
        self._resenias.append(resenia)
    
    def mostrarResenias(self):
        if len(self._resenias) > 0:
            mensaje = "\n"
            for n in self._resenias:
                mensaje += n.__str__()
                mensaje += "  \n ----------------------- \n"
            return mensaje
        else: 
            mensaje = "No hay reseñas que mostrar"
    
    def tenesReseniasDeTipoEnPeriodo(self, periodo, tipo):
        for resenia in self._resenias:
            if resenia.sosDePeriodo(periodo) and resenia.sosDeTipo(tipo):
                return True
            else:
                continue
        return False
                
    def obtenerDatosBodega(self):
        nombre = self._bodega.nombre
        #regionYPais = self._bodega.obtenerRegionYPais()
        region = self._bodega.obtenerRegion()
        #return (nombre, regionYPais)
        return (nombre, region)
    
    def obtenerVarietal(self):
        descripciones = []
        for descripcion in self._varietal:
            descripciones.append(descripcion)
        return descripciones
    
    def calcularPuntajePromedio(self, puntajes):
        longitud = len(puntajes)
        total = 0
        if longitud > 0:
            for puntaje in puntajes:
                total += puntaje
            return total/longitud
        else:
            return 0
    
    def calcularPuntajeDeSomelierEnPeriodo(self, periodo):
        puntajes = []
        for resenia in self._resenias:
            if resenia.sosDePeriodo(periodo) and resenia.sosDeTipo("Reseñas Somelier"):
                puntajes.append(resenia.puntaje)
            else:
                continue
        promedio = self.calcularPuntajePromedio(puntajes)
        
        return promedio
    
    def obtenerPorcentajeVarietales(self):
        varietales = ''
        for varietal in self.varietal:
            varietales += varietal.mostrarPorcentaje()
        return varietales
    
    def contarResenias(self):
        return len(self._resenias)
    
    def calcularRanking(self):
        pass
    
    def compararEtiqueta(self):
        pass
    
    def esDeBodega(self):
        pass
    
    def esDeRegionVitivinicola(self):
        pass

    #! ------- Agregar funcion para Cargar Resenias (cuando las reseñas ya se instanciaron indicando premium o no)
    def cargar_resenia(self, resenia:Resenia):
        self._resenias.append(resenia)


if __name__ == "__main__":
    
    vino1 = Vino("100 % Lucha", "Imagen.jpg", "Toro", 10, 200.67 )
    #print(vino1)
    
    # Cargar resenias 
    for n in range(10):
        if ((n % 2) == 1):
            vino1.reseniarPremium(("Muy Bueno", random.randrange(0,5)+round(random.random(), 2)))
        else:
            vino1.reseniarUsuario(("Muy Bueno", random.randrange(0,5)+round(random.random(), 2)))
            
    #print(vino1)
    #print(vino1.mostrarResenias())