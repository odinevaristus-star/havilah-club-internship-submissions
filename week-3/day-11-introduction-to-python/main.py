# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.


# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

student_name = "Alex"      
age = 20                   
gpa = 3.85                 
is_enrolled = True       

print("--- Exercise 1: Variables and Data Types ---")
print("Student Name (String):", student_name)
print("Age (Integer):", age)
print("GPA (Float):", gpa)
print("Is Enrolled (Boolean):", is_enrolled)
print()


# ── Exercise 2: Basic Arithmetic ─────────────────────────────────────────────
# Ask the user to enter two numbers and display sum, difference, product, quotient, and remainder.

print("--- Exercise 2: Basic Arithmetic ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1} + {num2} = {num1 + num2}")
print(f"Difference: {num1} - {num2} = {num1 - num2}")
print(f"Product: {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Quotient: {num1} / {num2} = {num1 / num2}")
    print(f"Remainder: {num1} % {num2} = {num1 % num2}")
else:
    print("Quotient & Remainder: Cannot divide by zero")
print()


# ── Exercise 3: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

print("--- Exercise 3: Temperature Converter ---")
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_equivalent = (celsius_input * 9/5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_equivalent:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_equivalent = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F is equal to {celsius_equivalent:.2f}°C")
print()


# ── Exercise 4: Robot Sensor Monitor ─────────────────────────────────────────
# Ask for Robot Name, ID, Sensor Name, Reading, and Operating Limit. Calculate difference.

print("--- Exercise 4: Robot Sensor Monitor ---")
robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

difference = operating_limit - sensor_reading

print(f"\n--- Robot Sensor Report ---")
print(f"Robot Name: {robot_name} (ID: {robot_id})")
print(f"Sensor: {sensor_name} | Reading: {sensor_reading} | Limit: {operating_limit}")
print(f"Margin / Difference: {difference}")
print()