import json
from NG_TipoUva import TipoUva

def crearJson(data, nombre_archivo):
    # Escribir los datos en el archivo JSON
    with open(nombre_archivo, "w") as archivo_json:
        json.dump(data, archivo_json)
    print(f"Se ha creado el archivo JSON '{nombre_archivo}'.")


def cargarJson(nombre_archivo):
    # Cargar el archivo JSON
    with open(nombre_archivo, "r") as archivo_json:
        datos = json.load(archivo_json)

    return datos





# Datos de la persona
tipos_uva_data = [
    {"nombre": "Malbec", "descripcion": "Uva tinta fuerte y robusta."},
    {"nombre": "Cabernet Sauvignon", "descripcion": "Uva tinta con notas de frutas oscuras."},
    {"nombre": "Merlot", "descripcion": "Uva tinta suave y afrutada."},
    {"nombre": "Syrah", "descripcion": "Uva tinta con sabores a especias."},
    {"nombre": "Pinot Noir", "descripcion": "Uva tinta ligera y elegante."},

]


tipos_uva = []
for n in tipos_uva_data:
    tipo_uva = TipoUva(n["nombre"], n["descripcion"])
    tipos_uva.append(tipo_uva)

for tipo_uva in tipos_uva:
    print(tipo_uva)

# Nombre del archivo JSON
nombre_archivo = "tiposUva.js"

# Escribir los datos en el archivo JSON
with open(nombre_archivo, "w") as archivo_json:
    json.dump(tipos_uva_data, archivo_json)

print(f"Se ha creado el archivo JSON '{nombre_archivo}'.")


# Cargar el archivo JSON
with open(nombre_archivo, "r") as archivo_json:
    datos = json.load(archivo_json)

tipos_uva = []
for n in datos:
    tipo_uva = TipoUva(n["nombre"], n["descripcion"])
    tipos_uva.append(tipo_uva)

for tipo_uva in tipos_uva:
    print(tipo_uva)