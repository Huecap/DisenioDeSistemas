# Cosas que tenemos que tener en cuenta para la entrega 1

[Volver](../README.md)

---

- Cree un entorno de trabajo para trabajar mejor para ejecutarlo
  - Windows = `.\env\bin\activate`
  - Linux = `source env/bin/activate`

> Esto sirve para cuando clonen el repo, directamente todas las dependencias esten instaladas y no haya problemas con las versiones de python que tengan

---

## Estructura del proyecto

### Nombre de archivos

- `HR` = Herramientas (todo lo que sea metodos de validacion, carga, etc. Los ponemos aca)
- `NG` = Todo lo relacionado a la lógica del Negocio va ava
- `IN` = Todo lo relacionado con la interfaz va aca
- `Aplicacion.py` = Este es el archivo principal, el que se debe ejecutar para que el programa funcione

---

### Elementos a tener en cuenta

- Tanto los setters como los getters, en python generalmente se definen con el mismo nombre del atributo que queremos acceder
*Ejemplo*

```python
    @property
    def nombre(self):
        return self.__nombre


    # En vez de 
    @property
    def getNombre(self):
        return self.__nombre
```

---

## Cosas que tenemos que hacer

### En el Análisis

- [ ] Cambiar el nombre de los metodos que usamos para que no queden distintos
- [ ]

### En la implementación

---

#### Interfaz

- [ ] Creacion de Clase interafaz

---

#### Logica de Negocio

---

- [ ] Creacion de clase Gestor
  - [ ]

---

- [x] Creacion Clase Vino
  - [ ] metodo `calcularRanking()`
  - [ ] metodo `compararEtiqueta()`
  - [ ] metodo `esDeBodega()`
  - [ ] metodo `esDeRegionVitivinicola()`

> Entiendo que el comparar no va xd

---

- [x] Creacion de Clase Varietal
  - [x] metodo `conocerTipoUva()`
  - [x] metodo `esDeTipoUva()`
  - [x] metodo `mostrarPorcentaje()`

---

- [x] Creacion de clase TipoUva

---

- [ ] Creacion de Clase Maridaje
  - [ ] metodo `maridaConVino`

---

- [x] Creacion Clase Reseñas

---

- [x] Creacion Clase Usuario
  - [ ]  No me acuerdo si este metodo cambia la propiedad esPremium o directamente retorna si es premium o no
  - [ ]  

---

- [x] Creacion Clase Somelier
  - [ ] No me acuerdo si el metodo esPremium() solo devuelve si es de somelier o modifica el estado del atributo esPremium

---

- [x] Creacion Clase Bodega
  - [x] metodo `contarResenias()`
  - [x] metodo `mostrarTodosVinos()`
- [x] Creacion Clase RegionVitivinicola
  - [x] metodo `conocerBodega()`
  - [x] metodo `contarBodegas()`
- [x] Creacion Clase Provincia
  - [x] metodo `contarRegiones()`
  - [x] metodo `mostrarRegioines`
  - [x] metodo `contarBodegas()`
- [x] Creacion Clase País
  - [x] metodo `contarBodegas()`

---

- [ ]  Validaciones de los setters

> En general hay que verificar las validaciones porque no valide nada

---
***Clases no implementadas***
- NovedadEvento
- Siguiendo
- Enofilo
- Certificación
- CobroPremium