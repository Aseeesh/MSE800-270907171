
def _get_positive_float(prompt: str) -> float:
        """Prompts until the user enters a valid positive number."""
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                return value
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

class BMICalculator:
    """Handles data input, validation, and BMI calculation."""

    def __init__(self):
        self.weight_kg: float = 0.0
        self.height_m: float = 0.0

    def get_data(self) -> None:
        """Collects weight in kg and height in cm, converting height to meters."""
        self.weight_kg = _get_positive_float("Please enter your weight in kilograms: ")
        height_cm = _get_positive_float("Please enter your height in centimetres: ")
        self.height_m = height_cm / 100.0

    def calculate(self) -> float:
        """Calculates and returns the BMI rounded to two decimal places."""
        try:
            bmi = self.weight_kg / (self.height_m ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            print("Error: Height cannot be zero.")
            return 0.0


def main():
    print("\n" + "=" * 42 + "\n")
    print("Hello, let's calculate your BMI.\n")

    calc = BMICalculator()
    calc.get_data()
    bmi = calc.calculate()

    print(f"Your BMI is {bmi}")
    print("\n" + "=" * 42 + "\n")


if __name__ == "__main__":
    main()