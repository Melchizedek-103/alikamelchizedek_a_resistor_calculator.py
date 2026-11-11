
# RESISTOR COMBINATION CALCULATOR
# CTE213 Mini Project
# ND2 Mechatronics Engineering

# Function to collect a valid resistance value
def get_resistance(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value
            else:
                print("Resistance must be greater than zero.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to calculate series resistance
def calculate_series(resistors):
    return sum(resistors)


# Function to calculate parallel resistance
def calculate_parallel(resistors):
    total = sum(1 / r for r in resistors)
    return 1 / total


# Main program
print("================================")
print("  RESISTOR COMBINATION CALCULATOR")
print("================================")

# Ask for the number of resistors
while True:
    try:
        number = int(input("How many resistors do you have? "))

        if number > 0:
            break
        else:
            print("Enter at least one resistor.")

    except ValueError:
        print("Please enter a valid whole number.")


# Store resistor values in a list
resistors = []

# Collect resistance values
for i in range(number):
    value = get_resistance(
        f"Enter resistor {i + 1} value (ohms): "
    )
    resistors.append(value)


# Perform calculations
series = calculate_series(resistors)
parallel = calculate_parallel(resistors)


# Display results
print("\n========== RESULTS ==========")

print(f"Series Resistance: {series:.2f} ohms")
print(f"Parallel Resistance: {parallel:.2f} ohms")


# Our additional engineering feature
print("\n======= ENGINEERING INSIGHT =======")

if len(resistors) > 1:
    print(f"Smallest resistor: {min(resistors):.2f} ohms")
    print("Parallel resistance is lower than")
    print("the smallest individual resistance.")
else:
    print("You entered only one resistor.")
    print("Both combinations have the same value.")

print("\nCalculation completed successfully!")
