import unittest


def sum_all_numbers(input_list):
    result = 0
    for index in range(0,len(input_list)):
        result += input_list[index]
    return result


def obtain_average(input_list):
    total = 0
    for index in range(0,len(input_list)):
        total += input_list[index]
    average = total / len(input_list)
    return average

def convert_celsius_to_farenheit(input_value):
    result = (input_value * 1.8) +32
    return result


class TestNumbersMethods(unittest.TestCase):
    
    def test_sum_with_positive_numbers(self):
        input_list = [1,4,5,8,9,6,8,5,5,6]

        result = sum_all_numbers(input_list)
        self.assertEqual(result,57)

    def test_obtain_average_with_negative_numbers(self):
        input_list = [-1,-4,-5,-8,-9,-6,-8,-5,-5,-6]

        result = obtain_average(input_list)
        self.assertEqual(result,-5.7)

    def test_convert_celsius_to_fahrenheit(self):
        # Arrange
        input_value= 33
        # Act 
        result = convert_celsius_to_farenheit(input_value)
        #Assert
        assert result == 91.4


if __name__ == '__main__':
    unittest.main()


