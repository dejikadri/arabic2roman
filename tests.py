import unittest

from roman_to_arabic_cls import ArabicToRoman

class TestArabicToRoman(unittest.TestCase):
    def setUp(self):
        self.ar2rom =  ArabicToRoman()

    def test_convert_arabic_to_roman_integer_input(self):

        self.assertEqual(self.ar2rom.arabic_to_roman(555), 'DLV')
        self.assertEqual(self.ar2rom.arabic_to_roman(3400), 'MMMCD')

    def test_convert_arabic_to_roman_non_integer_input(self):
        self.ar2rom.arabic_to_roman(2.4)

        self.assertEqual(self.ar2rom.arabic_to_roman(2.4), 'Invalid Entry')
        self.assertEqual(self.ar2rom.arabic_to_roman(5000), 'Invalid Entry')
        self.assertEqual(self.ar2rom.arabic_to_roman('two'), 'Invalid Entry')
