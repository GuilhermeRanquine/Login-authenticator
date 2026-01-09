import csv

def create_account():
    print("--- Create Account ---")
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    password = input("Password: ")
    
    with open('accounts.csv', "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, age, cpf, email, password])