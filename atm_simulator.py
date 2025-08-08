# Simple ATM Program
balance = 5000
statement = []

while True:
    print("\n1.Check Balance  2.Deposit  3.Withdraw  4.Mini Statement  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        print("Balance:", balance)

    elif ch == 2:
        amt = float(input("Enter deposit: "))
        balance += amt
        statement.append(f"Deposit {amt}")
        print("Deposited! New balance:", balance)

    elif ch == 3:
        amt = float(input("Enter withdraw: "))
        if amt <= balance:
            balance -= amt
            statement.append(f"Withdraw {amt}")
            print("Withdrawn! New balance:", balance)
        else:
            print("Insufficient funds!")

    elif ch == 4:
        print("Last 3 transactions:", statement[-3:])

    elif ch == 5:
        print("Exit. Bye!")
        break

    else:
        print("Invalid option")
