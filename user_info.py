# user_info.py
# Program to collect and display user information
# Fulfills: inputs, constant, explicit/implicit casting, types, and BMI (bonus)

# Constant (company name)
COMPANY_NAME = "TechSpark"

# --- Take user inputs (strings from keyboard) ---
name = input("Enter your name: ")
age_input = input("Enter your age: ")          # string for now
weight_input = input("Enter your weight (kg): ")  # string for now
email = input("Enter your email: ")

# --- Explicit type casting (required by assignment) ---
age = int(age_input)         # explicit: string -> int
weight = float(weight_input) # explicit: string -> float

# --- Implicit type casting example ---
# mixing int (age) and float (height) gives a float result automatically
height = 1.75  # fixed height in meters (implicit example uses this float)
mixed_result = age + height  # int + float -> float (implicit conversion)

# Another explicit cast example (float -> int)
weight_as_int = int(weight)  # explicit casting: float -> int (loses decimals)

# --- Calculate BMI (bonus) ---
bmi = weight / (height ** 2)

# --- Display results and data types ---
print("\n--- User Details ---")
print("Company:", COMPANY_NAME)
print("Name:  ", name, " (type:", type(name), ")")
print("Age:   ", age,  " (type:", type(age),  ")")
print("Weight:", weight," (type:", type(weight),")")
print("Email: ", email, " (type:", type(email),")")

print("\n--- Casting Examples ---")
print("Explicit: weight_as_int =", weight_as_int, " (type:", type(weight_as_int), ")")
print("Implicit: mixed_result =", mixed_result, " (type:", type(mixed_result), ")")

print(f"\nWelcome {name} to {COMPANY_NAME}!")
print(f"Your BMI (using fixed height {height} m) is: {bmi:.2f}")
