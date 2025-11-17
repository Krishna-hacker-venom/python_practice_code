# BMI CALCULATOR
# BMI Calculator
# Formula: BMI = weight (kg) / height (m)^2

def bmi_function(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# taking input section
weight_input = float(input("Enter your weight in kg : "))
height_input = float(input("Enter your height in meter : "))

# calculate BMI
bmi = bmi_function(weight_input, height_input)

# print results
print(f"Your BMI is {bmi:.2f}")
print("Category:", bmi_category(bmi))
