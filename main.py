import os

items = {
    "1": ("Water", 2.00),
    "2": ("Soda", 3.50),
    "3": ("Chips", 4.50),
    "4": ("Chocolate", 6.00),
    "5": ("Coffee", 7.50),
    "6": ("Juice", 8.50),
    "7": ("Sandwich", 9.00),
    "8": ("Energy Drink", 10.00)
}

valid_notes = [0.5, 1.0]

# ANSI Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(f"{Colors.HEADER}{'='*45}")
    print(f"{' VENDING MACHINE SIMULATION ':^45}")
    print(f"{'='*45}{Colors.ENDC}")

def print_items():
    print(f"\n{Colors.BOLD}Available Items:{Colors.ENDC}")
    for key, (name, price) in items.items():
        print(f" {key}. {name:<15} - RM{price:.2f}")

def get_valid_input(prompt, options):
    while True:
        choice = input(f"{Colors.OKBLUE}{prompt}{Colors.ENDC}").strip().lower()
        if choice in options:
            return choice
        print(f"{Colors.WARNING}Invalid input. Try again.{Colors.ENDC}")

def run_transaction(mode_name):
    print_items()
    item_choice = get_valid_input("Select an item by number: ", items.keys())

    item_name, price = items[item_choice]
    print(f"\n🛒 You selected: {Colors.OKGREEN}{item_name} - RM{price:.2f}{Colors.ENDC}")

    current_amount = 0.0
    current_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
    print(f"\n🔁 {Colors.UNDERLINE}Initial State:{Colors.ENDC} {current_state}")

    while current_amount < price:
        remaining = price - current_amount
        print(f"\n💰 {Colors.BOLD}Remaining:{Colors.ENDC} RM{remaining:.2f}")
        print(f"📍 Current State: {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")
        print(f"💵 {Colors.BOLD}Cumulative Inserted:{Colors.ENDC} RM{current_amount:.2f}")
        try:
            note = float(input("Insert RM0.5 or RM1.0: ").strip())
        except ValueError:
            note = -1  # Invalid

        if note not in valid_notes:
            if mode_name == "DFA":
                print(f"\n{Colors.FAIL}Invalid note inserted! DFA mode - machine halts.{Colors.ENDC}")
                print(f"{Colors.WARNING}Transaction aborted. Goodbye.{Colors.ENDC}")
                return False  # TERMINATE
            elif mode_name == "NFA":
                print(f"{Colors.WARNING}Invalid note. Rejected. Please insert RM0.5 or RM1.0.{Colors.ENDC}")
                continue

        prev_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
        current_amount += note
        current_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
        print(f"\n🔀 Transition: {prev_state} ➝ {current_state}")

    change = current_amount - price
    print(f"\n✅ {Colors.OKGREEN}Item dispensed: {item_name}{Colors.ENDC}")
    if change > 0:
        print(f"🔄 Change returned: RM{change:.2f}")
    print("🎉 Transaction complete.")
    return True  # Transaction completed

def vending_machine():
    clear()
    print_title()
    
    mode = get_valid_input("Select mode:\n  1. DFA\n  2. NFA\nEnter 1 or 2: ", ['1', '2'])
    mode_name = "DFA" if mode == '1' else "NFA"
    print(f"\n🧠 You are now in {Colors.BOLD}{mode_name} Mode{Colors.ENDC}.\n")

    while True:
        success = run_transaction(mode_name)
        if mode_name == "DFA" and not success:
            print(f"\n{Colors.FAIL}DFA mode: Machine terminates due to error.{Colors.ENDC}")
            break
        print("\nDo you want to:")
        print("  1. Make another purchase")
        print("  2. Exit")
        choice = get_valid_input("Enter your choice (1 or 2): ", ['1', '2'])
        if choice == "2":
            print(f"\n{Colors.OKGREEN}Thank you for using the {mode_name} Vending Machine. Goodbye!{Colors.ENDC}")
            break

vending_machine()
