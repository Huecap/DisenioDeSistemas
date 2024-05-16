from NG_Usuarios import Usuario
from NG_Vino import Vino

class Somelier():
    
    def __init__(self, usuario : Usuario, nombre : str, notaPresentacion: str) -> None:
        self._usuario = usuario
        self._nombre = nombre
        self._notaPresentacion = notaPresentacion
        self._validado = False
        self._certificaciones = None
        
        
    @property
    def usuario(self):
        return self._usuario
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def notaPresentacion(self):
        return self._notaPresentacion
    
    @property
    def validado(self):
        return self._validado
        
    def presentar_certificaciones(self, certificaciones : list):
        self._certificaciones = certificaciones 
    
    def validarSomelier(self):
    # No me acuerdo si el validar lo que hacia es ver si esta validado o cambia el estado de validacion
        self._validado = True
        
    def conocerCertificaciones(self):
        return self._certificaciones 
    
    def reseniar(self ,vino:Vino, resenia : tuple):
        if self._validado:
            vino.reseniarPremium(resenia) # resenia (comentario, puntaje)
        else:
            vino.reseniaUsuario(resenia)