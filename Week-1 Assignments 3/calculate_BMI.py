class BMICalulator:
    def get_bmi(self, weight, height):
        return weight / (height ** 2)

    def get_bmi_category(self, weight, height):
        bmi = self.get_bmi(weight, height)
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"


try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    if height <= 0:
        print("Error: Height must be greater than zero.")
    elif weight <= 0:
        print("Error: Weight must be greater than zero.")
    else:
        calculator = BMICalulator()
        bmi_value = calculator.get_bmi(weight, height)
        bmi_category = calculator.get_bmi_category(weight, height)
        print(f"BMI: {bmi_value:.2f}, Category: {bmi_category}")
        
except ZeroDivisionError:
    print("Error: Height cannot be zero.")