from create_account import create_account
from login import login
import sys

def menu():
    while True:
        print("\n=== Authenticator Bank ===")
        print("[1] Create Account")
        print("[2] Login")
        print("[3] Exit")
        
        option = input("Choose an option: ")
        
        if option == '1':
            create_account()
            print(f"Account created successfully!")
            print("What would you like to do now?")
            print("[1] Login now")
            print("[2] Return to Main Menu")
            print("[3] Exit")
            
            after_register = input("Option: ")
            if after_register == '1':
                login()
            elif after_register == '3':
                print("Thank you for using Authenticator Bank. Goodbye!")
                break
        elif option == '2':
            login()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    menu()