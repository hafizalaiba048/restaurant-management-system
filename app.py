# Restaurant Management System - Python
menu = {
    "Chicken Biryani": 450,
    "Chicken Karahi": 1200,
    "Zinger Burger": 550,
    "Pizza": 999,
    "Cold Drink": 150,
    "Kheer": 250
}

venues = ["Dine-In Main Hall", "Family Hall", "Takeaway", "Home Delivery", "Rooftop"]

print("Welcome to Zaika Restaurant")
print("Venues:", venues)

total = 0
while True:
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item} - Rs.{price}")
    choice = input("Kya order karna hai? (done likho khatam karne ke liye): ")
    if choice == "done":
        break
    if choice in menu:
        qty = int(input("Kitne chahiye? "))
        total += menu[choice] * qty
        print(f"Add ho gaya: {choice} x {qty}")
    else:
        print("Ye item menu me nahi hai")

print(f"\nTOTAL BILL: Rs.{total}")
print("Shukriya! Apka order confirm ho gaya.")
