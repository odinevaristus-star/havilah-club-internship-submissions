# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Takes a score (0-100) and returns the letter grade.
# A = 70+, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score (must be between 0 and 100)."
    elif score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

score = int(input("Enter your score (0-100): "))
grade = calculate_grade(score)
print("Your grade is:", grade)


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    while True:
        user_input = input("Enter a number for the table (or type 'quit' to go back): ").strip()
        
        if user_input.lower() == 'quit':
            print("Exiting multiplication table...\n")
            break
            
        try:
            num = float(user_input)
            print(f"\n--- Multiplication Table for {num:g} ---")
            for i in range(1, 13):
                result = num * i
                # Format output cleanly to avoid trailing .0 for whole numbers
                formatted_num = int(num) if num.is_integer() else num
                formatted_res = int(result) if result.is_integer() else result
                print(f"{formatted_num} x {i} = {formatted_res}")
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number or type 'quit'.\n")


# ── Function 3: Your Choice ───────────────────────────────────────────────────
# Define a third function of your choice — e.g. calculate_area(), convert_currency(),
# or check_palindrome().

def check_palindrome():
    text = input("Enter a word, phrase, or number to check: ")
    # Clean the string by keeping only alphanumeric characters and converting to lowercase
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    
    if len(cleaned_text) == 0:
        print("Please enter valid text characters.\n")
        return
        
    if cleaned_text == cleaned_text[::-1]:
        print(f"Success! '{text}' is a palindrome.\n")
    else:
        print(f"'{text}' is not a palindrome.\n")


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input (e.g. text entered instead of a number).

def main():
    while True:
        print("==============================")
        print("      PYTHON UTILITY MENU     ")
        print("==============================")
        print("1. Grade Calculator")
        print("2. Multiplication Table Generator")
        print("3. Palindrome Checker")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            print("\n--- Grade Calculator ---")
            try:
                score_input = float(input("Enter the student's score (0-100): "))
                grade = calculate_grade(score_input)
                print(f"Result: The letter grade is **{grade}**\n")
            except ValueError:
                print("Invalid input! Please enter a numerical score.\n")
                
        elif choice == '2':
            print("\n--- Multiplication Table Generator ---")
            multiplication_table()
            
        elif choice == '3':
            print("\n--- Palindrome Checker ---")
            check_palindrome()
            
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select a valid option between 1 and 4.\n")


if __name__ == "__main__":
    main()
