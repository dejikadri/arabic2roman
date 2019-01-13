import collections

class ArabicToRoman(object):
    def arabic_to_roman(self, int_number):
        numerals_ordered_dict = collections.OrderedDict()
        numerals_ordered_dict[1000] = 'M'
        numerals_ordered_dict[900] = 'CM'
        numerals_ordered_dict[500] = 'D'
        numerals_ordered_dict[400] = 'CD'
        numerals_ordered_dict[100] = 'C'
        numerals_ordered_dict[90] = 'XC'
        numerals_ordered_dict[50] = 'L'
        numerals_ordered_dict[40] = 'XL'
        numerals_ordered_dict[10] = 'X'
        numerals_ordered_dict[9] = 'IX'
        numerals_ordered_dict[5] = 'V'
        numerals_ordered_dict[4] = 'IV'
        numerals_ordered_dict[1] = 'I'

        roman_numeral = ""
        for key_arabic, value_roman in numerals_ordered_dict.items():
            while int_number >= key_arabic:
                roman_numeral += value_roman
                int_number -= key_arabic
        return roman_numeral


