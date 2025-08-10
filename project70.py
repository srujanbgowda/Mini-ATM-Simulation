def main():
    balence = 1000
    pin_code = "961196"

    print("🏧Welcome to the mini ATM!")

    for attempt in range(3):
        pin = input("🔐Enter your 6- digit PIN:")
        if pin == pin_code:
            break
        else:
            print("❌ Incorrect PIN.")
    else:
        print("🔒Too many wrong attempts . Exists..")        
        return 
    while True:
        print("\n 📋 ATM NENU")
        print("1.💰 Check Balence")
        print("2.➕ Deposit")
        print("3.➖ Withdraw")
        print("4.🚪 Exit")
        choice  = input("Enter your choice(1-4):")

        if choice == "1":
            print(f"💳 Your Current balece is ₹ {balence}")

        
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: ₹"))
                if amount > 0:
                    balance += amount
                    print(f"✅ ₹{amount} deposited. New balance: ₹{balance}")
                else:
                    print("⚠️ Enter a positive amount.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")


        
        elif choice == "3":
            try:   
                amount = float(input("Enter withdrawal amount: ₹"))
                if 0 < amount <= balance:
                    balance -= amount
                    print(f"✅ ₹{amount} withdrawn. New balance: ₹{balance}")
                elif amount > balance:
                    print("❌ Insufficient balance.")
                else:
                    print("⚠ Enter a positive amount.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        elif    choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose from 1-4.")

if __name__ == "__main__":
    main()

