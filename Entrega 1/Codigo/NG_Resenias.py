from datetime import date, datetime
# from NG_Vino import Vino

class Resenia:
    
    def __init__(self, vino , comentario : str, puntaje : float, esPremium: bool, fecha : date) -> None:
        self._vino = vino
        self._comentario = comentario
        self._puntaje = puntaje
        self._esPremium = esPremium
        # self._fechaResenia = datetime.datetime.now()
        self._fechaResenia = fecha
        
    def sosDeEnofilo(self):
        """Devuelve True si es de Enofilo, Devuelve False si es de Somelier

        :return: Devuelve un booleano
        :rtype: bool
        """ 
        return (False if self._esPremium else True)
    
    def sosDeSomelier(self):
        """Devuelve True si es de Somelier, Devuelve False se es de Enofilo 

        :return: Devuelve un booleano
        :rtype: bool
        """
        return (True if self._esPremium else False)    
    
    def __str__(self):
        """Metodo mágico que representa al objeto como un string
        
        """
        mensaje = f'Vino: {self._vino.nombre}\n'      
        mensaje += f'Comentario {self._comentario}\n'      
        mensaje += f'Puntaje: {self._puntaje}/5\n'      
        mensaje += f'La resenia fue dejada por un {"Enofilo" if self.sosDeEnofilo() else "Somelier"} \n'      
        mensaje += f'Fecha de la Reseña {self._fechaResenia}'      
        return mensaje
    
    def esPremium(self):
        return (True if self._esPremium else False)
        
        
    
if __name__ == "__main__":
    resenia1 = Resenia("Toro", "Muy bueno y barato \n Pega bien con pritty",
                       5, True, datetime.now())
    print(resenia1)