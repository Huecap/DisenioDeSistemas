
class TipoUva:
    def __init__(self, nombre:str, descripcion:str) -> None:
        self._nombre = nombre
        self._descripcion = descripcion
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def descripcion(self):
        return self._descripcion
    
    def __str__(self) -> str:
        mensaje = f'\nNombre: {self._nombre} \n'
        mensaje += f'Descripción: \n {self.descripcion}\n'
        return mensaje