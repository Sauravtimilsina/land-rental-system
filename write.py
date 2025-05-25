
LAND_FILE = "lands.txt"

# write land details
def write_lands_data(lands):
    with open(LAND_FILE, "w") as file:
        for land in lands:
            file.write(', '.join([
                land['Kitta'],
                land['Location'],
                land['Direction'],
                land['Area (annas)'],
                land['Price (per month)'],
                land['Status']
            ]) + '\n')