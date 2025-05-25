LANDS_FILE_PATH = "lands.txt"

# reading details of land
def reading_lands():
    lands = []
    with open(LANDS_FILE_PATH, "r") as file:
        for line in file:
            parts = line.replace('\n','').split(', ')
            lands.append({
                'Kitta': parts[0],
                'Location': parts[1],
                'Direction': parts[2],
                'Area (annas)': parts[3],
                'Price (per month)': parts[4],
                'Status': parts[5]
            })

    return lands