from NG_TipoUva import TipoUva
from NG_Varietal import Varietal
from NG_Maridaje import Maridaje
from NG_Geografia import *
from NG_Bodega import Bodega
from NG_Vino import Vino
from NG_Resenias import Resenia

#----------------------------------------------------------------
#Para pasar a formato json
import json 
#-------------------------------------------------------------


# Datos de ejemplo para TipoUva
tipos_uva_data = [
    {"nombre": "Malbec", "descripcion": "Uva tinta fuerte y robusta."},
    {"nombre": "Cabernet Sauvignon", "descripcion": "Uva tinta con notas de frutas oscuras."},
    {"nombre": "Merlot", "descripcion": "Uva tinta suave y afrutada."},
    {"nombre": "Syrah", "descripcion": "Uva tinta con sabores a especias."},
    {"nombre": "Pinot Noir", "descripcion": "Uva tinta ligera y elegante."},

]

# Crear instancias de TipoUva
tipos_uva = [TipoUva(**data) for data in tipos_uva_data]

"""
Verificar las instancias
for tipo_uva in tipos_uva:
    print(tipo_uva.nombre)
"""

# Datos de ejemplo para Varietal con TipoUva
varietal_data = [
    {"descripcion": "Malbec", "porcentaje_composicion": [(tipos_uva[0],40)]},
    {"descripcion": "Cabernet Sauvignon", "porcentaje_composicion": [(tipos_uva[1], 30)]},
    {"descripcion": "Chardonnay", "porcentaje_composicion": [(tipos_uva[2],25)]},
    {"descripcion": "Syrah", "porcentaje_composicion": [(tipos_uva[3],35)]},
    {"descripcion": "Merlot", "porcentaje_composicion": [(tipos_uva[4],45)]},
]

# Crear instancias de Varietal
varietales = [Varietal(**data) for data in varietal_data]

# Datos de ejemplo para Maridaje
maridajes_data = [
    {"descripcion": "Perfecto con carnes rojas.", "nombre": "Carnes Rojas"},
    {"descripcion": "Ideal con pescados y mariscos.", "nombre": "Pescados y Mariscos"},
    {"descripcion": "Excelente con pastas.", "nombre": "Pastas"},
    {"descripcion": "Acompaña muy bien quesos.", "nombre": "Quesos"},
    {"descripcion": "Marida con aves.", "nombre": "Aves"}
]

# Crear instancias de Maridaje
maridajes = [Maridaje(**data) for data in maridajes_data]

"""
for maridaje in maridajes:
    print(maridaje)
"""    

# Datos de ejemplo para Pais
paises_data = [
    {"nombre": "Argentina"},
    {"nombre": "Chile"}
]

# Crear instancias de Pais
paises = [Pais(**data) for data in paises_data]

    
# Datos de ejemplo para Provincia
provincias_data = [
    {"nombre": "Mendoza", "pais": paises[0]},
    {"nombre": "San Juan", "pais": paises[0]},
    {"nombre": "La Rioja", "pais": paises[0]},
    {"nombre": "Buenos Aires", "pais": paises[0]},
    {"nombre": "Colchagua", "pais": paises[1]},
    {"nombre": "Maule", "pais": paises[1]},
    {"nombre": "Casablanca", "pais": paises[1]},
    {"nombre": "Biobío", "pais": paises[1]}
]

# Crear instancias de Provincia
provincias = [Provincia(**data) for data in provincias_data]

"""
Por ejemplo, ahora desde provincia podrias acceder al 
nombre del pais 
for provincia in provincias:
    print(provincia.pais.nombre)
"""

# Datos de ejemplo para RegionVitivinicola con Provincia
regiones_data = [
    {"nombre": "Valle de Uco", "descripcion": "Una región vinícola famosa por sus vinos Malbec.", "provincia": provincias[0]},
    {"nombre": "Valle del Tulum", "descripcion": "Una región vinícola con clima templado y suelos fértiles.", "provincia": provincias[1]},
    {"nombre": "Valle de Famatina", "descripcion": "Un valle rodeado de montañas que produce vinos de altura.", "provincia": provincias[2]},
    {"nombre": "Pampas", "descripcion": "Una vasta llanura fértil conocida por su ganadería y agricultura.", "provincia": provincias[3]},
    {"nombre": "Valle de Colchagua", "descripcion": "Un valle chileno famoso por sus vinos tintos.", "provincia": provincias[4]},
    {"nombre": "Valle del Maule", "descripcion": "Una región vinícola diversa con una larga historia vitivinícola.", "provincia": provincias[5]},
    {"nombre": "Valle de Casablanca", "descripcion": "Una región vinícola costera conocida por sus vinos blancos.", "provincia": provincias[6]},
    {"nombre": "Valle del Biobío", "descripcion": "Un valle rodeado de ríos y montañas que produce vinos frescos y frutales.", "provincia": provincias[7]}
]

# Crear instancias de RegionVitivinicola
regiones = [RegionVitivinicola(**data) for data in regiones_data]

"""
for region in regiones:
    print(region._provincia._pais.nombre)
"""

# Datos de ejemplo  para Bodega con RegionVitivinicola
bodega_data = [
    {
        "coordenadas_ubicacion": [39.9526, -75.1652],
        "descripcion": "Bodega con vasta experiencia en vinos de autor",
        "historia": "Establecida en 1960 por Don Antonio Martínez",
        "nombre": "Bodega Martínez",
        "periodo_actualizacion": "2022-04-30",
        "region": regiones[2]
    },
    {
        "coordenadas_ubicacion": [37.7749, -122.4194],
        "descripcion": "Bodega moderna con enfoque en sostenibilidad",
        "historia": "Fundada en 2000 por la enóloga María García",
        "nombre": "Bodega García",
        "periodo_actualizacion": "2022-05-10",
        "region": regiones[3]
    },
    {
        "coordenadas_ubicacion": [41.8781, -87.6298],
        "descripcion": "Bodega reconocida por sus vinos de alta gama",
        "historia": "Con más de 100 años de tradición en viticultura",
        "nombre": "Bodega López",
        "periodo_actualizacion": "2022-05-05",
        "region": regiones[4]
    },
    {
        "coordenadas_ubicacion": [34.0522, -118.2437],
        "descripcion": "Bodega boutique con vinos exclusivos",
        "historia": "Inaugurada en 1990 por la familia Rodríguez",
        "nombre": "Bodega Rodríguez",
        "periodo_actualizacion": "2022-04-25",
        "region": regiones[1]
    }
]

# Crear instancias de Bodega
bodegas = [Bodega(**data) for data in bodega_data]

"""
for bodega in bodegas:
    print(bodega._nombre)
"""

# Datos de ejemplo para Vino
vino_data = [
    {
        "aniada": "2019",
        "imagen_etiqueta": "imagen_vino1.jpg",
        "nombre": "Vino Tinto Reserva",
        "nota_de_cata_bodega": 4.5,
        "precio_ARS": 750.0,
        "maridaje": [maridajes[0], maridajes[1]],
        "varietal": [varietales[0], varietales[1]],
        "bodega": bodegas[0],
    },
    {
        "aniada": "2020",
        "imagen_etiqueta": "imagen_vino2.jpg",
        "nombre": "Vino Blanco Joven",
        "nota_de_cata_bodega": 4.2,
        "precio_ARS": 550.0,
        "maridaje": [maridajes[1], maridajes[2]],
        "varietal": [varietales[1], varietales[2]],
        "bodega": bodegas[1],
    },
    {
        "aniada": "2023",
        "imagen_etiqueta": "imagen_vino3.jpg",
        "nombre": "Vino Tinto Añejo",
        "nota_de_cata_bodega": 5.0,
        "precio_ARS": 1200.5,
        "maridaje": [maridajes[2], maridajes[3]],
        "varietal": [varietales[3], varietales[3]],
        "bodega": bodegas[3],
    }, 
    {
        "aniada": "2021",
        "imagen_etiqueta": "imagen_vino4.jpg",
        "nombre": "Vino Tinto Reserva Elegante",
        "nota_de_cata_bodega": 3.0,
        "precio_ARS": 400.0,
        "maridaje": [maridajes[3], maridajes[4]],
        "varietal": [varietales[4], varietales[4]],
        "bodega": bodegas[2],
    },
    {
        "aniada": "2022",
        "imagen_etiqueta": "imagen_vino5.jpg",
        "nombre": "Vino Tinto Espléndido",
        "nota_de_cata_bodega": 2.8,
        "precio_ARS": 900.0,
        "maridaje": [maridajes[4], maridajes[3]],
        "varietal": [varietales[0], varietales[3]],
        "bodega": bodegas[3],
    },
    {
        "aniada": "2018",
        "imagen_etiqueta": "imagen_vino6.jpg",
        "nombre": "Vino Tinto Reserva Clásico",
        "nota_de_cata_bodega": 4.6,
        "precio_ARS": 950.5,
        "maridaje": [maridajes[0], maridajes[4]],
        "varietal": [varietales[1], varietales[4]],
        "bodega": bodegas[2],
    },
    {
        "aniada": "2019",
        "imagen_etiqueta": "imagen_vino7.jpg",
        "nombre": "Vino Tinto Noble",
        "nota_de_cata_bodega": 5.0,
        "precio_ARS": 880.6,
        "maridaje": [maridajes[1], maridajes[4]],
        "varietal": [varietales[0], varietales[2]],
        "bodega": bodegas[1],
    },
    {
        "aniada": "2020",
        "imagen_etiqueta": "imagen_vino8.jpg",
        "nombre": "Vino Tinto Reserva Exquisito",
        "nota_de_cata_bodega": 1.0,
        "precio_ARS": 740.0,
        "maridaje": [maridajes[0], maridajes[2]],
        "varietal": [varietales[1], varietales[3]],
        "bodega": bodegas[0],
    },
    {
        "aniada": "2021",
        "imagen_etiqueta": "imagen_vino9.jpg",
        "nombre": "Vino Blanco Joven Fresco",
        "nota_de_cata_bodega": 1.5,
        "precio_ARS": 650.0,
        "maridaje": [maridajes[1], maridajes[3]],
        "varietal": [varietales[2], varietales[4]],
        "bodega": bodegas[0],
    },
    {
        "aniada": "2022",
        "imagen_etiqueta": "imagen_vino10.jpg",
        "nombre": "Vino Blanco Vivo",
        "nota_de_cata_bodega": 2.7,
        "precio_ARS": 980.8,
        "maridaje": [maridajes[2], maridajes[4]],
        "varietal": [varietales[3], varietales[0]],
        "bodega": bodegas[1],
    },
    {
        "aniada": "2023",
        "imagen_etiqueta": "imagen_vino11.jpg",
        "nombre": "Vino Blanco Joven Delicado",
        "nota_de_cata_bodega": 3.0,
        "precio_ARS": 200.0,
        "maridaje": [maridajes[3], maridajes[2]],
        "varietal": [varietales[3], varietales[3]],
        "bodega": bodegas[2],
    },
    {
        "aniada": "2017",
        "imagen_etiqueta": "imagen_vino12.jpg",
        "nombre": "Vino Blanco Joven Radiante",
        "nota_de_cata_bodega": 4.6,
        "precio_ARS": 1000.5,
        "maridaje": [maridajes[4], maridajes[3]],
        "varietal": [varietales[4], varietales[2]],
        "bodega": bodegas[3],
    },
    {
        "aniada": "2018",
        "imagen_etiqueta": "imagen_vino13.jpg",
        "nombre": "Vino Blanco Luminoso",
        "nota_de_cata_bodega": 4.9,
        "precio_ARS": 2500.0,
        "maridaje": [maridajes[4], maridajes[2]],
        "varietal": [varietales[3], varietales[1]],
        "bodega": bodegas[3],
    },
    {
        "aniada": "2019",
        "imagen_etiqueta": "imagen_vino14.jpg",
        "nombre": "Vino Blanco Suave",
        "nota_de_cata_bodega": 3.9,
        "precio_ARS": 750.5,
        "maridaje": [maridajes[3], maridajes[1]],
        "varietal": [varietales[2], varietales[0]],
        "bodega": bodegas[2],
    },
    {
        "aniada": "2020",
        "imagen_etiqueta": "imagen_vino15.jpg",
        "nombre": "Vino Blanco Afrutado",
        "nota_de_cata_bodega": 2.2,
        "precio_ARS": 600.6,
        "maridaje": [maridajes[2], maridajes[0]],
        "varietal": [varietales[2], varietales[3]],
        "bodega": bodegas[1],
    }
]

# Crear instancias de Vino
vinos = [Vino(**data) for data in vino_data]

"""
for vino in vinos:
    print(vino)                     # muestra el str de vinos
    print(vino._bodega._nombre)     # muestra el nombre de la bodega a la que pertenece
"""

# Asociar vinos a bodega
"""
Usando vino._bodega accedemos al objetoeto bodega al que se asocia cada vino
Dicho objetoeto tiene la funcion cargar vino, a la cual le pasamos por parametro
el mismo objetoeto vino del cual obtuvimos la bodega, generando asi la relacion bidireccional
"""
for vino in vinos:                      
    vino._bodega.cargar_vino(vino)        
 
"""
for bodega in bodegas:              # muestra la coleccion de objetoetos Vino asociados a cada bodega
    print(bodega._vinos)        
"""

# Datos de ejemplo para Resenia
resenia_data = [
    {
        "comentario": "Excelente vino, muy equilibrado y con gran aroma",
        "esPremium": True,
        "fechaResenia": "2022-05-15",
        "puntaje": 4.8,
        "vino": vinos[0],
    },
    {
        "comentario": "Buen vino, relación calidad-precio adecuada",
        "esPremium": False,
        "fechaResenia": "2022-05-10",
        "puntaje": 4.0,
        "vino": vinos[0],
    },
    {
        "comentario": "Un vino con cuerpo y notas de frutas maduras",
        "esPremium": False,
        "fechaResenia": "2020-08-25",
        "puntaje": 3.5,
        "vino": vinos[0],
    },
    {
        "comentario": "Buen equilibrio entre fruta y acidez",
        "esPremium": False,
        "fechaResenia": "2021-09-10",
        "puntaje": 5.0,
        "vino": vinos[0],
    },
    {
        "comentario": "Aromas apagados y poco definidos",
        "esPremium": True,
        "fechaResenia": "2021-05-11",
        "puntaje": 1.5,
        "vino": vinos[1],
    },
    {
        "comentario": "Aromas apagados y poco definidos",
        "esPremium": False,
        "fechaResenia": "2022-12-18",
        "puntaje": 2.3,
        "vino": vinos[1],
    },
    {
        "comentario": "Final largo y persistente",
        "esPremium": True,
        "fechaResenia": "2023-10-02",
        "puntaje": 3.3,
        "vino": vinos[1],
    },
    {
        "comentario": "Presencia de defectos como corcho o avinagramiento",
        "esPremium": True,
        "fechaResenia": "2024-02-28",
        "puntaje": 4.4,
        "vino": vinos[1],
    },
    {
        "comentario": "Buen equilibrio entre fruta y acidez",
        "esPremium": False,
        "fechaResenia": "2024-04-16",
        "puntaje": 4.5,
        "vino": vinos[2],
    },
    {
        "comentario": "Sabor vibrante y fresco",
        "esPremium": False,
        "fechaResenia": "2024-02-22",
        "puntaje": 5.0,
        "vino": vinos[2],
    },
    {
        "comentario": "Poca intensidad aromática",
        "esPremium": True,
        "fechaResenia": "2024-01-31",
        "puntaje": 4.8,
        "vino": vinos[2],
    },
    {
        "comentario": "Aromas apagados y poco definidos",
        "esPremium": False,
        "fechaResenia": "2024-03-12",
        "puntaje": 1.7,
        "vino": vinos[2],
    },
    {
        "comentario": "Precio elevado para la calidad ofrecida",
        "esPremium": True,
        "fechaResenia": "2022-12-31",
        "puntaje": 3.5,
        "vino": vinos[3],
    },
    {
        "comentario": "Elegante y refinado en nariz y paladar",
        "esPremium": True,
        "fechaResenia": "2023-11-29",
        "puntaje": 2.8,
        "vino": vinos[3],
    },
    {
        "comentario": "La intensidad de los sabores se mantiene bien equilibrada en todo momento",
        "esPremium": False,
        "fechaResenia": "2022-09-05",
        "puntaje": 1.5,
        "vino": vinos[3],
    },
    {
        "comentario": "La relación calidad-precio no está justificada por la experiencia sensorial que ofrece",
        "esPremium": True,
        "fechaResenia": "2023-07-04",
        "puntaje": 3.9,
        "vino": vinos[3],
    },
    {
        "comentario": "El equilibrio entre la acidez y los taninos es perfecto",
        "esPremium": True,
        "fechaResenia": "2023-09-13",
        "puntaje": 2.3,
        "vino": vinos[4],
    },
    {
        "comentario": "Su textura en boca es suave y sedosa, creando una experiencia sensorial placentera",
        "esPremium": False,
        "fechaResenia": "2024-08-14",
        "puntaje": 4.8,
        "vino": vinos[4],
    },
    {
        "comentario": "Textura suave y sedosa en boca",
        "esPremium": False,
        "fechaResenia": "2024-07-15",
        "puntaje": 5.0,
        "vino": vinos[4],
    },
    {
        "comentario": "Taninos agresivos y astringentes",
        "esPremium": True,
        "fechaResenia": "2023-06-16",
        "puntaje": 3.5,
        "vino": vinos[4],
    },
    {
        "comentario": "El equilibrio entre la acidez y los taninos es perfecto",
        "esPremium": False,
        "fechaResenia": "2019-10-08",
        "puntaje": 4.6,
        "vino": vinos[5],
    },
    {
        "comentario": "Armonía entre taninos y fruta",
        "esPremium": True,
        "fechaResenia": "2020-09-09",
        "puntaje": 3.6,
        "vino": vinos[5],
    },
    {
        "comentario": "La persistencia en el paladar es corta y poco memorable",
        "esPremium": True,
        "fechaResenia": "2021-08-10",
        "puntaje": 1.5,
        "vino": vinos[5],
    },
    {
        "comentario": "Aromas complejos y seductores",
        "esPremium": False,
        "fechaResenia": "2022-07-11",
        "puntaje": 4.6,
        "vino": vinos[5],
    },
    {
        "comentario": "Final largo y persistente",
        "esPremium": False,
        "fechaResenia": "2020-04-18",
        "puntaje": 2.3,
        "vino": vinos[6],
    },
    {
        "comentario": "Sensación áspera en boca",
        "esPremium": True,
        "fechaResenia": "2021-03-19",
        "puntaje": 4.8,
        "vino": vinos[6],
    },
    {
        "comentario": "Gran profundidad y complejidad",
        "esPremium": False,
        "fechaResenia": "2022-02-20",
        "puntaje": 3.5,
        "vino": vinos[6],
    },
    {
        "comentario": "El vino parece haber sido elaborado con uvas de baja calidad, afectando su perfil aromático y gustativo",
        "esPremium": True,
        "fechaResenia": "2023-01-21",
        "puntaje": 1.7,
        "vino": vinos[6],
    },
    {
        "comentario": "Exceso de alcohol que domina el perfil",
        "esPremium": False,
        "fechaResenia": "2021-08-09",
        "puntaje": 2.8,
        "vino": vinos[7],
    },
    {
        "comentario": "Es un vino elegante y refinado que destaca por su complejidad y profundidad de sabor",
        "esPremium": True,
        "fechaResenia": "2022-07-10",
        "puntaje": 2.7,
        "vino": vinos[7],
    },
    {
        "comentario": "Notas de frutas maduras y especias",
        "esPremium": True,
        "fechaResenia": "2022-06-11",
        "puntaje": 5.0,
        "vino": vinos[7],
    },
    {
        "comentario": "Es un vino versátil que se puede maridar con una amplia variedad de platos",
        "esPremium": False,
        "fechaResenia": "2021-05-12",
        "puntaje": 1.5,
        "vino": vinos[7],
    },
    {
        "comentario": "Este vino tiene una excelente relación calidad-precio",
        "esPremium": True,
        "fechaResenia": "2021-09-29",
        "puntaje": 4.8,
        "vino": vinos[8],
    },
    {
        "comentario": "Falta de complejidad y profundidad",
        "esPremium": False,
        "fechaResenia": "2021-10-17",
        "puntaje": 2.3,
        "vino": vinos[8],
    },
    {
        "comentario": "La relación calidad-precio no está justificada por la experiencia sensorial que ofrece",
        "esPremium": True,
        "fechaResenia": "2022-07-27",
        "puntaje": 4.1,
        "vino": vinos[8],
    },
    {
        "comentario": "La añada de este vino particular ha resultado excepcional, resaltando su calidad",
        "esPremium": False,
        "fechaResenia": "2023-11-12",
        "puntaje": 3.5,
        "vino": vinos[8],
    },
    {
        "comentario": "Estructura bien integrada",
        "esPremium": True,
        "fechaResenia": "2023-06-16",
        "puntaje": 3.1,
        "vino": vinos[9],
    },
    {
        "comentario": "Sensación de desequilibrio entre los componentes",
        "esPremium": True,
        "fechaResenia": "2023-10-08",
        "puntaje": 4.8,
        "vino": vinos[9],
    },
    {
        "comentario": "La añada de este vino particular ha resultado excepcional, resaltando su calidad",
        "esPremium": False,
        "fechaResenia": "2022-09-05",
        "puntaje": 1.5,
        "vino": vinos[9],
    },
    {
        "comentario": "Final corto y decepcionante",
        "esPremium": False,
        "fechaResenia": "2024-03-12",
        "puntaje": 2.3,
        "vino": vinos[9],
    },
    {
        "comentario": "Buena expresión varietal",
        "esPremium": True,
        "fechaResenia": "2023-07-10",
        "puntaje": 5.0,
        "vino": vinos[10],
    },
    {
        "comentario": "Armonía entre taninos y fruta",
        "esPremium": True,
        "fechaResenia": "2024-03-12",
        "puntaje": 4.8,
        "vino": vinos[10],
    },
    {
        "comentario": "Buen equilibrio entre acidez, dulzura y amargura",
        "esPremium": False,
        "fechaResenia": "2024-03-12",
        "puntaje": 2.7,
        "vino": vinos[10],
    },
    {
        "comentario": "Notas de madera o roble demasiado pronunciadas",
        "esPremium": False,
        "fechaResenia": "2023-10-08",
        "puntaje": 2.8,
        "vino": vinos[10],
    },
    {
        "comentario": "Aromas complejos y cautivadores", 
        "esPremium": True,
        "fechaResenia": "2022-07-10",
        "puntaje": 3.5,
        "vino": vinos[11],
    },
    {
        "comentario": "Sabor suave y sedoso en el paladar", 
        "esPremium": False,
        "fechaResenia": "2021-08-10",
        "puntaje": 1.5,
        "vino": vinos[11],
    },
    {
        "comentario": "Exceso de dulzura o acidez desequilibrada",
        "esPremium": True,
        "fechaResenia": "2018-05-12",
        "puntaje": 3.6,
        "vino": vinos[11],
    },
    {
        "comentario": "Final largo y persistente", 
        "esPremium": True,
        "fechaResenia": "2019-06-16",
        "puntaje": 2.3,
        "vino": vinos[11],
    },
    {
        "comentario": "Excelente relación calidad-precio",
        "esPremium": False,
        "fechaResenia": "2019-10-08",
        "puntaje": 3.3,
        "vino": vinos[12],
    },
    {
        "comentario": "Buena estructura y cuerpo en boca", 
        "esPremium": True,
        "fechaResenia": "2022-09-05",
        "puntaje": 5.0,
        "vino": vinos[12],
    },
    {
        "comentario": "Perfecto equilibrio entre dulzura y acidez",
        "esPremium": False,
        "fechaResenia": "2024-03-12",
        "puntaje": 3.1,
        "vino": vinos[12],
    },
    {
        "comentario": "Agradable sensación en boca",
        "esPremium": True,
        "fechaResenia": "2022-07-10",
        "puntaje": 4.8,
        "vino": vinos[12],
    },
    {
        "comentario": "Aromas apagados o poco definidos", 
        "esPremium": False,
        "fechaResenia": "2023-06-16",
        "puntaje": 3.5,
        "vino": vinos[13],
    },
    {
        "comentario": "Sabor vibrante y fresco.",
        "esPremium": True,
        "fechaResenia": "2020-09-05",
        "puntaje": 1.5,
        "vino": vinos[13],
    },
    {
        "comentario": "Sabores desequilibrados o astringentes", 
        "esPremium": False,
        "fechaResenia": "2021-05-12",
        "puntaje": 2.3,
        "vino": vinos[13],
    },
    {
        "comentario": "Falta de carácter y personalidad",
        "esPremium": True,
        "fechaResenia": "2021-10-08",
        "puntaje": 4.4,
        "vino": vinos[13],
    },
    {
        "comentario": "Aromas y sabores poco auténticos o artificiales",
        "esPremium": False,
        "fechaResenia": "2023-06-16",
        "puntaje": 5.0,
        "vino": vinos[14],
    },
    {
        "comentario": "Sensación en boca áspera o rugosa", 
        "esPremium": True,
        "fechaResenia": "2022-10-08",
        "puntaje": 3.5,
        "vino": vinos[14],
    },
    {
        "comentario": "Final corto y poco memorable", 
        "esPremium": True,
        "fechaResenia": "2023-06-16",
        "puntaje": 2.3,
        "vino": vinos[14],
    },
    {
        "comentario": "Falta de profundidad y complejidad",
        "esPremium": False,
        "fechaResenia": "2021-05-12",
        "puntaje": 4.8,
        "vino": vinos[14],
    },
    {
        "comentario": "Falta de frescura y vivacidad",
        "esPremium": True,
        "fechaResenia": "2020-09-09",
        "puntaje": 1.5,
        "vino": vinos[5],
    }
]

# Crear instancias de Resenia
resenias = [Resenia(**data) for data in resenia_data]

"""
for resenia in resenias:
    print(resenia.esPremium())
"""

# Asociar resenias a vinos
for resenia in resenias:
    resenia._vino.cargar_resenia(resenia)
    
        

for vino in vinos:              # muestra la coleccion de objetoetos Resenia asociados a cada vino
    print(vino)




        
