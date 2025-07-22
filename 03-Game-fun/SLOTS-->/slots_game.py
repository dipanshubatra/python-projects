import random
import time
import winsound

def slotsmachine():
    print("********* WELCOME *********")
    print("*****⭐ TO SLOTS BET ⭐ *****")
    print("******* 🍒🍋🍉🍇🍊 *********")

    money = 100
    slots = ['🍒', '🍋', '🍉', '🍇', '🍊']

    while True:
        print("\n🎮 MENU OPTIONS:")
        print("1. ADD MONEY 💸")
        print("2. PLAY SLOTS 🎰")
        print("3. CHECK BALANCE 💳")
        print("4. EXIT GAME ❌")

        choice = input("Enter the option (1/2/3/4): ")

        if choice == "1":
            print(f"🧾 Current Balance: ${money}")
            print('Recharge Options:')
            print("1. $100")
            print("2. $500")
            print("⚠️ Max balance is $1000")
            recharge = input("Enter option (1/2): ")

            if money >= 1000:
                print("💥 You cannot exceed the $1000 limit!\n")
            elif recharge == "1":
                if money + 100 > 1000:
                    print("💥 Cannot add more than $1000!\n")
                else:
                    money += 100
                    print(f"✅ Money Added. New Balance: ${money}")
            elif recharge == "2":
                if money + 500 > 1000:
                    print("💥 Cannot add more than $1000!\n")
                else:
                    money += 500
                    print(f"✅ Money Added. New Balance: ${money}")
            else:
                print("❌ Invalid recharge option!")

        elif choice == "2":
            if money <= 0:
                print("❌ Not enough balance to play. Please recharge first.")
                continue

            print(f"\n💰 Your current balance is: ${money}")
            try:
                bet = int(input("Enter the amount you want to bet: $"))
                if bet <= 0:
                    print("❌ Bet must be more than 0.")
                    continue
                if bet > money:
                    print("❌ You cannot bet more than your current balance.")
                    continue
            except ValueError:
                print("❌ Please enter a valid number.")
                continue

            print("\n🎰 Spinning the slot machine...")
            winsound.Beep(800, 200)

            for i in range(2):
                for symbol in slots:
                    print(f"\r Preparing the game {symbol * 5}", end="", flush=True)
                    time.sleep(0.1)
            print("\r" + " " * 50, end="")

            spin = [random.choice(slots) for _ in range(3)]
            result = " | ".join(spin)
            print(f"\n🎰 Result: {result}")

            money -= bet

            if spin[0] == spin[1] == spin[2]:
                win_amount = bet * 5
                money += win_amount
                print(f"🎉 JACKPOT! You win ${win_amount}!")
                winsound.Beep(100, 300)
                winsound.Beep(1400, 300)
                winsound.Beep(1600, 400)
            elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin[2]:
                win_amount = bet * 2
                money += win_amount
                print(f"✨ Nice! You win ${win_amount}!")
                winsound.Beep(400, 10000)
                winsound.Beep(1400, 200)
            else:
                print(f"😢 You lost your bet of ${bet}.")
                winsound.Beep(500, 500)

            print(f"💰 Current Balance: ${money}")

        elif choice == "3":
            for i in range(1, money + 1):
                if i % 100 == 0:
                    winsound.Beep(700, 20)
                print(f"\r💸 Balance: ${i}", end="", flush=True)
                time.sleep(0.005)
            print()

        elif choice == "4":
            for _ in range(5):
                for symbol in slots:
                    print(f"\rExiting {symbol * 5}", end="", flush=True)
                    time.sleep(0.07)
            print("\r" + " " * 40)
            print("\n👋 Goodbye! Thanks for playing.")
            winsound.Beep(400, 500)
            break

        else:
            print("❌ Invalid input! Please enter 1, 2, 3, or 4.")

slotsmachine()
