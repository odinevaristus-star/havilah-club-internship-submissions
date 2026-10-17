# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: your code here

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

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: your code here

print("--- Exercise 2: Temperature Converter ---")
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_equivalent = (celsius_input * 9/5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_equivalent:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_equivalent = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F is equal to {celsius_equivalent:.2f}°C")
print()

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: your code here
print("--- Exercise 3: Age Calculator ---")
CURRENT_YEAR = 2026

user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_age = CURRENT_YEAR - birth_year
year_turns_30 = birth_year + 30

print(f"\nHello, {user_name}! You are currently {current_age} years old.")
print(f"You will turn 30 years old in the year {year_turns_30}.")