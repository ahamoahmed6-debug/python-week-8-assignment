import random

def run_number_game():
    """
    Tool 1: Number Guessing Game
    Uses loops and conditionals to validate inputs and track guesses.
    """
    print("\n--- Welcome to the Number Guessing Game! ---")
    secret_number = random.randint(1, 20)
    attempts = 0
    
    while True:
        user_input = input("Guess a number between 1 and 20: ").strip()
        
        if not user_input.isdigit():
            print("❌ Invalid input! Please enter a whole number.")
            continue
            
        guess = int(user_input)
        attempts += 1
        
        if guess < secret_number:
            print(f"📈 {guess} is too low. Try again!")
        elif guess > secret_number:
            print(f"📉 {guess} is too high. Try again!")
        else:
            print(f"🎉 Correct! You guessed the number {secret_number} in {attempts} attempts.")
            break

def run_task_tracker():
    """
    Tool 2: Task Tracker (To-Do List)
    Uses a dynamic list that changes while the program runs.
    """
    print("\n--- Welcome to the Task Tracker! ---")
    tasks = []
    
    while True:
        print(f"\nCurrent Tasks ({len(tasks)} items total):")
        if not tasks:
            print("  (No pending tasks)")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task}")
                
        print("\nOptions: [1] Add Task | [2] Clear All | [3] Return to Main Menu")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            new_task = input("Enter your task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"✅ Added task: \"{new_task}\"")
            else:
                print("⚠️ Task description cannot be empty.")
        elif choice == "2":
            tasks.clear()
            print("🗑️ All tasks have been cleared.")
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")

def run_name_formatter():
    """
    Tool 3: Name Formatter Pro
    Uses conditionals and string analysis.
    """
    print("\n--- Welcome to Name Formatter Pro! ---")
    first = input("Enter your first name: ").strip()
    last = input("Enter your last name: ").strip()
    
    if not first or not last:
        print("⚠️ Formatting error: First and last names cannot be blank.")
    else:
        clean_first = first.capitalize()
        clean_last = last.capitalize()
        full_name = f"{clean_first} {clean_last}"
        total_letters = len(clean_first) + len(clean_last)
        
        print(f"\n✨ Formatted Full Name: {full_name}")
        print(f"📊 Total letters in your name: {total_letters}")
        
        if total_letters > 12:
            print("💡 Notice: That is a relatively long name!")
        else:
            print("💡 Notice: Your name is short and punchy!")


# ==================== MAIN PROGRAM LOOP ====================
if __name__ == "__main__":
    print("=========================================")
    print("👋 Welcome to your PLP Python")
    print("   Utility Toolkit!")
    print("=========================================")
    
    while True:
        print("\n--- PYTHON COGNITIVE TOOLKIT ---")
        print("1. Play Number Guessing Game")
        print("2. Open Task Tracker (To-Do List)")
        print("3. Run Name Formatter Pro")
        print("4. Quit Program")
        print("---------------------------------")
        
        menu_choice = input("Enter your choice (1-4): ").strip()
        
        if menu_choice == "1":
            run_number_game()
        elif menu_choice == "2":
            run_task_tracker()
        elif menu_choice == "3":
            run_name_formatter()
        elif menu_choice == "4":
            print("\n=========================================")
            print("🚀 Thank you for utilizing the Toolkit. Goodbye!")
            print("=========================================")
            break
        else:
            print("⚠️ Please enter a valid menu number (1, 2, 3, or 4).")
