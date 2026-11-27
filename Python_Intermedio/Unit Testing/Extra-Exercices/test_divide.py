import unittest

def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


class TestDivideNumbers(unittest.TestCase):

    def test_divide(self):

        #Arrange
        number1 = 10
        number2 = 2

        # Act
        result = divide(number1,number2)

        # Assert
        assert result == 5.0

    def test_divide_by_zero(self):
    
            #Arrange
            number1 = 10
            number2 = 0
    
            # Act and Assert
            self.assertRaises(ValueError)

    def test_divide_by_string(self):
        #Arrange
        number1 = 10
        number2 = 'p'

        # Act and Assert
        self.assertRaises(TypeError)
            
if __name__ == '__main__':
    unittest.main()