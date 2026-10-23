# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    while True:
        user_input = input("Enter a number for the multiplication table (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        try:
            num = float(user_input)
            print(f"\n--- Multiplication Table for {num} ---")
            for i in range(1, 13):
                result = num * i
                if num.is_integer():
                    print(f"{int(num)} x {i} = {int(result)}")
                else:
                    print(f"{num} x {i} = {result}")
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number or 'quit'.\n")


# ── Function 3: Your Choice (Temperature Converter) ───────────────────────────
# Receives a temperature in Celsius as a parameter, converts it to Fahrenheit, and returns the result.

def convert_temperature(celsius):
    return (celsius * 9 / 5) + 32


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("=== Python Utility Menu ===")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter (Celsius to Fahrenheit)")
        print("4. Exit")
        
        choice_input = input("Select an option (1-4): ")
        
        if choice_input == '4':
            print("Exiting program. Goodbye!")
            break
            
        try:
            choice = int(choice_input)
            
            if choice == 1:
                print("\n--- Grade Calculator ---")
                score_input = float(input("Enter student score (0-100): "))
                if 0 <= score_input <= 100:
                    grade = calculate_grade(score_input)
                    print(f"The grade for score {score_input} is: {grade}\n")
                else:
                    print("Please enter a score between 0 and 100.\n")
                    
            elif choice == 2:
                multiplication_table()
                
            elif choice == 3:
                print("\n--- Temperature Converter ---")
                celsius_val = float(input("Enter temperature in Celsius: "))
                fahr_val = convert_temperature(celsius_val)
                print(f"{celsius_val}°C is equal to {fahr_val:.2f}°F\n")
                
            else:
                print("Invalid option choice. Please choose between 1 and 4.\n")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


if __name__ == "__main__":
    main()