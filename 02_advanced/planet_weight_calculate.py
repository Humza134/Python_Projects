# Define gravity constants for the planets
# MERCURY_CONSTANT = 0.376
# VENUS_CONSTANT = 0.889
# MARS_CONSTANT = 0.378
# JUPITER_CONSTANT = 2.36
# SATURN_CONSTANT = 1.081
# URANUS_CONSTANT = 0.815
# NEPTUNE_CONSTANT = 1.14

# def get_mars_weight():
#     user_weight:float = float(input("what is your weight"))
    
#     mars_weight = round(user_weight * MARS_CONSTANT, 2)
#     return mars_weight

# my_weight_on_mars = get_mars_weight()
# print(my_weight_on_mars)


# def planet_weight_calculate():
#     try:
#         user_weight = float(input("What is your weight? "))
#         planet_name = input("What is the name of the planet? ")

#         # Initialize gravity constant
#         gravity_constant = 0

#         # Match planet name with constants
#         if planet_name.lower() == "mars":
#             gravity_constant = MARS_CONSTANT
#         elif planet_name.lower() == "mercury":
#             gravity_constant = MERCURY_CONSTANT
#         elif planet_name.lower() == "venus":
#             gravity_constant = VENUS_CONSTANT
#         elif planet_name.lower() == "jupiter":
#             gravity_constant = JUPITER_CONSTANT
#         elif planet_name.lower() == "saturn":
#             gravity_constant = SATURN_CONSTANT
#         elif planet_name.lower() == "uranus":
#             gravity_constant = URANUS_CONSTANT
#         elif planet_name.lower() == "neptune":
#             gravity_constant = NEPTUNE_CONSTANT
#         else:
#             return "Invalid planet name. Please try again."

#         # Calculate weight
#         weight = round(user_weight * gravity_constant, 2)
#         return f"Your weight on {planet_name.capitalize()} is {weight} kg."

#     except ValueError:
#         return "Invalid input for weight. Please enter a numeric value."

# my_weight = planet_weight_calculate()
# print(my_weight)


gravity_constants = {
    "mercury": 0.376,
    "venus": 0.889,
    "mars": 0.378,
    "jupiter": 2.36,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.14
}
    
def calculate_planet_weight():
    while True:
        try:
            user_weight = float(input("Enter your weight"))
            break
        except ValueError:
            print("Invalid weight provide only numeric value")
    
    planet_name = input("Enter the planet name").lower()

    if planet_name in gravity_constants:
        weight = round(user_weight * gravity_constants[planet_name],2)
        return f"Your weight on {planet_name.capitalize()} is {weight} kg."
    else:
        return "Invalid planet name"


result = calculate_planet_weight()
print(result)