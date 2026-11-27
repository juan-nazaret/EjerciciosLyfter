from Python.Funciones import Ejercicios_de_funciones

def test_is_it_prime_number_with_a_short_list():
    # Arrange
    input_list = [5,9,3,6,7]

    #Act
    result = Ejercicios_de_funciones.is_it_prime_number(input_list)

    #Assert
    assert result == [5,3,7]


def test_is_it_prime_number_with_a_long_list():
    # Arrange
    input_list = [164, 29, 7, 190, 71, 63, 58, 36, 189, 27, 174, 190, 140, 23, 152, 109, 9, 8, 24, 56, 
    60, 130, 155, 7, 144, 51, 184, 167, 180, 140, 108, 57, 115, 151, 72, 2, 195, 41, 179, 109, 
    88, 72, 40, 56, 196, 87, 27, 24, 98, 25, 92, 89, 155, 68, 12, 187, 118, 138, 32, 97, 
    21, 142, 76, 161, 159, 93, 148, 50, 181, 18, 12, 170, 59, 198, 75, 21, 60, 26, 98, 72, 
    117, 163, 94, 42, 95, 91, 54, 172, 69, 180, 175, 166, 19, 156, 163, 44, 137, 187, 63, 42, 
    119, 98, 70, 164, 177, 143, 57, 176, 84, 197, 199, 15, 59, 9, 81, 103, 69, 17, 55, 146, 
    184, 81, 55, 168, 128, 102, 165, 118, 37, 68, 36, 64, 191, 144]

    #Act
    result = Ejercicios_de_funciones.is_it_prime_number(input_list)

    #Assert
    assert result == [ 29, 7, 71, 23, 109, 7, 167, 151, 2, 41, 179, 109, 89, 97, 
    181, 59, 163, 19, 163, 137, 197, 199, 59, 103, 17, 37, 191]

def test_is_it_prime_number_with_only_one_number_list():
    # Arrange
    input_list = [164]

    #Act
    result = Ejercicios_de_funciones.is_it_prime_number(input_list)

    #Assert
    assert result == []

