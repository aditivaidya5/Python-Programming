
import random

while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:

        # Choose cab type
        print("\nSelect Cab Type:")
        print("1. Auto - Rs. 12/km")
        print("2. Sedan - Rs. 18/km")
        print("3. SUV - Rs. 25/km")

        try:
            cab_choice = int(input("Enter cab choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if cab_choice == 1:
            cab_type = "Auto"
            rate = 12
        elif cab_choice == 2:
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == 3:
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice! Returning to main menu.")
            continue

        # Choose predefined route
        print("\nSelect Route:")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        try:
            route_choice = int(input("Enter route choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if route_choice == 1:
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == 2:
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == 3:
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice! Returning to main menu.")
            continue

        # Calculate fare
        fare = rate * distance

        print("\n========== RIDE DETAILS ==========")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print("Total Fare: Rs.", fare)

        # Confirm or cancel before sharing OTP
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        try:
            confirm = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter 1 or 2.")
            continue

        if confirm == 2:
            print("Ride cancelled successfully. No OTP shared.")
            continue

        elif confirm == 1:
            otp = random.randint(1000, 9999)
            print("\nYour ride OTP is:", otp)
            print("OTP has been shared with you.")
            print("IMPORTANT: Ride cancellation is not allowed")
            print("after the OTP has been shared.")
            print("Booking confirmed successfully!")
            continue

        else:
            print("Invalid confirmation choice! Returning to main menu.")
            continue

    elif choice == 2:
        print("Thank you for using Cab Booking Chatbot!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
