from Python.Funciones import Ejercicios_de_funciones


def test_upper_lower_cases_with_short_string():
    # Arrange
    input_word = 'Hola Mundo'

    # Action
    cases = Ejercicios_de_funciones.upper_lower_cases(input_word)

    # Assert
    assert cases == (2,7)


def test_upper_lower_cases_with_long_string():
    # Arrange
    input_word = 'Python es un lenguaje de programacion versatil y potente utilizado en desarrollo web, ciencia de datos y automatiz'

    # Action
    cases = Ejercicios_de_funciones.upper_lower_cases(input_word)

    # Assert
    assert cases == (1,95)


def test_upper_lower_cases_with_one_single_character_string():
    # Arrange
    input_word = 'P'

    # Action
    cases = Ejercicios_de_funciones.upper_lower_cases(input_word)

    # Assert
    assert cases == (1,0)