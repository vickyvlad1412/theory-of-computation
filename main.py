import os

# Dictionary of items available in the vending machine
# Each item is a tuple of (name, price)
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

# Valid notes for the vending machine
valid_notes = [0.5, 1.0]

# ANSI escape codes for colored output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'    # Resets color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Clears the terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays the title banner for the vending machine
def print_title():
    print(f"{Colors.HEADER}{'='*45}")
    print(f"{' VENDING MACHINE SIMULATION ':^45}")
    print(f"{'='*45}{Colors.ENDC}")

# Prints the available items in the vending machine with their prices
def print_items():
    print(f"\n{Colors.BOLD}Available Items:{Colors.ENDC}")
    for key, (name, price) in items.items():
        print(f" {key}. {name:<15} - RM{price:.2f}")

# Prompts the user for input and validates it against a list of acceptable options
def get_valid_input(prompt, options):
    while True:
        choice = input(f"{Colors.OKBLUE}{prompt}{Colors.ENDC}").strip().lower()
        if choice in options:
            return choice
        print(f"{Colors.WARNING}Invalid input. Try again.{Colors.ENDC}")

# Simulates the transaction process for one item in the vending machine
def run_transaction(mode_name):
    print_items()  # Display available items
    item_choice = get_valid_input("Select an item by number: ", items.keys())

    # Retrieve selected item and its price
    item_name, price = items[item_choice]
    print(f"\nYou selected: {Colors.OKGREEN}{item_name} - RM{price:.2f}{Colors.ENDC}")

    # Initialize the current inserted amount and state display
    current_amount = 0.0
    current_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
    print(f"\n{Colors.UNDERLINE}Initial State:{Colors.ENDC} {current_state}")

    # Loop until the current amount meets or exceeds the price of the item
    while current_amount < price:
        remaining = price - current_amount
        print(f"\n{Colors.BOLD}Remaining amount:{Colors.ENDC} RM{remaining:.2f}")
        print(f"Current State: {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")
        print(f"{Colors.BOLD}Cumulative Inserted:{Colors.ENDC} RM{current_amount:.2f}")
        
        # Attempt to read user input as a float for note insertion
        try:
            note = float(input("Insert RM0.5 or RM1.0: ").strip())
        except ValueError:
            note = -1  # Invalid input

        # Handle invalid note input based on DFA or NFA mode
        if note not in valid_notes:
            if mode_name == "DFA":
                # In DFA mode, invalid input leads to termination
                print(f"\n{Colors.FAIL}Invalid note inserted! DFA mode - machine halts.{Colors.ENDC}")
                print(f"{Colors.WARNING}Transaction aborted. Goodbye.{Colors.ENDC}")
                return False  # TERMINATE
            elif mode_name == "NFA":
                # In NFA mode, invalid input is rejected and the user is prompted again
                print(f"{Colors.WARNING}Invalid note. Rejected. Please insert RM0.5 or RM1.0.{Colors.ENDC}")
                continue

        # Simulate the state transition by adding the note to the current amount
        prev_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
        current_amount += note
        current_state = f"{Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}"
        print(f"\nTransition: {prev_state} ➝ {current_state}")

    # Once the current amount meets or exceeds the price, dispense the item
    change = current_amount - price
    print(f"\n✅ {Colors.OKGREEN}Item dispensed: {item_name}{Colors.ENDC}")
    if change > 0:
        print(f" 🔄 Change returned: RM{change:.2f}")
    print(" 🎉 Transaction successfully completed.")
    return True  # Transaction successfully completed

# Main function to run the vending machine simulation
def vending_machine():
    clear()          # Clear the terminal screen
    print_title()    # Print the title banner
    
    # Ask the user to select the mode of operation (DFA or NFA)
    mode = get_valid_input("Select mode:\n  1. DFA\n  2. NFA\nEnter 1 or 2: ", ['1', '2'])
    mode_name = "DFA" if mode == '1' else "NFA"
    print(f"\nYou are now in {Colors.BOLD}{mode_name} Mode{Colors.ENDC}.\n")

    # Repeatedly allow transactions unless user exits or DFA halts
    while True:
        success = run_transaction(mode_name)   # Run a transaction in the selected mode
        if mode_name == "DFA" and not success:
            # In DFA mode, exit loop if invalid note is inserted
            print(f"\n{Colors.FAIL}DFA mode: Machine terminates due to error.{Colors.ENDC}")
            break
        
        # Prompt the user for another transaction or to exit
        print("\nDo you want to:")
        print("  1. Make another purchase")
        print("  2. Exit")
        choice = get_valid_input("Enter your choice (1 or 2): ", ['1', '2'])
        if choice == "2":
            print(f"\n{Colors.OKGREEN}Thank you for using the {mode_name} Vending Machine. Goodbye!{Colors.ENDC}")
            break

# Run the vending machine simulation
vending_machine()