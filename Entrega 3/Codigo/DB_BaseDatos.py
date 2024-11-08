import sqlite3
from datetime import datetime
from sqlite3 import Connection

class DatabaseSingleton:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, db_name="database.db"):
        # Si no existe una instancia, crear una nueva
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            # Inicializar la conexión de la base de datos
            cls._instance._connection = sqlite3.connect(db_name)
        return cls._instance

    def get_connection(self) -> Connection:
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            DatabaseSingleton._instance = None  # Resetear la instancia para que pueda ser creada de nuevo

    def create_table(self, consult):
        with self.get_connection():
            self.get_connection().execute(consult)
            print("Tabla creada o ya existe en la base de datos.")
            
            
    def crearTablas(self):
        db_instance = self._instance
        connection = db_instance.get_connection()

        # Crear una tabla de ejemplo

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS varietal (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    descripcion TEXT NOT NULL,
                                    porcentaje DOUBLE NOT NULL,
                                    tipoUva_id INTEGER,
                                    FOREIGN KEY (tipoUva_id) REFERENCES tipoUva(id)
                                )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS maridaje (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    descripcion TEXT NOT NULL,
                                    nombre TEXT NOT NULL
                                )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS tipoUva (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL,
                                    descripcion TEXT NOT NULL
                                    )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS resenia (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    comentario TEXT NOT NULL,
                                    puntaje DOUBLE NOT NULL,
                                    esPremium BOOLEAN,
                                    fechaResenia DATE,
                                    vino_id INTEGER,
                                    FOREIGN KEY (vino_id) REFERENCES vino(id)
                                    )''')
        db_instance.create_table('''CREATE TABLE IF NOT EXISTS pais (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL
                                    )''')


        db_instance.create_table('''CREATE TABLE IF NOT EXISTS provincia (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL,
                                    pais_id,
                                    FOREIGN KEY (pais_id) REFERENCES pais(id)
                                    )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS regionVitivinicola (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL,
                                    descripcion TEXT NOT NULL, 
                                    provincia_id,
                                    FOREIGN KEY (provincia_id) REFERENCES provincia(id)
                                    )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS bodega (
            
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    coordenadas TEXT NOT NULL,
                                    descripcion TEXT NOT NULL,
                                    historia TEXT NOT NULL,
                                    nombre TEXT NOT NULL,
                                    periodo_actualizacion DATE,
                                    region_id,
                                    FOREIGN KEY (region_id) REFERENCES region(id)
                                    )''')

        db_instance.create_table('''CREATE TABLE IF NOT EXISTS vino (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL,
                                    aniada INT NOT NULL,
                                    image VARCHAR,
                                    precioArs DOUBLE NOT NULL,
                                    maridaje_id INT,
                                    varietal_id INT,
                                    bodega_id INT,
                                    FOREIGN KEY (maridaje_id) REFERENCES maridaje(id),
                                    FOREIGN KEY (varietal_id) REFERENCES varietal(id),
                                    FOREIGN KEY (bodega_id) REFERENCES bodega(id)
                                )''')

    def cargarTablas(self):
        # ? Cargar maridaje
        db_instance = self._instance
        connection = self.get_connection()    
            # Datos de ejemplo para Maridaje
        maridajes_data = [
                {"descripcion": "Perfecto con carnes rojas.", "nombre": "Carnes Rojas"},
                {"descripcion": "Ideal con pescados y mariscos.", "nombre": "Pescados y Mariscos"},
                {"descripcion": "Excelente con pastas.", "nombre": "Pastas"},
                {"descripcion": "Acompaña muy bien quesos.", "nombre": "Quesos"},
                {"descripcion": "Marida con aves.", "nombre": "Aves"}
            ]

        for maridaje in maridajes_data:
            with connection:
                connection.execute("INSERT INTO maridaje (descripcion, nombre) VALUES(?,?)", (maridaje["descripcion"], maridaje["nombre"]))


        # ? Cargar Vinos 

            # Datos de ejemplo para Vino
        vinos = [
                {
                    "aniada": "2019",
                    "imagen_etiqueta": "imagen_vino1.jpg",
                    "nombre": "Vino Tinto Reserva",
                    "nota_de_cata_bodega": 4.5,
                    "precio_ARS": 750.0,
                    "maridaje": 1,
                    "varietal": 1,
                    "bodega": 1,
                },
                {
                    "aniada": "2020",
                    "imagen_etiqueta": "imagen_vino2.jpg",
                    "nombre": "Vino Blanco Joven",
                    "nota_de_cata_bodega": 4.2,
                    "precio_ARS": 550.0,
                    "maridaje": 2,
                    "varietal":1,
                    "bodega": 2,
                },
                {
                    "aniada": "2023",
                    "imagen_etiqueta": "imagen_vino3.jpg",
                    "nombre": "Vino Tinto Añejo",
                    "nota_de_cata_bodega": 5.0,
                    "precio_ARS": 1200.5,
                    "maridaje": 3,
                    "varietal": 3,
                    "bodega": 4,
                }, 
                {
                    "aniada": "2021",
                    "imagen_etiqueta": "imagen_vino4.jpg",
                    "nombre": "Vino Tinto Reserva Elegante",
                    "nota_de_cata_bodega": 3.0,
                    "precio_ARS": 400.0,
                    "maridaje": 5,
                    "varietal": 2,
                    "bodega": 3,
                },
                {
                    "aniada": "2022",
                    "imagen_etiqueta": "imagen_vino5.jpg",
                    "nombre": "Vino Tinto Espléndido",
                    "nota_de_cata_bodega": 2.8,
                    "precio_ARS": 900.0,
                    "maridaje": 5,
                    "varietal": 4,
                    "bodega":4,
                },
                {
                    "aniada": "2018",
                    "imagen_etiqueta": "imagen_vino6.jpg",
                    "nombre": "Vino Tinto Reserva Clásico",
                    "nota_de_cata_bodega": 4.6,
                    "precio_ARS": 950.5,
                    "maridaje": 3,
                    "varietal": 5,
                    "bodega": 3,
                },
                {
                    "aniada": "2019",
                    "imagen_etiqueta": "imagen_vino7.jpg",
                    "nombre": "Vino Tinto Noble",
                    "nota_de_cata_bodega": 5.0,
                    "precio_ARS": 880.6,
                    "maridaje": 2,
                    "varietal": 1,
                    "bodega": 2,
                },
                {
                    "aniada": "2020",
                    "imagen_etiqueta": "imagen_vino8.jpg",
                    "nombre": "Vino Tinto Reserva Exquisito",
                    "nota_de_cata_bodega": 1.0,
                    "precio_ARS": 740.0,
                    "maridaje": 1,
                    "varietal": 3,
                    "bodega":1,
                },
                {
                    "aniada": "2021",
                    "imagen_etiqueta": "imagen_vino9.jpg",
                    "nombre": "Vino Blanco Joven Fresco",
                    "nota_de_cata_bodega": 1.5,
                    "precio_ARS": 650.0,
                    "maridaje": 3,
                    "varietal":3,
                    "bodega":1,
                },
                {
                    "aniada": "2022",
                    "imagen_etiqueta": "imagen_vino10.jpg",
                    "nombre": "Vino Blanco Vivo",
                    "nota_de_cata_bodega": 2.7,
                    "precio_ARS": 980.8,
                    "maridaje": 5,
                    "varietal": 5,
                    "bodega": 2,
                },
                {
                    "aniada": "2023",
                    "imagen_etiqueta": "imagen_vino11.jpg",
                    "nombre": "Vino Blanco Joven Delicado",
                    "nota_de_cata_bodega": 3.0,
                    "precio_ARS": 200.0,
                    "maridaje": 4,
                    "varietal": 3,
                    "bodega": 3,
                },
                {
                    "aniada": "2017",
                    "imagen_etiqueta": "imagen_vino12.jpg",
                    "nombre": "Vino Blanco Joven Radiante",
                    "nota_de_cata_bodega": 4.6,
                    "precio_ARS": 1000.5,
                    "maridaje": 5,
                    "varietal": 4,
                    "bodega":5,
                },
                {
                    "aniada": "2018",
                    "imagen_etiqueta": "imagen_vino13.jpg",
                    "nombre": "Vino Blanco Luminoso",
                    "nota_de_cata_bodega": 4.9,
                    "precio_ARS": 2500.0,
                    "maridaje": 2,
                    "varietal": 2,
                    "bodega": 4,
                },
                {
                    "aniada": "2019",
                    "imagen_etiqueta": "imagen_vino14.jpg",
                    "nombre": "Vino Blanco Suave",
                    "nota_de_cata_bodega": 3.9,
                    "precio_ARS": 750.5,
                    "maridaje": 2,
                    "varietal": 1,
                    "bodega": 3,
                },
                {
                    "aniada": "2020",
                    "imagen_etiqueta": "imagen_vino15.jpg",
                    "nombre": "Vino Blanco Afrutado",
                    "nota_de_cata_bodega": 2.2,
                    "precio_ARS": 600.6,
                    "maridaje": 2,
                    "varietal": 1,
                    "bodega":2,
                }
            ]



        for vino in vinos:     
            with connection: 
                connection.execute("INSERT INTO vino (nombre, aniada, image, precioArs, maridaje_id, varietal_id, bodega_id) VALUES(?, ? ,? ,?, ?,?,?)", (vino["nombre"],int(vino["aniada"]), vino["imagen_etiqueta"], vino["precio_ARS"], vino["maridaje"], vino["varietal"], vino["bodega"]) )            


        # Cargar Resenia
        resenia_data = [
                {
                    "comentario": "Excelente vino, muy equilibrado y con gran aroma",
                    "esPremium": True,
                    "fechaResenia": "2022-05-15",
                    "puntaje": 4.8,
                    "vino": 1,
                },
                {
                    "comentario": "Buen vino, relación calidad-precio adecuada",
                    "esPremium": False,
                    "fechaResenia": "2022-05-10",
                    "puntaje": 4.0,
                    "vino": 1,
                },
                {
                    "comentario": "Un vino con cuerpo y notas de frutas maduras",
                    "esPremium": False,
                    "fechaResenia": "2020-08-25",
                    "puntaje": 3.5,
                    "vino": 1,
                },
                {
                    "comentario": "Buen equilibrio entre fruta y acidez",
                    "esPremium": False,
                    "fechaResenia": "2021-09-10",
                    "puntaje": 5.0,
                    "vino": 1,
                },
                {
                    "comentario": "Aromas apagados y poco definidos",
                    "esPremium": True,
                    "fechaResenia": "2021-05-11",
                    "puntaje": 1.5,
                    "vino": 2,
                },
                {
                    "comentario": "Aromas apagados y poco definidos",
                    "esPremium": False,
                    "fechaResenia": "2022-12-18",
                    "puntaje": 2.3,
                    "vino": 2,
                },
                {
                    "comentario": "Final largo y persistente",
                    "esPremium": True,
                    "fechaResenia": "2023-10-02",
                    "puntaje": 3.3,
                    "vino": 2,
                },
                {
                    "comentario": "Presencia de defectos como corcho o avinagramiento",
                    "esPremium": True,
                    "fechaResenia": "2024-02-28",
                    "puntaje": 4.4,
                    "vino": 2,
                },
                {
                    "comentario": "Buen equilibrio entre fruta y acidez",
                    "esPremium": False,
                    "fechaResenia": "2024-04-16",
                    "puntaje": 4.5,
                    "vino": 3,
                },
                {
                    "comentario": "Sabor vibrante y fresco",
                    "esPremium": False,
                    "fechaResenia": "2024-02-22",
                    "puntaje": 5.0,
                    "vino": 3,
                },
                {
                    "comentario": "Poca intensidad aromática",
                    "esPremium": True,
                    "fechaResenia": "2024-01-31",
                    "puntaje": 4.8,
                    "vino": 3,
                },
                {
                    "comentario": "Aromas apagados y poco definidos",
                    "esPremium": False,
                    "fechaResenia": "2024-03-12",
                    "puntaje": 1.7,
                    "vino": 3,
                },
                {
                    "comentario": "Precio elevado para la calidad ofrecida",
                    "esPremium": True,
                    "fechaResenia": "2022-12-31",
                    "puntaje": 3.5,
                    "vino": 4,
                },
                {
                    "comentario": "Elegante y refinado en nariz y paladar",
                    "esPremium": True,
                    "fechaResenia": "2023-11-29",
                    "puntaje": 2.8,
                    "vino": 4,
                },
                {
                    "comentario": "La intensidad de los sabores se mantiene bien equilibrada en todo momento",
                    "esPremium": False,
                    "fechaResenia": "2022-09-05",
                    "puntaje": 1.5,
                    "vino": 4,
                },
                {
                    "comentario": "La relación calidad-precio no está justificada por la experiencia sensorial que ofrece",
                    "esPremium": True,
                    "fechaResenia": "2023-07-04",
                    "puntaje": 3.9,
                    "vino": 4,
                },
                {
                    "comentario": "El equilibrio entre la acidez y los taninos es perfecto",
                    "esPremium": True,
                    "fechaResenia": "2023-09-13",
                    "puntaje": 2.3,
                    "vino": 5,
                },
                {
                    "comentario": "Su textura en boca es suave y sedosa, creando una experiencia sensorial placentera",
                    "esPremium": False,
                    "fechaResenia": "2024-08-14",
                    "puntaje": 4.8,
                    "vino": 5,
                },
                {
                    "comentario": "Textura suave y sedosa en boca",
                    "esPremium": False,
                    "fechaResenia": "2024-07-15",
                    "puntaje": 5.0,
                    "vino": 5,
                },
                {
                    "comentario": "Taninos agresivos y astringentes",
                    "esPremium": True,
                    "fechaResenia": "2023-06-16",
                    "puntaje": 3.5,
                    "vino": 5,
                },
                {
                    "comentario": "El equilibrio entre la acidez y los taninos es perfecto",
                    "esPremium": False,
                    "fechaResenia": "2019-10-08",
                    "puntaje": 4.6,
                    "vino": 6,
                },
                {
                    "comentario": "Armonía entre taninos y fruta",
                    "esPremium": True,
                    "fechaResenia": "2020-09-09",
                    "puntaje": 3.6,
                    "vino": 6,
                },
                {
                    "comentario": "La persistencia en el paladar es corta y poco memorable",
                    "esPremium": True,
                    "fechaResenia": "2021-08-10",
                    "puntaje": 1.5,
                    "vino": 6,
                },
                {
                    "comentario": "Aromas complejos y seductores",
                    "esPremium": False,
                    "fechaResenia": "2022-07-11",
                    "puntaje": 4.6,
                    "vino": 6,
                },
                {
                    "comentario": "Final largo y persistente",
                    "esPremium": False,
                    "fechaResenia": "2020-04-18",
                    "puntaje": 2.3,
                    "vino": 7,
                },
                {
                    "comentario": "Sensación áspera en boca",
                    "esPremium": True,
                    "fechaResenia": "2021-03-19",
                    "puntaje": 4.8,
                    "vino": 7,
                },
                {
                    "comentario": "Gran profundidad y complejidad",
                    "esPremium": False,
                    "fechaResenia": "2022-02-20",
                    "puntaje": 3.5,
                    "vino": 7,
                },
                {
                    "comentario": "El vino parece haber sido elaborado con uvas de baja calidad, afectando su perfil aromático y gustativo",
                    "esPremium": True,
                    "fechaResenia": "2023-01-21",
                    "puntaje": 1.7,
                    "vino": 7,
                },
                {
                    "comentario": "Exceso de alcohol que domina el perfil",
                    "esPremium": False,
                    "fechaResenia": "2021-08-09",
                    "puntaje": 2.8,
                    "vino": 8,
                },
                {
                    "comentario": "Es un vino elegante y refinado que destaca por su complejidad y profundidad de sabor",
                    "esPremium": True,
                    "fechaResenia": "2022-07-10",
                    "puntaje": 2.7,
                    "vino": 8,
                },
                {
                    "comentario": "Notas de frutas maduras y especias",
                    "esPremium": True,
                    "fechaResenia": "2022-06-11",
                    "puntaje": 5.0,
                    "vino": 8,
                },
                {
                    "comentario": "Es un vino versátil que se puede maridar con una amplia variedad de platos",
                    "esPremium": False,
                    "fechaResenia": "2021-05-12",
                    "puntaje": 1.5,
                    "vino": 8,
                },
                {
                    "comentario": "Este vino tiene una excelente relación calidad-precio",
                    "esPremium": True,
                    "fechaResenia": "2021-09-29",
                    "puntaje": 4.8,
                    "vino": 9,
                },
                {
                    "comentario": "Falta de complejidad y profundidad",
                    "esPremium": False,
                    "fechaResenia": "2021-10-17",
                    "puntaje": 2.3,
                    "vino": 9,
                },
                {
                    "comentario": "La relación calidad-precio no está justificada por la experiencia sensorial que ofrece",
                    "esPremium": True,
                    "fechaResenia": "2022-07-27",
                    "puntaje": 4.1,
                    "vino": 9,
                },
                {
                    "comentario": "La añada de este vino particular ha resultado excepcional, resaltando su calidad",
                    "esPremium": False,
                    "fechaResenia": "2023-11-12",
                    "puntaje": 3.5,
                    "vino": 9,
                },
                {
                    "comentario": "Estructura bien integrada",
                    "esPremium": True,
                    "fechaResenia": "2023-06-16",
                    "puntaje": 3.1,
                    "vino": 10,
                },
                {
                    "comentario": "Sensación de desequilibrio entre los componentes",
                    "esPremium": True,
                    "fechaResenia": "2023-10-08",
                    "puntaje": 4.8,
                    "vino": 10,
                },
                {
                    "comentario": "La añada de este vino particular ha resultado excepcional, resaltando su calidad",
                    "esPremium": False,
                    "fechaResenia": "2022-09-05",
                    "puntaje": 1.5,
                    "vino": 10,
                },
                {
                    "comentario": "Final corto y decepcionante",
                    "esPremium": False,
                    "fechaResenia": "2024-03-12",
                    "puntaje": 2.3,
                    "vino": 10,
                },
                {
                    "comentario": "Buena expresión varietal",
                    "esPremium": True,
                    "fechaResenia": "2023-07-10",
                    "puntaje": 5.0,
                    "vino": 11,
                },
                {
                    "comentario": "Armonía entre taninos y fruta",
                    "esPremium": True,
                    "fechaResenia": "2024-03-12",
                    "puntaje": 4.8,
                    "vino": 11,
                },
                {
                    "comentario": "Buen equilibrio entre acidez, dulzura y amargura",
                    "esPremium": False,
                    "fechaResenia": "2024-03-12",
                    "puntaje": 2.7,
                    "vino": 11,
                },
                {
                    "comentario": "Notas de madera o roble demasiado pronunciadas",
                    "esPremium": False,
                    "fechaResenia": "2023-10-08",
                    "puntaje": 2.8,
                    "vino": 11,
                },
                {
                    "comentario": "Aromas complejos y cautivadores", 
                    "esPremium": True,
                    "fechaResenia": "2022-07-10",
                    "puntaje": 3.5,
                    "vino": 12,
                },
                {
                    "comentario": "Sabor suave y sedoso en el paladar", 
                    "esPremium": False,
                    "fechaResenia": "2021-08-10",
                    "puntaje": 1.5,
                    "vino": 12,
                },
                {
                    "comentario": "Exceso de dulzura o acidez desequilibrada",
                    "esPremium": True,
                    "fechaResenia": "2018-05-12",
                    "puntaje": 3.6,
                    "vino": 12,
                },
                {
                    "comentario": "Final largo y persistente", 
                    "esPremium": True,
                    "fechaResenia": "2019-06-16",
                    "puntaje": 2.3,
                    "vino": 12,
                },
                {
                    "comentario": "Excelente relación calidad-precio",
                    "esPremium": False,
                    "fechaResenia": "2019-10-08",
                    "puntaje": 3.3,
                    "vino": 13,
                },
                {
                    "comentario": "Buena estructura y cuerpo en boca", 
                    "esPremium": True,
                    "fechaResenia": "2022-09-05",
                    "puntaje": 5.0,
                    "vino": 13,
                },
                {
                    "comentario": "Perfecto equilibrio entre dulzura y acidez",
                    "esPremium": True,
                    "fechaResenia": "2024-05-22",
                    "puntaje": 3.1,
                    "vino": 13,
                },
                {
                    "comentario": "Agradable sensación en boca",
                    "esPremium": True,
                    "fechaResenia": "2022-07-10",
                    "puntaje": 4.8,
                    "vino": 13,
                },
                {
                    "comentario": "Aromas apagados o poco definidos", 
                    "esPremium": False,
                    "fechaResenia": "2023-06-16",
                    "puntaje": 3.5,
                    "vino": 14,
                },
                {
                    "comentario": "Sabor vibrante y fresco.",
                    "esPremium": True,
                    "fechaResenia": "2020-09-05",
                    "puntaje": 1.5,
                    "vino": 14,
                },
                {
                    "comentario": "Sabores desequilibrados o astringentes", 
                    "esPremium": False,
                    "fechaResenia": "2021-05-12",
                    "puntaje": 2.3,
                    "vino": 14,
                },
                {
                    "comentario": "Falta de carácter y personalidad",
                    "esPremium": True,
                    "fechaResenia": "2021-10-08",
                    "puntaje": 4.4,
                    "vino": 14,
                },
                {
                    "comentario": "Aromas y sabores poco auténticos o artificiales",
                    "esPremium": False,
                    "fechaResenia": "2023-06-16",
                    "puntaje": 5.0,
                    "vino": 15,
                },
                {
                    "comentario": "Sensación en boca áspera o rugosa", 
                    "esPremium": True,
                    "fechaResenia": "2022-10-08",
                    "puntaje": 3.5,
                    "vino": 15,
                },
                {
                    "comentario": "Final corto y poco memorable", 
                    "esPremium": True,
                    "fechaResenia": "2023-06-16",
                    "puntaje": 2.3,
                    "vino": 15,
                },
                {
                    "comentario": "Falta de profundidad y complejidad",
                    "esPremium": False,
                    "fechaResenia": "2021-05-12",
                    "puntaje": 4.8,
                    "vino": 15,
                },
                {
                    "comentario": "Falta de frescura y vivacidad",
                    "esPremium": True,
                    "fechaResenia": "2020-09-09",
                    "puntaje": 1.5,
                    "vino": 6,
                }
            ]
        resenia = {
                    "comentario": "Excelente vino, muy equilibrado y con gran aroma",
                    "esPremium": 1,
                    "fechaResenia": "2022-05-15",
                    "puntaje": 4.8,
                    "vino": 1
                }


        for resenia in resenia_data:
            date_format = "%Y-%m-%d"
            fechaResenia = datetime.strptime(resenia["fechaResenia"], date_format).date()  
            with connection:                 
                connection.execute("INSERT INTO resenia (comentario, puntaje, esPremium, fechaResenia, vino_id) VALUES(?, ? ,? ,?,?)", (resenia["comentario"], resenia["puntaje"], resenia["esPremium"], fechaResenia, resenia["vino"]) )

        #? Cargar Tipo de UVA
        tipos_uva_data = [
                {"nombre": "Malbec", "descripcion": "Uva tinta fuerte y robusta."},
                {"nombre": "Cabernet Sauvignon", "descripcion": "Uva tinta con notas de frutas oscuras."},
                {"nombre": "Pinot Noir", "descripcion": "Uva tinta ligera y elegante."}, 
                {"nombre": "Syrah", "descripcion": "Uva tinta con sabores a especias."},
                {"nombre": "Merlot", "descripcion": "Uva tinta suave y afrutada."},

            ]

        for uva in tipos_uva_data:
            with connection:
                connection.execute("INSERT INTO tipoUva (nombre, descripcion) VALUES (?, ?)", (uva["nombre"], uva["descripcion"]))


        # ? Cargar Varietal 
        varietal_data = [
                {"descripcion": "Malbec", "tipo_uva": 1, "porcentaje_composicion": 100},
                {"descripcion": "Cabernet Sauvignon","tipo_uva": 2, "porcentaje_composicion": 100},
                {"descripcion": "Pinot Noir","tipo_uva": 3, "porcentaje_composicion": 100},
                {"descripcion": "Syrah","tipo_uva": 4, "porcentaje_composicion": 100},
                {"descripcion": "Merlot","tipo_uva": 5, "porcentaje_composicion": 100},
            ]

        for varietal in varietal_data:
            with connection:
                connection.execute("INSERT INTO varietal (descripcion, porcentaje, tipoUva_id) VALUES (?, ?, ?)", (varietal["descripcion"], varietal["porcentaje_composicion"], varietal["tipo_uva"]))


        #? Cargar Pais 
        paises_data = [
                {"nombre": "Argentina"},
                {"nombre": "Chile"}
            ]

        for pais in paises_data:
            with connection:
                connection.execute("INSERT INTO pais (nombre) VALUES(?)", (pais["nombre"],))
                
                
        # ? Cargar provincias 
        provincias_data = [
                {"nombre": "Mendoza", "pais": 1},
                {"nombre": "San Juan", "pais": 1},
                {"nombre": "La Rioja", "pais": 1},
                {"nombre": "Buenos Aires", "pais": 1},
                {"nombre": "Colchagua", "pais": 2},
                {"nombre": "Maule", "pais": 2},
                {"nombre": "Casablanca", "pais": 2},
                {"nombre": "Biobío", "pais": 2}
            ]

        for provincia in provincias_data:
            with connection:
                connection.execute("INSERT INTO provincia (nombre, pais_id) VALUES(?,?)", (provincia["nombre"], provincia["pais"]))

        regiones_data = [
                {"nombre": "Valle de Uco", "descripcion": "Una región vinícola famosa por sus vinos Malbec.", "provincia": 1},
                {"nombre": "Valle del Tulum", "descripcion": "Una región vinícola con clima templado y suelos fértiles.", "provincia": 2},
                {"nombre": "Valle de Famatina", "descripcion": "Un valle rodeado de montañas que produce vinos de altura.", "provincia": 3},
                {"nombre": "Pampas", "descripcion": "Una vasta llanura fértil conocida por su ganadería y agricultura.", "provincia": 4},
                {"nombre": "Valle de Colchagua", "descripcion": "Un valle chileno famoso por sus vinos tintos.", "provincia": 5},
                {"nombre": "Valle del Maule", "descripcion": "Una región vinícola diversa con una larga historia vitivinícola.", "provincia": 6},
                {"nombre": "Valle de Casablanca", "descripcion": "Una región vinícola costera conocida por sus vinos blancos.", "provincia": 7},
                {"nombre": "Valle del Biobío", "descripcion": "Un valle rodeado de ríos y montañas que produce vinos frescos y frutales.", "provincia": 8}
            ]

        for region in regiones_data:
            with connection:
                connection.execute("INSERT INTO regionVitivinicola (nombre, descripcion, provincia_id) VALUES(?, ? ,?)", (region["nombre"], region["descripcion"], region["provincia"]))


        bodega_data = [
                {
                    "coordenadas_ubicacion": "39.9526, -75.1652",
                    "descripcion": "Bodega con vasta experiencia en vinos de autor",
                    "historia": "Establecida en 1960 por Don Antonio Martínez",
                    "nombre": "Bodega Martínez",
                    "periodo_actualizacion": "2022-04-30",
                    "region": 3
                },
                {
                    "coordenadas_ubicacion": "37.7749, -122.4194",
                    "descripcion": "Bodega moderna con enfoque en sostenibilidad",
                    "historia": "Fundada en 2000 por la enóloga María García",
                    "nombre": "Bodega García",
                    "periodo_actualizacion": "2022-05-10",
                    "region": 3
                },
                {
                    "coordenadas_ubicacion": "41.8781, -87.6298",
                    "descripcion": "Bodega reconocida por sus vinos de alta gama",
                    "historia": "Con más de 100 años de tradición en viticultura",
                    "nombre": "Bodega López",
                    "periodo_actualizacion": "2022-05-05",
                    "region": 5
                },
                {
                    "coordenadas_ubicacion": "34.0522, -118.2437",
                    "descripcion": "Bodega boutique con vinos exclusivos",
                    "historia": "Inaugurada en 1990 por la familia Rodríguez",
                    "nombre": "Bodega Rodríguez",
                    "periodo_actualizacion": "2022-04-25",
                    "region": 2
                }
            ]
        bodega = {
                    "coordenadas_ubicacion": "34.0522, -118.2437",
                    "descripcion": "Bodega boutique con vinos exclusivos",
                    "historia": "Inaugurada en 1990 por la familia Rodríguez",
                    "nombre": "Bodega Rodríguez",
                    "periodo_actualizacion": "2022-04-25",
                    "region": 2
                }
        for bodega in bodega_data:
            with connection:
                date_format = "%Y-%m-%d"
                periodo = datetime.strptime(bodega["periodo_actualizacion"], date_format).date() 
                connection.execute("INSERT INTO bodega (coordenadas, descripcion, historia, nombre, periodo_actualizacion, region_id) VALUES(?,?,?,?,?,?)", 
                                (bodega["coordenadas_ubicacion"], bodega["descripcion"], bodega["historia"], bodega["nombre"], periodo, bodega["region"]))
    
    # Datos de los vinos
    def obtenerDatosVino(self):
        connection = self.get_connection()
        datos = connection.execute("SELECT * FROM vino")
        for n in datos:
            print(n)
    
    def obtenerDatosTipoUva(self):
        connection = self.get_connection()
        datos = connection.execute("SELECT * FROM tipoUva")
        for n in datos:
            print(n)
    
            
data_base = DatabaseSingleton("base_de_datos.db")
# data_base.crearTablas()
# data_base.cargarTablas()
data_base.obtenerDatosTipoUva()