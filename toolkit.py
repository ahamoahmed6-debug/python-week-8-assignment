# ==================== MAIN PROGRAM LOOP ====================
if __name__ == "__main__":
    print("=========================================")
    print("👋 Welcome to your PLP Python Utility Toolkit!")
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
