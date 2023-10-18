# Create an empty set to store user data
user_data = set()

# Set the number of data points you want to collect
num_data_points = int(input("How many data points would you like to enter? "))

# Loop to collect data
for i in range(num_data_points):
    data = input(f"Enter data point {i + 1}: ")
    user_data.add(data)

# Print the data entered by the user
print("Data entered by the user:")
for data in user_data:
    print(data)
