import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def balance_show(balance):
    print(f"{Fore.GREEN}Your current balance is: {Fore.CYAN}{balance:.2f}")

def deposit(balance):
    print(f"{Fore.YELLOW}--- Deposit Funds ---")
    amount = float(input(f"{Fore.GREEN}Enter the amount to deposit: {Fore.CYAN}"))
    if amount < 0:
        print(f"{Fore.RED}Invalid amount. Please enter a positive value.")
        return balance
    
    balance += amount
    print(f"{Fore.GREEN}Deposit successful! {Fore.CYAN}Updated balance: {balance:.2f}")
    return balance

def withdraw(balance):
    print(f"{Fore.YELLOW}--- Withdraw Funds ---")
    amount = float(input(f"{Fore.GREEN}Enter the amount to withdraw: {Fore.CYAN}"))
    if amount > balance:
        print(f"{Fore.RED}Insufficient balance! You have only {balance:.2f}.")
        return balance
    elif amount < 0:
        print(f"{Fore.RED}Invalid input! You cannot withdraw a negative amount.")
        return balance
    else:
        balance -= amount
        print(f"{Fore.GREEN}Withdrawal successful! {Fore.CYAN}Updated balance: {balance:.2f}")
        return balance

def main():
    balance = 0.0
    is_running = True
    
    while is_running:
        print(f"\n{Fore.YELLOW}{Style.BRIGHT}--- Welcome to the Banking System ---")
        print(f"{Fore.CYAN}1: Show Balance")
        print(f"{Fore.CYAN}2: Deposit Funds")
        print(f"{Fore.CYAN}3: Withdraw Funds")
        print(f"{Fore.CYAN}4: Exit")
        
        choose = input(f"{Fore.GREEN}Choose an option (1 to 4): {Fore.CYAN}")

        if choose == '1':
            balance_show(balance)
        elif choose == '2':
            balance = deposit(balance)
        elif choose == '3':
            balance = withdraw(balance)
        elif choose == "4":
            is_running = False
        else:
            print(f"{Fore.RED}Invalid input. Please choose a valid option.")
    print(f"{Fore.MAGENTA}Thank you for using the Banking System! Goodbye!")

if __name__ == '__main__':
    main()
