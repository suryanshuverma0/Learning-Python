def calculate_age(year):
    if year < 0:
        raise ValueError("Invalid year. Year must be positive.")
    return 2024 - year

try:
    age = calculate_age(2003)
    print("Age:", age)
except ValueError as e:
    print("Error:", e)
