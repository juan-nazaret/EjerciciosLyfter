from Python.Funciones import Ejercicios_de_funciones

def test_list_sum_with_short_list():
    # Arrange
    input_list = [5,6,2,3]

    # Action
    result = Ejercicios_de_funciones.list_sum(input_list)

    # Assert
    assert result == 16



def test_list_sum_with_long_list():
    # Arrange
    input_list = [
    41, 8, 2, 48, 18, 16, 15, 9, 48, 7, 44, 48, 35, 6, 38, 28, 3, 2, 6, 14,
    15, 33, 39, 2, 36, 13, 46, 42, 45, 35, 27, 15, 29, 38, 18, 1, 49, 11, 45, 28,
    22, 18, 10, 14, 49, 22, 7, 6, 25, 7, 23, 23, 39, 17, 3, 47, 30, 35, 8, 25,
    6, 36, 19, 41, 40, 24, 37, 13, 46, 5, 3, 43, 15, 50, 19, 6, 15, 7, 25, 18,
    30, 41, 24, 11, 24, 23, 14, 43, 18, 45, 44, 42, 5, 39, 41, 11, 35, 47, 16, 11,
    30, 25, 18, 41, 45, 36, 15, 44, 21, 50, 50, 4, 15, 3, 21, 26
    ]

    # Action
    result = Ejercicios_de_funciones.list_sum(input_list)

    # Assert
    assert result == 2909


def test_list_sum_with_only_one_element_in_list():
    # Arrange
    input_list = [5]

    # Action
    result = Ejercicios_de_funciones.list_sum(input_list)

    # Assert
    assert result == 5
