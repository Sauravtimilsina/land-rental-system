from operation import display_lands, rent_land, return_land
from read import reading_lands

def main():
    lands = reading_lands()
    while True:
        print("\nWelcome to the techno property Nepal System")
        print("\n")
        print("1. Display Available Lands")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit")
        choice = input("Choose any one: ")
        if choice == '1':
            display_lands(lands)
        elif choice == '2':
            rent_land(lands)
        elif choice == '3':
            return_land(lands)
        elif choice == '4':
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

main()
