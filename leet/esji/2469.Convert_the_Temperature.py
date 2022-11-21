from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin: float = celsius + 273.15
        fahrenheit: float = celsius * 1.80 + 32.0

        return [kelvin, fahrenheit]


if __name__ == "__main__":
    convert_class = Solution()
    convert_class.convertTemperature(celsius=36.50)
