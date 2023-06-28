class Materia:
    def __init__(self,id,title):
        self.id = id
        self.title = title
    
    def __str__(self):
        return f'id = {self.id} titulo = {self.title}'