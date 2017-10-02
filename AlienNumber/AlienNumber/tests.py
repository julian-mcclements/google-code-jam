import unittest
from alien import AlienNumberConverter, AlienNumberTestCase

# See http://stackoverflow.com/questions/644821/python-how-to-run-unittest-main-for-all-source-files-in-a-subdirectory on 
# how to run python unit tests from the command line.

# Always prefix test methods with "test".

class TestAlienNumberConverter(unittest.TestCase):
    '''
    Test fixture for the AlienNumberConvertor class.
    '''

    def test_convert_number_to_target_language(self):

        test_cases = []
        test_cases.append((AlienNumberTestCase("100010010111100001", "01", "01234567"), "422741"))
        test_cases.append((AlienNumberTestCase("225E1", "0123456789ABCDEF", "0123456"), "1124256"))
        test_cases.append((AlienNumberTestCase("3003413", "012345", "012"), "21011002200"))
        test_cases.append((AlienNumberTestCase("140769", "0123456789", "0123456789ABCDEFGHJK"), "HBJ9"))
        test_cases.append((AlienNumberTestCase("9", "0123456789", "012"), "100"))
        test_cases.append((AlienNumberTestCase("9", "0123456789", "oF8"), "Foo"))
        test_cases.append((AlienNumberTestCase("Foo", "oF8", "0123456789"), "9"))
        test_cases.append((AlienNumberTestCase("13", "0123456789abcdef", "01"), "10011"))
        test_cases.append((AlienNumberTestCase("CODE", "O!CDE?", "A?JM!."), "JAM!"))

        converter = AlienNumberConverter()

        for (test_case, expected) in test_cases:
            self.assertEqual(converter.convert(test_case), expected)

if __name__ == '__main__':
    unittest.main()
