# Cosas que tenemos que tener en cuenta para la entrega 1

[Volver](../README.md)

---

- Cree un entorno de trabajo para trabajar mejor para ejecutarlo
  - Windows = `.\env\bin\activate`
  - Linux = `source env/bin/activate`

> Esto sirve para cuando clonen el repo, directamente todas las dependencias esten instaladas y no haya problemas con las versiones de python que tengan.
>
> Si quieren pueden ejecutarlo directamente en su maquina, no hay drama con eso. Pero si utilizan algun modulo o libreria ponganlo en la parte de dependencias

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

## Dependencias

- `random` = Generar valores aleatorios
- `datetime` = Para manejar valores del tipo fecha
-

---
