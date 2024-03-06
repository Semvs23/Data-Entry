import csv
import re

def validate_input(prompt, regex_pattern):
    while True:
        user_input = input(prompt)
        if re.match(regex_pattern, user_input):
            return user_input
        else:
            print("Ongeldige invoer. Probeer opnieuw.")

def main():
    print("Welkom bij het urenregistratiesysteem.") #welkomsbericht staat op het begin

    name = input("Naam werknemer: ") #input voor je naam

    date_pattern = re.compile("^\d{8}$") #alleen cijfers
    date = validate_input("Datum (YYYYMMDD): ", date_pattern) #input voor datum

    hours_pattern = re.compile("^\d+$") #alleen cijfers 
    hours_worked = validate_input("Aantal gewerkte uren: ", hours_pattern) # input voor je aantal gewerkte uren

    project_number = input("Projectnummer: ") #input voor je projectnummer

    data = {
        "Naam": name,
        "Datum": date,
        "Gewerkte Uren": hours_worked,
        "Projectnummer": project_number
    }

    csv_file = 'urenregistratie.csv'
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Als het bestand leeg is, schrijf de header
        if file.tell() == 0:
            writer.writeheader()

        # Schrijf de gegevens naar het CSV-bestand
        writer.writerow(data)

    print(f"Urenregistratie succesvol opgeslagen in {csv_file}.")

if __name__ == "__main__":
    main()
