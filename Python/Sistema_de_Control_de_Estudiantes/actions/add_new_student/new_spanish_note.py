import actions.add_new_student.new_student_utilities

#Agregamos la nota de español
def add_spanish_note():
    spanish_note = actions.add_new_student.new_student_utilities.obtain_note('spanish')
    return spanish_note