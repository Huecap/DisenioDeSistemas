


class Maridaje:
    def __init__(self,descripcion:str, nombre:str):
        self._descripcion = descripcion
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    @property
    def descripcion(self):
        return self._descripcion
    @nombre.setter
    def nombre(self, nom: str):
        self._nombre = nom

    @descripcion.setter
    def descripcion(self, desc: str):
        self._descripcion = desc


    def maridaConVino(self):
        # Lista de recomendaciones de plato para probar junto al vino
        pass
