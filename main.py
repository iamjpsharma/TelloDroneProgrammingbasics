# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Get user input
full_address = input("Enter your full address: ")
distance = float(input("Enter the distance (in kilometers) from your address to the restaurant: "))
order_amount = float(input("Enter the order amount (in AUD): "))

# Calculate packaging charges
if order_amount > 20 and order_amount <= 35:
    packaging_charge = order_amount * 0.1
elif order_amount > 35 and order_amount <= 50:
    packaging_charge = order_amount * 0.08
else:
    packaging_charge = order_amount * 0.06

# Calculate delivery charges
if distance > 20 and distance <= 30:
    delivery_charge = 3
elif distance > 30 and distance <= 40:
    delivery_charge = 6
else:
    delivery_charge = 10

# Calculate total charges
total_charge = order_amount + packaging_charge + delivery_charge

# Display the details
print("\nOrder Details:")
print("Full Address: ", full_address)
print("Distance to Restaurant (in km): ", distance)
print("Order Amount (in AUD): ", order_amount)
print("Packaging Charge (10% of order amount): ", packaging_charge)
print("Delivery Charge: ", delivery_charge)
print("Total Charge: ", total_charge)