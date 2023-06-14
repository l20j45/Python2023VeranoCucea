class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property    
    def age(self):
        return f'{self._age} anios' 
    
    @age.setter
    def age(self, age):
        self._age = age 
        
    def saludo(self):
        print(f'hola mi nombre es {self._name} y mi edad es {self._age}')
    
    def __str__(self):
        return f'hola mi nombre es {self._name} y mi edad es {self._age}'
    
p1 = Person("daniel", 29)
print(f'esto es p1 {p1}')
p1.saludo()
