
from NG_Resenias import Resenia

class Vino():
    def __init__(self, aniada:str, imagen:bin, nombre:str, notaCata:float, precioArs:float):
        self._aniada = aniada
        self._imagen  = imagen 
        self._nombre  = nombre 
        self._notaCata  = notaCata
        self._precioArs  = precioArs
        self._resenias = []
        
        
    # Getters 
    @property    
    def aniada(self):
        return self.__aniada
    
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
        mensaje +=  f'- Precio = ${self._precioArs} (Pesos Argentinos)\n'
        return mensaje
    
    
    def reseniar(self):
    

if __name__ == "__main__":
    
    vino1 = Vino("100 % Lucha", "Imagen.jpg", "Toro", 10, 200.67 )
    print(vino1)
    vino1.precio = 1200
    print(vino1.precio)
    print(vino1)