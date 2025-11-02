from sum_digits import sum_digits
from data_file_extraction import data_file_extraction
from password_validator import password_validator
from remove_duplicates import remove_duplicates
from translation_log_calculator import translation_log_calculator

def mostrar_menu():
    print("\n")
    print("=== MENÚ PRINCIPAL ===")
    print("1. Sum digits")
    print("2. Password Validator")
    print("3. Remove duplicates from a list")
    print("4. Data file extraction")
    print("5. Translation log calculator")
    print("0. Salir")
    print("\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Choose an option: ")

        if opcion == "1":
            sum_digits.execute()
        elif opcion == "2":
            password_validator.execute()
        elif opcion == "3":
            remove_duplicates.execute()
        elif opcion == "4":
            data_file_extraction.execute()
        elif opcion == "5":
            translation_log_calculator.execute()         
        elif opcion == "0":
            print("See you soon!")
            break
        else:
            print("Incorrect option. Try again.\n")

if __name__ == "__main__":
    main()