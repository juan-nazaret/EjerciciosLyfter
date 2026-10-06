import actions.add_new_student.new_student_utilities


#Agregar una nueva nota de ingles
def add_new_english_note():
    english_note = actions.add_new_student.new_student_utilities.obtain_note('english')
    return english_note