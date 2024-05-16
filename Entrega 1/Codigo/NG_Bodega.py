import random
from datetime import date
from NG_Geografia import RegionVitivinicola
from NG_Vino import Vino

class Bodega:
    def __init__(self, nombre:str, descripcion:str, historia:str, region:RegionVitivinicola, coordenadasUbicacion:str, periodoActualizacion:date) -> None:
        self._nombre = nombre
        self._descripcion = descripcion
        self._historia = historia
        self._region = region
        self._coordenadas = coordenadasUbicacion
        self._periodoActualizacion = periodoActualizacion
        self._vinos = []
        
    def cargar_vino(self, vino:Vino):
        """Permite cargar un vino

        :param vino: Vino ya instanciado
        :type vino: Vino
        """
        self._vinos.append(vino)
        
    def mostrarTodosVinos(self):
        """Retorna una cadena con todos los nombres de los vinos

        :return: Cadena con todos los vinos de la bodega
            En caso de que no tenga vinos lo indica
        :rtype: _type_
        """
        if len(self._vinos) > 0:
            mensaje = f'\n ** Vinos de la bodega {self._nombre} ** \n'
            for vino in self._vinos:
                mensaje += f' - {vino.nombre} \n'
            return mensaje
        else:
            mensaje = "Todavía no hay vinos asociados a esta Bodega"
            
    def contarResenias(self):
        """Retorna la cantidad de reseñas que tiene la bodega asociada a todos los vinos

        :return: Sumatoria de todas las reseñas de todos los vinos
        :rtype: int
        """
        cantidad = 0
        for vino in self._vinos:
            cantidad += vino.contarResenias()
        return cantidad
        
    def __str__(self):
        mensaje = f'--- Bodega {self._nombre} --- \n'
        mensaje += f'- Descripcion: {self._descripcion}\n'
        mensaje += f'- Historia: {self._historia} \n'
        mensaje += f'- RegionVitivinicola: {self._historia}\n'
        mensaje += f'- Coordenadas: {self._coordenadas}\n'
        mensaje += f'- Vinos disponibles: {self.mostrarTodosVinos()}\n \n'
        return mensaje
        
if __name__ == "__main__":
    bodega1 = Bodega("Sueños de Oro", "Buenos vinos", "Teniamos sed y mucha sed", "Cordoba", "11111111", date.today())
    
    print(bodega1)
    vino1 = Vino("100 % Lucha", "Imagen.jpg", "Toro", 10, 200.67 )
    # print(vino1)
    
    # Cargar resenias 
    for n in range(10):
        if ((n % 2) == 1):
            vino1.reseniarPremium(("Muy Bueno", random.randrange(0,5)+round(random.random(), 2)))
        else:
            vino1.reseniarUsuario(("Muy Bueno", random.randrange(0,5)+round(random.random(), 2)))
    bodega1.cargar_vino(vino1)
    print(bodega1)
    print(bodega1.contarResenias())
    