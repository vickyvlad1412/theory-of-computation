import sys

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

def print_item_list(items):
    print(f"{Colors.BOLD}\n📦 Available Items:{Colors.ENDC}")
    for key, (item, price) in items.items():
        print(f"  {key}. {item} - RM{price:.2f}")

def get_valid_choice(prompt, choices):
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        print(f"{Colors.WARNING}⚠️ Invalid choice. Please try again.{Colors.ENDC}")

def dfa_mode(items):
    print_item_list(items)
    choice = get_valid_choice("\nSelect an item (1/2/3): ", items.keys())
    item_name, item_price = items[choice]
    print(f"\n📍 You selected: {Colors.OKGREEN}{item_name} - RM{item_price:.2f}{Colors.ENDC}")

    current_amount = 0.0
    print(f"\n🔁 {Colors.UNDERLINE}Initial State:{Colors.ENDC} {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")

    while current_amount < item_price:
        print(f"\n💠 {Colors.BOLD}Remaining:{Colors.ENDC} RM{item_price - current_amount:.2f}")
        print(f"🧠 {Colors.BOLD}Current State:{Colors.ENDC} {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")
        note_input = input("Insert RM0.5 or RM1.0: ").strip()

        if note_input not in ['0.5', '1.0']:
            print(f"{Colors.FAIL}❌ Invalid note inserted. DFA does not accept this. Terminating...{Colors.ENDC}")
            sys.exit()

        note = float(note_input)
        prev_state = f"Q{current_amount:.1f}"
        current_amount += note
        current_state = f"Q{current_amount:.1f}"
        print(f"🔀 Transition: {Colors.OKCYAN}{prev_state} ➝ {current_state}{Colors.ENDC}")

    print(f"\n🎉 {Colors.OKGREEN}Transaction complete. Please collect your {item_name}.{Colors.ENDC}")
    print(f"{Colors.BOLD}ℹ️ DFA vending machine terminates after completing a transaction.{Colors.ENDC}")
    print(f"{Colors.OKBLUE}Thank you for using the DFA vending machine!{Colors.ENDC}")
    sys.exit()

def nfa_mode(items):
    while True:
        print_item_list(items)
        choice = get_valid_choice("\nSelect an item (1/2/3): ", items.keys())
        item_name, item_price = items[choice]
        print(f"\n📍 You selected: {Colors.OKGREEN}{item_name} - RM{item_price:.2f}{Colors.ENDC}")

        current_amount = 0.0
        print(f"\n🔁 {Colors.UNDERLINE}Initial State:{Colors.ENDC} {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")

        while current_amount < item_price:
            print(f"\n💠 {Colors.BOLD}Remaining:{Colors.ENDC} RM{item_price - current_amount:.2f}")
            print(f"🧠 {Colors.BOLD}Current State:{Colors.ENDC} {Colors.OKCYAN}Q{current_amount:.1f}{Colors.ENDC}")
            note_input = input("Insert RM0.5 or RM1.0: ").strip()

            if note_input not in ['0.5', '1.0']:
                print(f"{Colors.WARNING}⚠️ Invalid note rejected. Please insert a valid note.{Colors.ENDC}")
                continue

            note = float(note_input)
            prev_state = f"Q{current_amount:.1f}"
            current_amount += note
            current_state = f"Q{current_amount:.1f}"
            print(f"🔀 Transition: {Colors.OKCYAN}{prev_state} ➝ {current_state}{Colors.ENDC}")

        print(f"\n🎉 {Colors.OKGREEN}Transaction complete. Please collect your {item_name}.{Colors.ENDC}")
        cont = get_valid_choice(f"\nWould you like to make another purchase?\n  1. Yes\n  2. No\nSelect: ", ['1', '2'])
        if cont == '2':
            print(f"\n{Colors.OKBLUE}Thank you for using the NFA vending machine!{Colors.ENDC}")
            break

def main():
    items = {
        '1': ("Water", 2.0),
        '2': ("Soda", 2.5),
        '3': ("Juice", 3.0)
    }

    print(f"{Colors.HEADER}{Colors.BOLD}🧃 Welcome to the Vending Machine Simulation!{Colors.ENDC}")
    mode = get_valid_choice("Choose mode:\n  1. DFA\n  2. NFA\nSelect: ", ['1', '2'])

    if mode == '1':
        print(f"\n{Colors.OKBLUE}⚙️ DFA Mode Activated{Colors.ENDC}")
        dfa_mode(items)
    else:
        print(f"\n{Colors.OKBLUE}⚙️ NFA Mode Activated{Colors.ENDC}")
        nfa_mode(items)

if __name__ == "__main__":
    main()

