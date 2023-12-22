# User-defined variables
userName = "JohnDoe"
userAge = 25
userLocation = "City123"


# Function with a user-defined variable
def greet_user():
    print(f"Hello, {userName}!")


# Another user-defined variable
favoriteColor = "Blue"

# Imported module
import math


# User-defined function
def calculate_square_area(side_length):
    return side_length**2


# Using an imported function
circle_area = math.pi * calculate_square_area(5)

# More user-defined variables
userAddress = "123 Main Street"
userEmail = "john@example.com"

# Display user information
print("User Information:")
print(f"Name: {userName}")
print(f"Age: {userAge}")
print(f"Location: {userLocation}")
print(f"Favorite Color: {favoriteColor}")
print(f"Address: {userAddress}")
print(f"Email: {userEmail}")

# Function call
greet_user()

# Display calculated area
print(f"Calculated Circle Area: {circle_area}")
