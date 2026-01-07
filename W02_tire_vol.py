import math
import os
from datetime import datetime

os.system('cls')

tire_type = []
width = []
aspect_ratio = []
diameter = []
price = []
tire_name = []
width_match = []

with open("C:\Users\geoad\Desktop\SCHOOL\CSE 111\Git\BYU-CSE-Codes\tires.csv") as data_file:
    for index, line in enumerate(data_file):
        if index == 0:
            continue
        parts = line.strip().split(',')
        tire_type.append(parts[0])
        width.append(int(parts[1]))
        aspect_ratio.append(int(parts[2]))
        diameter.append(int(parts[3]))
        price.append(float(parts[4]))
        tire_name.append(parts[5])

general_catalog = list(zip(tire_type, width, aspect_ratio, diameter, price, tire_name))

car_catalog = []
moto_catalog = []
for line in general_catalog:
    vehicle_type = line[0]
    if vehicle_type.lower() == 'car':
        car_catalog.append(line)
    else:
        moto_catalog.append(line)

def calculate_vol():
    today = datetime.now().today()
    user_width = int(input("Enter the tire width in mm (e.g., 205): "))
    user_aspect_ratio = int(input("Enter the tire aspect ratio in % (e.g., 60): "))
    user_diameter = int(input("Enter the wheel diameter in inches (e.g., 15): "))

    user_vol = (math.pi * user_width**2 * user_aspect_ratio * (user_width * user_aspect_ratio + 2540 * user_diameter)) / 10000000000
    print(f"\nThe approximate volume is {user_vol:.2f} liters.\n")

def moto_tire():
    print()
    print("Please enter the following information:")
    print("--------------------------------")

    while True:
        print()
        print("Choose a Tire detail to refine your search.")
        print("1. Width")
        print("2. Aspect Ratio")
        print("3. Diameter")
        print("4. Back to Tire Type")
        print()
        try:
            detail_choice = int(input("Please enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        if detail_choice == 1:
            user_width = int(input("Enter the width of the tire in mm: "))
            if 60 <= user_width <= 40:
                closest_index = find_closest_indices(width, user_width)
                printing_tires (closest_index, moto_catalog)
            else:
                print(f"The width {user_width} mm is out of range. Please enter a width between 40 mm and 60 mm.")
        elif detail_choice == 2:
            user_aspect_ratio = int(input("Enter the aspect ratio fo the tire in %: "))
            if 30 <= user_aspect_ratio <= 90:
                closest_index = find_closest_indices(aspect_ratio, user_aspect_ratio)
                printing_tires (closest_index, moto_catalog)
            else:
                print(f"The aspect ratio {user_aspect_ratio}% is out of range. Please enter an aspect ratio between 30% and 80%.")
        elif detail_choice == 3:
            user_diameter = int(input("Enter the diameter of the tire in inches: "))
            if 10 <= user_diameter <= 21:
                closest_index = find_closest_indices(diameter, user_diameter)
                printing_tires (closest_index, moto_catalog)
            else:
                print(f"The diameter {user_diameter} inches is out of range. Please enter a diameter between 10 inches and 21 inches.")
        elif detail_choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

def car_tire():
    print()
    print("Please enter the following information:")
    print("--------------------------------")

    while True:
        print()
        print("Choose a Tire detail to refine your search.")
        print("1. Width")
        print("2. Aspect Ratio")
        print("3. Diameter")
        print("4. Back to Tire Type")
        print()
        try:
            detail_choice = int(input("Please enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        if detail_choice == 1:
            user_width = int(input("Enter the width of the tire in mm: "))
            if 145 <= user_width <= 355:
                closest_index = find_closest_indices(width, user_width)
                printing_tires (closest_index, car_catalog)
            else:
                print(f"The width {user_width} mm is out of range. Please enter a width between 145 mm and 355 mm.")
        elif detail_choice == 2:
            user_aspect_ratio = int(input("Enter the aspect ratio fo the tire in %: "))
            if 25 <= user_aspect_ratio <= 85:
                closest_index = find_closest_indices(aspect_ratio, user_aspect_ratio)
                printing_tires (closest_index, car_catalog)
            else:
                print(f"The aspect ratio {user_aspect_ratio}% is out of range. Please enter an aspect ratio between 25% and 85%.")
        elif detail_choice == 3:
            user_diameter = int(input("Enter the diameter of the tire in inches: "))
            if 13 <= user_diameter <= 24:
                closest_index = find_closest_indices(diameter, user_diameter)
                printing_tires (closest_index, car_catalog)
            else:
                print(f"The diameter {user_diameter} inches is out of range. Please enter a diameter between 13 inches and 24 inches.")
        elif detail_choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

def find_closest_indices(numbers, target):
    closest_indices = []
    min_diff = float('inf')

    for i, number in enumerate(numbers):
        diff = abs(number - target)
        if diff < min_diff:
            min_diff = diff
            closest_indices = [i]
        elif diff == min_diff:
            closest_indices.append(i)

    return closest_indices

def printing_tires (indices, tire_catalog):
    today = datetime.now().today()
    line_response = 1
    print()
    print("We are confident that these tires will fit your needs: ")
    for i in indices:
        print(f"{line_response}. {tire_catalog[i][0]}, {tire_catalog[i][1]}mm, {tire_catalog[i][2]}%, {tire_catalog[i][3]} in - ${tire_catalog[i][4]:.2f} ({tire_catalog[i][5]})")
        line_response = line_response + 1

        while True:
            print()
            print("Would you like to purchase these tires?")
            print("1. Yes")
            print("2. No and Return to Previous Menu")
            print("3. No and Exit")
            try:
                print()
                choice = int(input("Please enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")
                continue
            if choice == 1:
                os.system('cls')
                car_tire()
            elif choice == 2:
                print("\nReturning to Previous Menu...\n")
                moto_tire()
            elif choice == 3:
                print("\nThank you. Goodbye.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
                continue

def main():
    while True:
        print()
        print("What type of tire are you shopping for?")
        print()
        print("1. Car Tire")
        print("2. Motorcycle Tire")
        print("3. View Choices")
        print("4. Exit")
        try:
            choice = int(input("Please enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        if choice == 1:
            os.system('cls')
            car_tire()
        elif choice == 2:
            os.system('cls')
            moto_tire()
        elif choice == 3:
            os.system('cls')
            calculate_vol()
        elif choice == 4:
            print("\nThank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue