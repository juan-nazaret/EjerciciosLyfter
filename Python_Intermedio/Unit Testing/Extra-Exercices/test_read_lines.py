import unittest
from unittest.mock import Mock
from unittest.mock import mock_open,patch



def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

class TestingReadLines(unittest.TestCase):

    def test_reading_lines(self):

        #Arrange
        mocked_file = mock_open(read_data = 'Hola Mundo')

        #Act
        with patch('builtins.open',mocked_file):
            result = read_lines('documento.txt')

        # Assert 
        assert result == ['Hola Mundo']


    def test_read_lines_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            try:
                read_lines("inexistente.txt")
            except FileNotFoundError:
                assert True
            

if __name__ == '__main__':
    unittest.main()