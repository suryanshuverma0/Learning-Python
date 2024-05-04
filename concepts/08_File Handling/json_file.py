import json

# Create data dictionary
data = {"name": "Suryanshu Verma", "age": 21}

# Open file in write mode
with open("data.json", "w") as file:
    # Write JSON data to file
    json.dump(data, file)



# Open the JSON file in read mode
with open("data.json", "r") as file:
    # Load the JSON data from the file
    data = json.load(file)

# Print the loaded data
print("Data from JSON file:", data)

