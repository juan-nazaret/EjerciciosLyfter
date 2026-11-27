from Python.Funciones import Ejercicios_de_funciones

def test_creating_list_words_with_short_string():
    
    # Arrange
    input_string = 'hola-cachorro-perro'

    # Act
    result = Ejercicios_de_funciones.creating_words_list(input_string)

    # Assert
    assert result == 'cachorro-hola-perro' 



def test_creating_list_words_with_long_string():
    
    # Arrange
    input_string = 'sol-luna-gato-arbol-mesa-libro-azul-rojo-casa-perro-nube-rio-flor-tren-mar-estrella-viento-fuego-tierra-agua-cielo-bosque'

    # Act
    result = Ejercicios_de_funciones.creating_words_list(input_string)

    # Assert
    assert result == 'agua-arbol-azul-bosque-casa-cielo-estrella-flor-fuego-gato-libro-luna-mar-mesa-nube-perro-rio-rojo-sol-tierra-tren-viento' 


def test_creating_list_words_with_one_word_string():
    
    # Arrange
    input_string = 'sol'
    # Act
    result = Ejercicios_de_funciones.creating_words_list(input_string)

    # Assert
    assert result == 'sol'