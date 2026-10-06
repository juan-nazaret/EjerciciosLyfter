import re
import actions.actions_utilities.actions_utilities


#función que agregará la sección del estudiante
def add_new_section():
    section = actions.actions_utilities.actions_utilities.add_new_section()
    return section