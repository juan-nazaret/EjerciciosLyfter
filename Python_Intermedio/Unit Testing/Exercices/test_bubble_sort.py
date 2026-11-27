from Python_Intermedio.Algoritmos_de_ordenamiento import Exercise1
import pytest

def test_bubble_sort_with_short_list():
    # Arrange
    input_list = [1,5,6,8,9]

    # Act
    result = Exercise1.bubble_sort(input_list)

    # Assert
    assert result == [1,5,6,8,9]


def test_bubble_sort_with_long_list():
    # Arrange
    input_list =[
    10, 85, 96, 115, 93, 31, 94, 88, 97, 110,
    48, 80, 89, 33, 17, 63, 83, 98, 52, 69,
    9, 62, 99, 109, 8, 2, 79, 71, 27, 81,
    22, 53, 42, 51, 67, 40, 68, 35, 61, 39,
    60, 56, 77, 23, 64, 66, 24, 41, 100, 113,
    25, 7, 57, 91, 19, 50, 119, 43, 3, 104,
    73, 74, 37, 47, 38, 11, 75, 16, 59, 6,
    34, 45, 46, 13, 49, 102, 111, 120, 101, 20,
    86, 44, 105, 21, 1, 116, 106, 58, 114, 54,
    108, 90, 84, 92, 26, 72, 103, 78, 65, 30,
    28, 107, 118, 5, 55, 76, 12, 70, 112, 87,
    14, 117, 18, 29, 32, 36, 95, 4, 15, 82
    ]
    # Act
    result = Exercise1.bubble_sort(input_list)

    # Assert
    assert result == [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
    111, 112, 113, 114, 115, 116, 117, 118, 119, 120
    ]


def test_bubble_sort_with_empty_list():
    # Arrange
    input_list = []

    # Act
    result = Exercise1.bubble_sort(input_list)

    # Assert
    assert result == []



def test_bubble_sort_with_error_raised():
    # Arrange
    input_list = [1,5,2,6,9,True]

    # Act and Assert
    with pytest.raises(TypeError)as exe:
        Exercise1.bubble_sort(input_list)


def test_bubble_sort_without_list_param():
    # Arrange
    input_list = 8

    # Act and Assert
    with pytest.raises(TypeError)as exe:
        Exercise1.bubble_sort(input_list)


