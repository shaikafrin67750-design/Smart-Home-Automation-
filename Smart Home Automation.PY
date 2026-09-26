# Smart Home Automation System
# Python Project

devices = {
    "Light": False,
    "Fan": False,
    "AC": False,
    "TV": False
}

def show_status():
    print("\n--- Device Status ---")
    for device, status in devices.items():
        state = "ON" if status else "OFF"
        print(f"{device}: {state}")

while True:
    print("\n===== SMART HOME AUTOMATION =====")
    print("1. Turn ON device")
    print("2. Turn OFF device")
    print("3. Show device status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        device = input("Enter device name (Light/Fan/AC/TV): ").title()

        if device in devices:
            devices[device] = True
            print(f"{device} turned ON.")
        else:
            print("Invalid device!")

    elif choice == "2":
        device = input("Enter device name (Light/Fan/AC/TV): ").title()

        if device in devices:
            devices[device] = False
            print(f"{device} turned OFF.")
        else:
            print("Invalid device!")

    elif choice == "3":
        show_status()

    elif choice == "4":
        print("Smart Home System Closed.")
        break

    else:
        print("Invalid choice! Please try again.")
