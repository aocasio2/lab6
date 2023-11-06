#alvin ocasio jr
#11/5/2023
#problem 1
import random

for _ in range(10):
    random_int = random.randrange(25, 36)
    print(random_int)

#problem 2
import random

odd_integer = random.randrange(1, 100, 2)
print(odd_integer)
#problem 3
import random
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = random.choice(days_of_week)
print(day_of_week)
#problme 4
import math
def approximate_pi():
  pi = 4
  for i in range(3, 100, 2):
    pi += (-1)**(i - 1) / i
  return pi
approximate_pi = approximate_pi()
print(approximate_pi)
print(math.pi)
#problem 5
import math

def convert_radians_to_degrees(radians):
  degrees = radians * 180 / math.pi
  return degrees

user_input = float(input("Enter a value in radians: "))
degrees = convert_radians_to_degrees(user_input)
print("The conversion to degrees is:", degrees)
print("The calculated value using the degrees function in the math module is:", math.degrees(user_input))
#problem 6
import math

def calculate_factorial(n):
  factorial = 1
  for i in range(1, n + 1):
    factorial *= i
  return factorial

user_input = int(input("Enter a value to calculate the factorial of: "))
factorial = calculate_factorial(user_input)
print("The factorial of", user_input, "is:", factorial)
print("The calculated value using the factorial function in the math module is:", math.factorial(user_input))



