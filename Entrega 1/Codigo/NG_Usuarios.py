
class Usuario:
    
    def __init__(self, nombre, constrasenia) -> None:
        self._nombre = nombre
        self._constrasenia = constrasenia
        self._premium = False
        
    @property
    def nombre(self):
        return self._nombre

    def esPremium(self):
    # No me acuerdo si este metodo cambia la propiedad esPremium o directamente retorna si es premium o no
        self._premium = True
        
    def esTuUsuario(self, usuario):
        if usuario == self:
            return True
        else:
            return False
    
if __name__ == "__main__":
    usuario1 = Usuario("Juan Carlos", "123sss222")
    print(usuario1.nombre)
    usuario2 = Usuario("Alberto Fernandez", "weefadsas")
    print(usuario1.esTuUsuario(usuario2))