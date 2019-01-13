from roman_to_arabic_cls import ArabicToRoman

number_input = input("Please enter a number to convert to roman figure: ")

try:
    int_number_input = int(number_input)
    ar2rom = ArabicToRoman()

    print(f"The Roman Numeral Equivalent of {int_number_input} is {ar2rom.arabic_to_roman(int_number_input)}")
except ValueError:
   print("Your entry is not an integer, please try again")
