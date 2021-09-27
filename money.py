total_funds = int (input('How much is your money right now?'))
amount = 0
new_funds = total_funds

def deposit(amount,new_funds):
    amount = input("How much money you want to input??")
    new_funds = new_funds + amount
    return new_funds


def withdraw(amount,new_funds):
    amount = input("How much money you want to output??")
    if new_funds < amount:
        print("Your funds are insufficient, and cannot be withdrawn")
    else:

        new_funds = new_funds - amount
        return new_funds

def in_or_out (amount,new_funds):
    x = int(input("Would you like to deposit (0) or withdraw (1)"))
    if x == 0:
        deposit(amount,new_funds)
    else:
        withdraw(amount,new_funds)

def check(new_funds):
    print("Your money is currently " + new_funds)

def main():
    process = True
    while process:
        in_or_out(amount,new_funds)
        check(new_funds)
        x = input ("Do you want to continue your process? Y/N")
        if x.lower == "y":
            continue
        else:
            print("Thanks for using our services!! See you soon.")
            break

# starts running the program
main()
# done





