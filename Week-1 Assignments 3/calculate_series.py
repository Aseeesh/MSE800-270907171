class SeriesCalculator:

  def calculate_fibonacci(self, n: int):
    print(f"Generates a Fibonacci series up to {n} terms.\n output result below \n")
    if n <= 0:
      return []
    elif n == 1:
      return [0]
    series = [0, 1]
    while len(series) < n:
      next_term = series[-1] + series[-2]
      series.append(next_term)
    return series

  def calculate_factorial(self, n: int):
    print(f"Calculates factorial using a basic loop.\n output result below \n")
    if n < 0:
      return "Error: Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
      return 1
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result


calculator = SeriesCalculator()
try:
  user_input = int(input("Enter a positive integer: "))
  fib_output = calculator.calculate_fibonacci(user_input)
  print(f"The fibonacci of {user_input} is: {fib_output}")

  fact_output = calculator.calculate_factorial(user_input)
  print(f"The factorial of {user_input} is: {fact_output}")
except ValueError:
  print("Error: Please enter a valid whole number.")
