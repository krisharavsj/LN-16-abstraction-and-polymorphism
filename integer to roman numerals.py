
class IntToRoman:
    def __init__(self, num: int):
        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")
        if num <= 0 or num >= 4000:
            raise ValueError("Enter a number between 1 and 3999.")
        self.num = num
        self.roman = self._convert()

    def _convert(self) -> str:
        lookup = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
        ]
        result = ''
        n = self.num
        for value, symbol in lookup:
            count, n = divmod(n, value)
            result += symbol * count
        return result

    def __str__(self):
        return f"{self.num} → {self.roman}"

# Example usage:
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer (1–3999): ").strip())
        converter = IntToRoman(user_input)
        print(converter)  # e.g., "1994 → MCMXCIV"
    except (ValueError, TypeError) as e:
        print("Error:", e)
