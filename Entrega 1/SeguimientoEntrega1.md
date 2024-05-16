# Cosas que tenemos que tener en cuenta para la entrega 1

- Cree un entorno de trabajo para trabajar mejor para ejecutarlo
  - Windows = `.\env\bin\activate`
  - Linux = `source env/bin/activate `
> Esto sirve para cuando clonen el repo, directamente todas las dependencias esten instaladas y no haya problemas con las versiones de python que tengan

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

#### En el Análisis 
- [ ] Cambiar el nombre de los metodos que usamos para que no queden distintos
- [ ] 

#### En la implementación 

***En todas las clases***
- [ ] Creacion Clase Vino
  - [ ] 
- [ ] Creacion Clase Reseñas
- [ ] Creacion Clase Usuario
  - [ ]  No me acuerdo si este metodo cambia la propiedad esPremium o directamente retorna si es premium o no
- [ ] Creacion Clase Somelier
  - [ ] No me acuerdo si el metodo esPremium() solo devuelve si es de somelier o modifica el estado del atributo esPremium
- [ ] Creacion Clase 

- [ ]  Validaciones de los setters 

