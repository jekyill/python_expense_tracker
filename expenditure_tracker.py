import sys
import expenditure_functions

def main():
    name = input("What is your name?: ")
    options = ("1. Log an expense", "2. Display Summary", "3. Exit Program")

    print(f"Welcome {name} to the expenditure tracker!")
    
    while True:
        for option in options:
            print(option)
        
        user_choice = input("Please enter the number of what you would like to do: ").strip()

        if user_choice == "1":
            expenditure_functions.log_expense()
        elif user_choice == "2":
            expenditure_functions.view_expenditure_list()
        elif user_choice == "3":
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

