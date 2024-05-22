import random
# from NG_Bodega import Bodega

class Pais:
    def __init__(self, nombre) -> None:
        self._nombre = nombre
        self._provincias = []
    
    @property
    def nombre(self):
        return self._nombre        
    
    @property
    def provincias(self):
        return self._provincias
    
    def cargarProvincias(self, provincias:list):
        for provincia in provincias:
            newProvincia = Provincia(self, provincia)
            self._provincias.append(newProvincia)
    
    def contarBodegas(self):
        cantidad = 0    
        for provincia in self._provincias:
            cantidad += provincia.contarBodegas()
        return cantidad

class Provincia():
    def __init__(self, pais, nombre) -> None:
        self._pais = pais
        self._nombre = nombre
        self._regiones = []
        
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def regiones(self):
        return self._regiones
        
    def cargarRegiones(self, regiones:list):
        for region in regiones:
            newRegion = RegionVitivinicola(self, region)
            self._regiones.append(newRegion)
    
    def contarBodegas(self):
        cantidad = 0
        for region in self._regiones:
            cantidad += region.contarBodegas()
        return cantidad 
    
    def obtenerPais(self):
        return self._pais.nombre
    
    def __str__(self) -> str:
        mensaje = f' --- Provincia de {self._nombre} --- \n'
        if len(self._regiones) > 0:
        
            for region in self._regiones:
                mensaje += region.__str__()
        else: 
            mensaje+= "\n No tiene regiones asociadas \n"
        return mensaje
        
class RegionVitivinicola():
    def __init__(self, nombre, descripcion, provincia) -> None:
        self._nombre = nombre
        self._descripcion = descripcion #Cate: Esto lo agregue por los datos de prueba 
        self._provincia = provincia
        self._bodegas = [] 
        
    @property
    def nombre(self):
        return self._nombre    
        
    def cargarBodegas(self, bodegas:list):
        for bodega in bodegas:
            self._bodegas.append(bodega)
            
    def contarBodegas(self):
        return len(self._bodegas)

    def obtenerPais(self):
        return self._provincia.obtenerPais()
    
    def __str__(self) -> str:
        mensaje = f'\n Region = {self._nombre} \n' #{self._nombre}'
        mensaje += f'Cantidad de bodegas = {len(self._bodegas) if (len(self._bodegas)>0) else "No tiene Bodegas"}\n'
        return mensaje
            
            
if __name__ == "__main__":
    argentina = Pais("Argentina")
    provincias = [
    "Buenos Aires",
    "Catamarca",
    "Chubut",
    "Córdoba",
    "Corrientes",
    "Entre Ríos",
    "Formosa",
    "Jujuy",
    "La Pampa",
    "La Rioja",
    "Mendoza",
    "Misiones",
    "Neuquén",
    "Río Negro",
    "San Juan",
    "San Luis",
    "Santa Cruz",
    "Santa Fe",
    "Santiago del Estero",
    "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
    "Tucumán"
]
    
    regiones_vitivinicolas = {
        "Buenos Aires": ["Costa Atlántica", "Valle de Uco"],
        "Catamarca": ["Cafayate", "Hualfin"],
        "Chubut": ["Valle del Río Chubut", "Valle Inferior del Río Chubut"],
        "Córdoba": ["Sierras de Córdoba", "Valle Calamuchita"],
        "Corrientes": ["Río Uruguay", "Litoral Norte"],
        "Entre Ríos": ["Río Uruguay", "Delta del Paraná"],
        "Formosa": [],  # No wine regions currently listed
        "Jujuy": ["Quebrada de Humahuaca", "Valles Calileños"],
        "La Pampa": [],  # No wine regions currently listed
        "La Rioja": ["Chilecito", "Famatina"],
        "Mendoza": ["Valle de Uco", "Valle Central"],
        "Misiones": [],  # No wine regions currently listed
        "Neuquén": ["Neuquén", "Alto Valle del Río Negro"],
        "Río Negro": ["Alto Valle del Río Negro", "Valle Inferior del Río Negro"],
        "San Juan": ["Valle de Tulum", "Valle de Pedernales"],
        "San Luis": ["Valle de San Francisco", "Valle del Conlara"],
        "Santa Cruz": [],  # No wine regions currently listed
        "Santa Fe": ["Río Paraná", "Salto Grande"],
        "Santiago del Estero": ["Quebrada de las Salinas", "Ribera del Dulce"],
        "Tierra del Fuego, Antártida e Islas del Atlántico Sur": [],  # No wine regions currently listed
        "Tucumán": ["Cafayate", "Tafí del Valle"]
    }

    bodegas_creativas = [
        "Viñedos del Alba",
        "Cumbres Andinas",
        "Sol Naciente",
        "Valle Escondido",
        "Manos Argentinas",
        "Sabor Malbec",
        "Corazón de Tierra",
        "Frutos del Viento",
        "Viñedos del Sur",
        "Estrellas del Desierto",
        "Leyendas del Vino",
        "Alma Gaucha",
        "Raíces Argentinas",
        "Viñedos del Río",
        "Horizontes Libres",
        "Sueños de Uva",
        "Tesoros del Terroir",
        "Viñedos del Sol",
        "Ecos del Viento"
    ]
    argentina.cargarProvincias(provincias)
    cantidad = 0
    for provincia in argentina.provincias:
        provincia.cargarRegiones(regiones_vitivinicolas.get(provincia.nombre))
        for region in provincia.regiones:
            a = random.randrange(0,18)
            b = random.randrange(a, 18)
            region.cargarBodegas(bodegas_creativas[a:b])
            cantidad += len(bodegas_creativas[a:b])
            
            
        #print(provincia)
        
    #print(argentina.contarBodegas())
