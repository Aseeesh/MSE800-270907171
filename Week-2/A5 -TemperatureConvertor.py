# Bundles the scale unit ('C' or 'F') and numeric value together with the
# mathematical formulas required to perform temperature conversions.
class Temperature:
    def __init__(self, unit: str, value: float):
        self.unit = unit.upper()  # Standardizes unit to uppercase ('C' or 'F')
        self.value = value        # Numeric degree value

    def to_celsius(self) -> float:
        """Converts Fahrenheit degree value to Celsius."""
        return (self.value - 32) * 5 / 9

    def to_fahrenheit(self) -> float:
        """Converts Celsius degree value to Fahrenheit."""
        return (self.value * 9 / 5) + 32


# Hides input parsing, case normalization, and conversion calculations 
# behind a single, clean method call (`process_input`).
class TemperatureConverter:
    def process_input(self, raw_input: str) -> str:
        """Validates raw input string and executes the conversion."""
        text = raw_input.strip()

        if len(text) < 2:
            raise ValueError()

        # Accepts uppercase or lowercase ('c', 'C', 'f', 'F') at start or end of input
        if text[0].upper() in ('C', 'F'):
            unit = text[0].upper()# Index 0 gets the FIRST character -> "F"
            numeric_part = text[1:]      # Slices from Index 1 to end      -> "51"
        elif text[-1].upper() in ('C', 'F'):
            unit = text[-1].upper()
            numeric_part = text[:-1]
        else:
            raise ValueError()

        # Parse numeric degree value (raises ValueError if numeric_part is invalid)
        value = float(numeric_part)

        # OOP CONCEPT: Object Instantiation
        temp = Temperature(unit, value)

        if unit == 'F':
            celsius_val = temp.to_celsius()
            return f"{text} degrees Fahrenheit is converted to {celsius_val:.2f} degrees Celsius"
        else:
            fahrenheit_val = temp.to_fahrenheit()
            return f"{text} degrees Celsius is converted to {fahrenheit_val:.2f} degrees Fahrenheit"


def main():
    converter = TemperatureConverter()

    while True:
        # INNER LOOP: Continues prompting until a valid temperature is entered
        while True:
            user_input = input("\nEnter temperature (e.g., F51 or C11): ").strip()

            # TRY-EXCEPT: Catches formatting and conversion errors
            try:
                result = converter.process_input(user_input)
                print(result)
                break  # Exit inner loop ONLY when conversion succeeds
            except ValueError:
                print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")

        
        choice = input("\nConvert another temperature? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()