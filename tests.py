import unittest

from roman_to_arabic_cls import ArabicToRoman

class TestArabicToRoman(unittest.TestCase):
    def test_convert_arabic_to_roman(self):
        ar2rom = ArabicToRoman()
        roman_figure = ar2rom.arabic_to_roman(555)

        self.assertEqual(roman_figure, 'DLV')