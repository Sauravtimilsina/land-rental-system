from datetime import datetime
from write import write_lands_data

LAND_FILE = "lands.txt"
INVOICE_FILE = "./invoices/"

# Function to display land
def display_lands(lands, available=True):
    status = "Available" if available else "Not Available"
    filtered_lands = [land for land in lands if land['Status'] == status]
    
    print("\n" + status + " Lands:")
    print("Kitta\tLocation\tDirection\tArea(annas)\tPrice (per month)\tStatus")
    print("\n")    
    for land in filtered_lands:
        print(land['Kitta'] + "\t" + land['Location'] + "\t" + land['Direction'] + "\t" + land['Area (annas)'] + "\t" + land['Price (per month)'] + "\t" + land['Status'])


# Function to renting process of land
def rent_land(lands):
    renting = True
    total_amount = 0
    rentals = []
    customer_name = input("Enter your name: ")
    
    while renting:
        display_lands(lands)
        print()
        kitta = input("Enter the kitta number: ")
        try:
            duration = int(input("Enter the duration of the rent in months: "))
            found = False
            for land in lands:
                if land['Kitta'] == kitta and land['Status'] == "Available":
                    land['Status'] = "Not Available"
                    cost = int(land['Price (per month)']) * duration
                    total_amount += cost
                    rentals.append({
                        'Kitta': land['Kitta'],
                        'Location': land['Location'],
                        'Direction': land['Direction'],
                        'Area (annas)': land['Area (annas)'],
                        'Duration': duration,
                        'Cost': cost
                    })
                    found = True
                    break
            if not found:
                print("Land is not available or kitta number is invalid.")
        except ValueError:
            print("Invalid. Please enter a valid number for the duration.")
        print()
        more = input("Do you want to rent more lands? (yes/no): ").lower()
        print()
        if more != 'yes':
            renting = False

    if rentals:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gen_rent_invoice(customer_name, date_now, rentals, total_amount)
        write_lands_data(lands)
        print("All selected lands have been successfully rented.")
    else:
        print("No lands were rented.")


# Function to return land
def return_land(lands):
    returning = True
    total_fine = 0
    returns = []
    customer_name = input("Enter your name: ")

    while returning:
        display_lands(lands, available=False)
        kitta = input("Enter the kitta number of the land to return: ")
        try:
            actual_duration = int(input("Enter the actual duration of the rent in months: "))
            contract_duration = int(input("Enter the contract duration in months: "))
            found = False
            for land in lands:
                if land['Kitta'] == kitta and land['Status'] == "Not Available":
                    land['Status'] = "Available"
                    cost = int(land['Price (per month)']) * contract_duration
                    fine = (actual_duration - contract_duration) * int(land['Price (per month)']) * 1.5 if actual_duration > contract_duration else 0
                    total_fine += fine
                    returns.append({
                        'Kitta': land['Kitta'],
                        'Location': land['Location'],
                        'Direction': land['Direction'],
                        'Area (annas)': land['Area (annas)'],
                        'Actual Duration': actual_duration,
                        'Contract Duration': contract_duration,
                        'Cost': cost,
                        'Fine': fine
                    })
                    found = True
                    break
            if not found:
                print("Invalid kitta number or land is not currently rented.")
        except ValueError:
            print("Invalid input. Please enter a valid number for durations.")

        more = input("Do you want to return more lands? (yes/no): ").lower()
        if more != 'yes':
            returning = False

    if returns:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gen_return_invoice(customer_name, date_now, returns, total_fine)
        write_lands_data(lands)
        print("All selected lands have been successfully returned.")
    else:
        print("No lands were returned.")


# Function to generate invoice details of return
def gen_return_invoice(customer_name, date_now, returns, total_fine):
    filename = INVOICE_FILE + customer_name.replace(' ', '_') + "_" + date_now.replace(':', '-') + ".txt"
    with open(filename, "w") as invoive_gen_file:
        invoive_gen_file.write("Land&Sand Return Invoice\n")
        invoive_gen_file.write("\n")
        invoive_gen_file.write("Date/Time: " + date_now + "\n")
        invoive_gen_file.write("Customer Name: " + customer_name + "\n")
        invoive_gen_file.write("Returns:\n")
        for return_detail in returns:
            for key, value in return_detail.items():
                if key != "Cost":
                    invoive_gen_file.write(key + ": " + str(value) + "\n")
            invoive_gen_file.write("\n")
        invoive_gen_file.write("Total Fine: Rs " + str(total_fine) + "\n")
    print("Invoice file:" + filename)


# Function to generate details of rent invoice
def gen_rent_invoice(customer_name, date_now, rentals, total_amount):
    filename = INVOICE_FILE + customer_name.replace(' ', '_') + "_" + date_now.replace(':', '-') + ".txt"
    with open(filename, "w") as invoive_gen_file:
        invoive_gen_file.write("Land&Sand Rental Invoice\n")
        invoive_gen_file.write("\n")
        invoive_gen_file.write("Date/Time: " + date_now + "\n")
        invoive_gen_file.write("Customer Name: " + customer_name + "\n")
        invoive_gen_file.write("Rentals:\n")
        for rental in rentals:
            for key, value in rental.items():
                if key != "Cost":
                    invoive_gen_file.write(key + ": " + str(value) + "\n")
            invoive_gen_file.write("\n")
        invoive_gen_file.write("Total Amount: Rs " + str(total_amount) + "\n")
    print("Invoice file:" + filename)
