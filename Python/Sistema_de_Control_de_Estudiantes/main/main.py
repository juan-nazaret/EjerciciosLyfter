#dentro de la carpeta main
import sys
import os
#os.path.dirname nos ayude a subir un nivel en la ruta que tiene python como referencia para encontrar los módulos que estamos insertando
#como quisimos subir dos niveles, pusimos dos veces os.path.dirname
project_path = os.path.dirname(os.path.dirname(__file__))



#inserta a la lista de rutas la nueva referencia que pusimos como ruta de búsqueda para los módulos 
sys.path.insert(0,project_path)

import menu.show_menu

menu.show_menu.show_menu()