# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels and their data types.

print("=== Exercise 1: Variables and Data Types ===")
student_name = "Raphael"  # String
student_age = 20          # Integer
student_gpa = 4.75        # Float
is_enrolled = True        # Boolean

print(f"Name: {student_name} (Type: {type(student_name)})")
print(f"Age: {student_age} (Type: {type(student_age)})")
print(f"GPA: {student_gpa} (Type: {type(student_gpa)})")
print(f"Enrolled: {is_enrolled} (Type: {type(is_enrolled)})")
print()


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

print("=== Exercise 2: Temperature Converter ===")
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_result = (celsius_input * 9 / 5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_result:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_result = (fahrenheit_input - 32) * 5 / 9
print(f"{fahrenheit_input}°F is equal to {celsius_result:.2f}°C")
print()


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

print("=== Exercise 3: Age Calculator ===")
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year (e.g., 2005): "))

current_year = 2026
current_age = current_year - birth_year
year_turning_30 = birth_year + 30

print(f"Hello, {user_name}! You are currently {current_age} years old.")
print(f"You will turn 30 in the year {year_turning_30}.")