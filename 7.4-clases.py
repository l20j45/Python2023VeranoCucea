class Person:
    def __init__(self,codigo, name, age,status,carrera):
        self.codigo = codigo
        self.name = name
        self.age = age
        self.status = status
        self.carrera = carrera
        self._age = age 
         
    def __str__(self):
        return f'hola mi nombre es {self.name} y mi edad es {self.age} persona'

class student(Person):  	
    def __init__(self,codigo, name, age,status,carrera,promedio,semestre):
        super().__init__(codigo,name, age,status,carrera)
        self.promedio = promedio
        self.semestre = semestre
    
    def __str__(self):
        return f'hola mi nombre es {self.name} y mi edad es {self.age} alumno'
persona1 = Person(1231,'raul',29,'activo','licenciatura')
alumno1 = student(130,'raul2',29,'activo','licenciatura',89,9)

print(f'{persona1.codigo} {persona1.name}')
print(f'{alumno1.codigo} {alumno1.name}')

print(f'{persona1}')
print(f'{alumno1}')