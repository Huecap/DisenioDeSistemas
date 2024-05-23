
import tkinter as tk
from tkinter import ttk, messagebox, font
from tkcalendar import DateEntry
from screeninfo import get_monitors


from IN_Interfaz import PantallaRankingVinos
from NG_Gestor import Gestor


class Apk:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self._gestor = Gestor()
        #! Directamente ya pasamos gestor por parametro
        self.PantallaRankingVinos = PantallaRankingVinos(self.ventana, self._gestor)

    
if __name__ == "__main__":

    aplicacion = Apk()

    # Geometria de la ventan 
    aplicacion.ventana.geometry("600x520")
    aplicacion.ventana.resizable(False, False)


    # Seteamos el tema
    aplicacion.ventana.tk.call("source", "azure.tcl")
    aplicacion.ventana.tk.call("set_theme", "dark")
    
    # Actualizamos cualquier cambio de la aplicacion.ventana
    aplicacion.ventana.update()

    # Limitamos el tamaño mínimo de la aplicacion.ventana
    aplicacion.ventana.minsize(aplicacion.ventana.winfo_width(), aplicacion.ventana.winfo_height())

    # Localizamos el monitor principal
    monitor = get_monitors()[0]

    # Centramos la aplicacion.ventana
    x_cordinate = int((monitor.width / 2) - (aplicacion.ventana.winfo_width() / 2))
    y_cordinate = int((monitor.height / 2) - (aplicacion.ventana.winfo_height() / 2))
    aplicacion.ventana.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
    
    # Main loop para que se mantenga corriendo
    aplicacion.ventana.mainloop()
