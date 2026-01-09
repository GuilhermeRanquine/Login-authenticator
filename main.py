from create_account import create_account
from login import login

def menu():
    while True:
        print("\n=== Authenticator Bank ===")
        print("[1] Create Account")
        print("[2] Login")
        print("[3] Exit")
        
        option = input("Choose an option: ")
        
        if option == '1':
            create_account()
        elif option == '2':
            login()
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    menu()