class AlienNumberTestCase:
    """Represents a single alien number conversion test case"""

    def __init__(self, alien_number, source_language, target_language):
        self.__alien_number = alien_number
        self.__source_language = source_language
        self.__target_language = target_language

    @property
    def alien_number(self):
        return self.__alien_number

    @property
    def source_language(self):
        return self.__source_language

    @property
    def target_language(self):
        return self.__target_language

    def __str__(self):
        return "{{ alien_number: {0}, source_language: {1}, target_language: {2} }}".format(
            self.alien_number, self.source_language, self.target_language)

class AlienNumberConverter:

    def __init__(self):
        pass

    def convert(self, testcase):

        # Get radix for source language
        src_radix = len(testcase.source_language)

        # Map source language digits to matching decimal numbers
        src_digit_value_map = {src_digit : index for index, src_digit in enumerate(list(testcase.source_language))}

        # Convert alien number to decimal number
        decimal_value = 0
        max_src_radix_power = len(testcase.alien_number) - 1
        for index, digit in enumerate(list(testcase.alien_number)):
            decimal_value += (src_radix ** (max_src_radix_power - index)) * src_digit_value_map[digit]

        # Get radix for target language
        target_radix = len(testcase.target_language)

        # Conversion of the decimal value to the target radix is a two-step process. The first step is
        # repeatedly divide the decimal value by the target radix. The remainder of each division is 
        # appended to a list. 
        remainders = []
        dividend = decimal_value
        while dividend >= target_radix:
            remainders.append(dividend % target_radix)
            dividend = dividend // target_radix
        remainders.append(dividend)

        # Map target language digits onto matching decimal values
        target_value_digit_map = {index : target_digit  for index, target_digit in enumerate(list(testcase.target_language))}

        # In the second stage the list of remainders is reversed and iterated over. The value of each 
        # item is mapped to the digit in the target language.
        target_number = "".join([ target_value_digit_map[converted] for converted in reversed(remainders)])
        
        return target_number
