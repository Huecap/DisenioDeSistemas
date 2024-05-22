
import tkinter as tk
from tkinter import ttk, messagebox, font
from tkcalendar import DateEntry
from screeninfo import get_monitors


def mostrar_menu_principal():
    # Ocultar el menú de inicio
    menu_inicio_frame.pack_forget()
    # Mostrar el menú principal
    frame.pack()

def mostrar_menu_inicio():
    # Ocultar el menú principal
    frame.pack_forget()
    # Mostrar el menú de inicio
    menu_inicio_frame.pack()


def enviar():
    
#    valor = campo1.get()
#    messagebox.showinfo("Archivo Generado correctamente",f'{valor}')
    
#    valor = campo1.get()
#    messagebox.showerror("Error",f'{valor}')
    valor = "Buenas tardes"
    valor = messagebox.askyesno("Confirmacioń", "Esta seguro que quiere confirmar")
    
    messagebox.showinfo("Archivo Generado correctamente",f'{valor}')

def cancelar():
    mostrar_menu_inicio()

# Configuramos la ventana 
ventana = tk.Tk()
ventana.resizable(False, False)
# Geometria de la ventan 
ventana.geometry("420x520")
# Titulo de la ventana
ventana.title("Bon Vino App")

# Seteamos el tema
ventana.tk.call("source", "azure.tcl")
ventana.tk.call("set_theme", "dark")
    
# Variables 
valor_tipo_resenia = tk.StringVar()    

fuente_titulo = font.Font(size=23)
fuenta_letras = font.Font(size=12)





# Frame para el menú de inicio
menu_inicio_frame = tk.Frame(ventana)
menu_inicio_frame.pack()

# Titulo
frame_titulo = tk.Frame(menu_inicio_frame)
frame_titulo.pack(pady=10)
titulo = ttk.Label(frame_titulo, text="Bon Vino", font=fuente_titulo)
titulo.pack(anchor="center", expand=True, pady=10)


boton_menu_principal = ttk.Button(menu_inicio_frame, text="Generar Ranking de Vinos", command=mostrar_menu_principal)
boton_menu_principal.pack(pady=10)

# Frame para el Generar ranking vinos
frame = tk.Frame(ventana)
frame.config(width=300, height=100)


# Titulo
frame_titulo = tk.Frame(frame)
frame_titulo.pack(pady=10)
titulo = ttk.Label(frame_titulo, text="Generar Ranking de Vinos", font=fuente_titulo)
titulo.pack(anchor="center", expand=True, pady=10)


# Fecha desde
frame_fd = tk.Frame(frame)
frame_fd.pack(pady=10, expand=True, fill="both")
fecha_desde_label = ttk.Label(frame_fd, text="Fecha Desde", font=fuenta_letras)
fecha_desde_label.pack(anchor="w", expand=True)

date_entry_desde = DateEntry(frame_fd, width=20)
date_entry_desde.pack(expand=True,fill="both")



# Fecha Hasta
frame_fh = tk.Frame(frame)
frame_fh.pack(pady=10, expand=True, fill="both")
fecha_hasta_label = ttk.Label(frame_fh, text="Fecha Desde", font=fuenta_letras)
fecha_hasta_label.pack(anchor="w", expand=True)

date_entry_hasta = DateEntry(frame_fh, width=20)
date_entry_hasta.pack(expand=True,fill="both")

# Lista TIpo de reseña
frame_tr = tk.Frame(frame)
frame_tr.pack(pady=10, expand=True, fill="both")

tipo_resenia_label = ttk.Label(frame_tr, text="Tipo Reseña", font=fuenta_letras)
tipo_resenia_label.pack(anchor="w", expand=True)

valores = ["Reseñas Somelier", "Reseñas Amigos", "Reseñas Normales"]
combo_tipo_resenia = ttk.Combobox(frame_tr, values=valores)
combo_tipo_resenia.pack(anchor="w", fill="both")

# Lista Formato Reporte
frame_fr = tk.Frame(frame)
frame_fr.pack(pady=10, expand=True, fill="both")

formato_reporte_label = ttk.Label(frame_fr, text="Formato de Reporte", font=fuenta_letras)
formato_reporte_label.pack(anchor="w", expand=True)

valores = ["Excel", "PDF"]
combo_formato_reporte = ttk.Combobox(frame_fr, values=valores)
combo_formato_reporte.pack(anchor="w", fill="both")

# Botones
frame_botones = tk.Frame(frame)
frame_botones.pack(pady=10, expand=True, fill="both")

boton_enviar = ttk.Button(frame_botones, text="Generar Reporte", command=enviar)
boton_cancelar = ttk.Button(frame_botones, text="Cancelar", command=cancelar)
boton_enviar.pack(pady=10)
boton_cancelar.pack(pady=10)


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
