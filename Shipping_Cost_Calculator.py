# Shipping Cost Calculator
# Here is a new update by dilrodri
## Here is another update by dilrodri
# This script calculates the total shipping cost based on weight and rate.

# Prompt the user to enter the package weight (in kilograms)
weight = float(input("Enter the package weight in kilograms: "))

# Prompt the user to enter the shipping rate per kilogram
rate = float(input("Enter the shipping rate per kilogram (USD): "))

# Calculate the total shipping cost
shipping_cost = weight * rate

# Display the result in USD
print(f"Total Shipping Cost: {shipping_cost} USD")

