class BMICalulator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return bmi

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
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
        calculator = BMICalulator(weight=weight, height=height)
        bmi_value = calculator.calculate_bmi()
        bmi_category = calculator.get_bmi_category()
        print(f"BMI: {bmi_value:.2f}, Category: {bmi_category}")
        
except ZeroDivisionError:
    print("Error: Height cannot be zero.")