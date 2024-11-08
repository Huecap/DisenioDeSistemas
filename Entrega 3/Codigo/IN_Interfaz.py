
import tkinter as tk
from tkinter import ttk, messagebox, font
from tkcalendar import DateEntry
from screeninfo import get_monitors
from datetime import datetime



class PantallaRankingVinos():
    # ! ------ Atributos lo tiene que tener el gestor -------- ##SOLUCIONADO
    #valores_tipos_archivos = ["Excel", "PDF", 'Mostrar Por Pantalla']
    #valores_tipos_resenias = ["Reseñas Somelier", "Reseñas Amigos", "Reseñas Normales"]
    
    #! Recibe gestor por parametro    
    def __init__(self, root, gestor:object) -> None:
        self.root = root
        self.root.title("Interfaz Generar Ranking Vino") 
        self._gestor = gestor
        self.cargarInterfaz()           #! La interfaz tiene que cargarse una vez que el gestor se asigno
        
    
    def mostrarMenuPrincipal(self):
        # Ocultar el menú principal
        self.menu_generar_ranking.pack_forget()
        # Mostrar el menú de inicio
        self.menu_inicio_frame.pack()

    def opcionRankingVinos(self):
        # Ocultar el menú de inicio
        self.menu_inicio_frame.pack_forget()
        # Mostrar el menú principal
        self.menu_generar_ranking.pack()
    
    
    def cancelar(self):
        self.mostrarMenuPrincipal()
    
    def generarRanking(self):
        fecha_d = self.tomarFechaDesde()
        fecha_h = self.tomarFechaHasta()
        tipo = self.tomarTipoResenia()
        archivo = self.tomarTipoVisualizacion()
        
        
        if tipo != self._gestor.valores_tipos_resenias[0] or archivo == self._gestor.valores_tipos_archivos[2]:
            messagebox.showwarning("Warning", 'Opciones actualmente no disponibles')
        else:
                #print('HolaMundo')
                #self._gestor.generarRankingVinos((fecha_d,fecha_h),tipo,archivo)
                #messagebox.showinfo("Archivo Generado correctamente", 'Archivo Generado correctamente')
            self._gestor.generarRankingVinos((fecha_d,fecha_h),tipo,archivo)
            messagebox.showinfo("Archivo Generado correctamente", 'Archivo Generado correctamente')
#            try:
#                #print('HolaMundo')
#                self._gestor.generarRankingVinos((fecha_d,fecha_h),tipo,archivo)
#                messagebox.showinfo("Archivo Generado correctamente", 'Archivo Generado correctamente')
#            except Exception:
#                #print(Exception)
#                messagebox.showerror("Error", 'No se pudo generar el archivo')
                
    def validarPeriodo(self):
        fecha_desde = self.tomarFechaDesde()
        fecha_hasta = self.tomarFechaHasta()
        if fecha_desde > fecha_hasta:
            return False
        return True 
    
    def tomarConfirmacionGenReporte(self):
        if not self.validarPeriodo():
            messagebox.showerror("ERROR",'Error la La fecha desde debe ser menor a fecha hasta')
            return

        confirmacion = messagebox.askyesno("Confirmacioń", "Esta seguro que quiere confirmar")
        if confirmacion:
            self.generarRanking()
        else:
            messagebox.showwarning("Cancelado",'Se ha cancelado la operación')
    def tomarFechaDesde(self):
        return self.date_entry_desde.get_date()
    
    def tomarFechaHasta(self):
        return self.date_entry_hasta.get_date()
    
    def tomarTipoResenia(self):
        return self.combo_tipo_resenia.get()
    
    def tomarTipoVisualizacion(self):
        return self.combo_formato_reporte.get()
        
    @property
    def gestor(self):
        return self._gestor
    
    @gestor.setter
    def gestor(self, gestor):
        self._gestor = gestor
        
    def cargarInterfaz(self):
        self.fuente_titulo = font.Font(size=23)
        self.fuenta_letras = font.Font(size=12)  
          
        #### --------------- Menu de inicio --------------- ####
        # Frame para el menú de inicio
        self.menu_inicio_frame = tk.Frame(self.root)
        
        # Titulo
        self.frame_titulo = tk.Frame(self.menu_inicio_frame)
        self.frame_titulo.pack(pady=10)
        #self.titulo = ttk.Label(self.frame_titulo, text="Bon Vino", font=self.fuente_titulo)
        #self.titulo.pack(anchor="center", expand=True, pady=10)

        self.imagen = tk.PhotoImage(file="image.png")
        self.label_image = ttk.Label(self.menu_inicio_frame, image=self.imagen)
        self.label_image.pack(anchor="center", expand=True, pady=10, padx=10)


        boton_menu_principal = ttk.Button(self.menu_inicio_frame, text="Generar Ranking de Vinos", command=self.opcionRankingVinos)
        boton_menu_principal.pack(pady=10)
        
        #### --------------- Generar Ranking de vinos ---------------####
        # Frame para el Generar ranking vinos
        self.menu_generar_ranking = tk.Frame(self.root)
        self.menu_generar_ranking.config(width=300, height=100)


        # Titulo
        self.frame_titulo = tk.Frame(self.menu_generar_ranking)
        self.frame_titulo.pack(pady=10)

        self.titulo = ttk.Label(self.frame_titulo, text="Generar Ranking de Vinos", font=self.fuente_titulo)
        self.titulo.pack(anchor="center", expand=True, pady=10)

        # Fecha desde
        self.frame_fd = tk.Frame(self.menu_generar_ranking)
        self.frame_fd.pack(pady=10, expand=True, fill="both")

        self.fecha_desde_label = ttk.Label(self.frame_fd, text="Fecha Desde", font=self.fuenta_letras)
        self.fecha_desde_label.pack(anchor="w", expand=True)

        default_date_desde = datetime(2024, 2, 25)
        self.date_entry_desde = DateEntry(self.frame_fd, width=20, year=default_date_desde.year, month=default_date_desde.month, day=default_date_desde.day, selectbackground="#ffffff")
        self.date_entry_desde.pack(expand=True,fill="both")

        # Fecha Hasta
        default_date_hasta = datetime(2024, 5, 25)
        self.frame_fh = tk.Frame(self.menu_generar_ranking)
        self.frame_fh.pack(pady=10, expand=True, fill="both")
     
        self.fecha_hasta_label = ttk.Label(self.frame_fh, text="Fecha Hasta", font=self.fuenta_letras)
        self.fecha_hasta_label.pack(anchor="w", expand=True)
     
        self.date_entry_hasta = DateEntry(self.frame_fh, width=20, year=default_date_hasta.year, month=default_date_hasta.month, day=default_date_hasta.day)
        self.date_entry_hasta.pack(expand=True,fill="both")



        # Lista TIpo de reseña
        self.frame_tr = tk.Frame(self.menu_generar_ranking)
        self.frame_tr.pack(pady=10, expand=True, fill="both")
     
        self.tipo_resenia_label = ttk.Label(self.frame_tr, text="Tipo Reseña", font=self.fuenta_letras)
        self.tipo_resenia_label.pack(anchor="w", expand=True)
     
        self.combo_tipo_resenia = ttk.Combobox(self.frame_tr, values=self._gestor.valores_tipos_resenias)
        self.combo_tipo_resenia.set(self._gestor.valores_tipos_resenias[0])
        self.combo_tipo_resenia.pack(anchor="w", fill="both")
        
        # Lista Formato Reporte
        self.frame_fr = tk.Frame(self.menu_generar_ranking)
        self.frame_fr.pack(pady=10, expand=True, fill="both")
     
        self.formato_reporte_label = ttk.Label(self.frame_fr, text="Formato de Reporte", font=self.fuenta_letras)
        self.formato_reporte_label.pack(anchor="w", expand=True)
     
        self.combo_formato_reporte = ttk.Combobox(self.frame_fr, values=self._gestor.valores_tipos_archivos)
        self.combo_formato_reporte.set(self._gestor.valores_tipos_archivos[0])
        self.combo_formato_reporte.pack(anchor="w", fill="both")
        
        
        self.frame_botones = tk.Frame(self.menu_generar_ranking)
        self.frame_botones.pack(pady=10, expand=True, fill="both")
     
        self.boton_tomarConfirmacionGenReporte = ttk.Button(self.frame_botones, text="Generar Reporte", command=self.tomarConfirmacionGenReporte)
        self.boton_cancelar = ttk.Button(self.frame_botones, text="Cancelar", command=self.cancelar)
        self.boton_tomarConfirmacionGenReporte.pack(pady=10)
        self.boton_cancelar.pack(pady=10)
                
        
        self.menu_inicio_frame.pack()
        #self.menu_generar_ranking.pack()

        self.date_entry_desde.config(background='#454343')
        self.date_entry_hasta.configure(background="#454343")
        
if __name__ == "__main__":

    ventana = tk.Tk()
    boundary = PantallaRankingVinos(ventana)

    # Geometria de la ventan 
    ventana.geometry("420x520")
    ventana.resizable(False, False)


    # Seteamos el tema
    ventana.tk.call("source", "azure.tcl")
    ventana.tk.call("set_theme", "dark")
    
    
    
    # Actualizamos cualquier cambio de la ventana
    ventana.update()

    # Limitamos el tamaño mínimo de la ventana
    ventana.minsize(ventana.winfo_width(), ventana.winfo_height())

    # Localizamos el monitor principal
    monitor = get_monitors()[0]

    # Centramos la ventana
    x_cordinate = int((monitor.width / 2) - (ventana.winfo_width() / 2))
    y_cordinate = int((monitor.height / 2) - (ventana.winfo_height() / 2))
    ventana.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))
    
    # Main loop para que se mantenga corriendo
    ventana.mainloop()
