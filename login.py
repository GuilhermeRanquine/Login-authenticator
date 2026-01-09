import csv

def login():
    print("--- Login ---")
    email_input = input("Email: ")
    password_input = input("Password: ")
    
    try:
        with open('accounts.csv', "r", encoding='utf-8') as file:
            leitor = csv.reader(file)
            for linha in leitor:
                if len(linha) >= 6:
                    email_csv = linha[4]
                    senha_csv = linha[5]
                    
                    if email_input == email_csv and password_input == senha_csv:
                        print(f"Login successful. Welcome back, {linha[0]}!")
                        return True
        print("Login failed! Please check your credentials.")
        return False
    except FileNotFoundError:
        print("No accounts found. Please create an account first.")
        return False