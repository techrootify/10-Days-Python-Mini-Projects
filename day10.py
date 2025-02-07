# BMI Calculator

def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = calculate_bmi(weight, height)

print(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
else:
    print("You are overweight.")
