class RomanConverter:
    def int_to_roman(self, num):
        roman_numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M" }
        result = ""
        for value in sorted(roman_numerals.keys(), reverse=True):
            while num >= value:
                result += roman_numerals[value]
                num -= value
        return result
num = int(input("Enter a number: "))
converter = RomanConverter()
print("Roman numeral:", converter.int_to_roman(num))