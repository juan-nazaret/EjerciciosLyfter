from Python.Funciones import Ejercicios_de_funciones


def test_string_backwards_with_short_string():
    # Arrange
    input_word = 'Hola Mundo'

    # Action
    result = Ejercicios_de_funciones.string_backwards(input_word)

    # Assert 
    assert result == 'odnuM aloH'


def test_string_backwards_with_long_string():
    # Arrange
    input_word = 'Python es un lenguaje de programacion versatil y potente utilizado en desarrollo web, ciencia de datos y automatizado.'

    # Action
    result = Ejercicios_de_funciones.string_backwards(input_word)

    # Assert 
    assert result == '.odazitamotua y sotad ed aicneic ,bew ollorrased ne odazilitu etnetop y litasrev noicamargorp ed ejaugnel nu se nohtyP'


def test_string_backwards_with_only_one_character_string():
    # Arrange
    input_word = 'a'

    # Action
    result = Ejercicios_de_funciones.string_backwards(input_word)

    # Assert 
    assert result == 'a'


