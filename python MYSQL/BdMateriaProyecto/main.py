import Menu
import MateriaDAO

Menu.menuPrincipal()
opcion = input('Ingresa una opcion')
opcion = 3
if opcion == 1 :
    id = input('ingresa el id')
    title = input('ingresa el title')
    MateriaDAO.altaMateria(id,title)
elif opcion == 2 :
    id = input('ingresa el id')
    MateriaDAO.verMateria(id)
elif opcion == 3 :
    MateriaDAO.verTodasMateria()
elif opcion == 4 :
    id = input('ingresa el id')
    title = input('ingresa el title')
    MateriaDAO.modificarMateria(id,title)
elif opcion == 5 :
    title = input('ingresa el title')
    MateriaDAO.borrarMateria(title)