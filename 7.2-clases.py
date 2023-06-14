class person:
    name:str
    age:int
    
    def greetting():
        print(f'hola mi nombre es')
    
person1=person
person1.name='daniel'
person1.age=29

print(person1.name)
person1.greetting()
print(person1.age)

