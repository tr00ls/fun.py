# Author: tr00ls
# Description: A script i made as a challenge, that calculates your BMI. It converts Pounds/Kilograms and Feet/Inches/Centimeters, depending on your input.

print("This program lets you calculate your BMI, by entering your height and weight")
error_message = "Something went wrong, please try again"

height_unit = input("Would you like to enter your height in Centimeters, Feet/Inches, or just Inches?: ") .upper().strip()
if height_unit in ("FEET/INCHES", "FEET + INCHES", "FEETINCHES", "FEET AND INCHES", "F", "FEET", "FT"):
    height_feet = int(input("Feet: "))
    height_inches = float(input("Inches: "))
    total_inches = (height_feet * 12) + height_inches
    height_m = total_inches * 0.0254 
elif height_unit in ("CM", "CENTIMETER", "CENTIMETERS", "C"):
    height = float(input("Please enter your height in Centimeters: "))
    height_m = height / 100
elif height_unit in ("INCHES", "INCH", "IN", "''", "I"):
    height = float(input("Please enter your height in Inches: "))
    height_m = height * 0.0254
else:
        print("Invalid input, please try again")
        exit()

weight_unit = input("Would you like to enter your weight in Kilograms or Pounds?: ") .upper().strip()
weight = float(input("Please enter your weight: "))

if weight_unit in ("K", "KG", "KILO", "KILOGRAM", "KILOGRAMS", "KGS"):
    weight_kg = weight
elif weight_unit in ("P", "LBS.", "LBS", "LB", "L", "POUND", "POUNDS"):
    weight_kg = weight / 2.205
else:
    print(error_message)
    exit()

bmi = round(weight_kg / (height_m ** 2), 2)

if bmi <= 18.5:
    bmi_index = "Underweight! - Please take good care of yourself"
elif bmi <= 24.9:
    bmi_index = "Normal Weight"
elif bmi <= 29.9:
    bmi_index = "Overweight! - Please take good care of yourself"
else:
    bmi_index = "Obese! - Please take better care of yourself"

print(f"Your calculated BMI is {bmi}, which is categorized as {bmi_index}.")
print("Remember, this is an approximation. Please refer to your doctor for health advise")
