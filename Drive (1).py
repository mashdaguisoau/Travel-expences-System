# Travel Transaction System
print("=" * 40)
print("        ✈️  TRAVEL TRANSACTION SYSTEM")
print("=" * 40)

# Get user details
name = input("\nEnter your name: ")
print("\n--- Choose Your Destination ---")
print("1. Manila → Cebu      - ₱2,500")
print("2. Manila → Davao     - ₱3,200")
print("3. Manila → Palawan   - ₱2,800")
print("4. Manila → Baguio    - ₱1,500")

choice = int(input("\nEnter your choice (1-4): "))

# Set price & destination using if-elif-else
if choice == 1:
    destination = "Cebu"
    price = 2500
elif choice == 2:
    destination = "Davao"
    price = 3200
elif choice == 3:
    destination = "Palawan"
    price = 2800
elif choice == 4:
    destination = "Baguio"
    price = 1500
else:
    print("\n❌ Invalid choice! Please restart the program.")
    exit()  # End program if wrong input

# Choose travel class
print("\n--- Choose Travel Class ---")
print("1. Economy   (No extra charge)")
print("2. Business  (+₱800)")
print("3. First Class (+₱1,500)")

class_choice = int(input("\nEnter your choice (1-3): "))

if class_choice == 1:
    travel_class = "Economy"
    add_cost = 0
elif class_choice == 2:
    travel_class = "Business"
    add_cost = 800
elif class_choice == 3:
    travel_class = "First Class"
    add_cost = 1500
else:
    print("\n❌ Invalid class choice!")
    exit()

# Calculate total
total = price + add_cost

# Display receipt
print("\n" + "=" * 40)
print("          📝  TRANSACTION RECEIPT")
print("=" * 40)
print(f"Passenger Name: {name}")
print(f"Destination:    Manila → {destination}")
print(f"Travel Class:  {travel_class}")
print(f"Base Fare:     ₱{price:,}")
if add_cost > 0:
    print(f"Class Upgrade: +₱{add_cost:,}")
print("-" * 40)
print(f"TOTAL AMOUNT:  ₱{total:,}")
print("=" * 40)
print("    ✅ Thank you for booking with us! Safe trip! 🌏")

