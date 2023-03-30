import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 1,
    "B": 2,
    "C": 4,
    "D": 8
}

symbol_value = {
    "A": 8,
    "B": 5,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Another way to copy a list
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], end="|")
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit value must be greater than 0")
        else:
            print("Please enter a value in £ only")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines < 1 or lines > MAX_LINES:
                print("Invalid number of lines")
            else:
                break
        else:
            print("Invalid number of lines")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line (" + str(MIN_BET) + "-" + str(MAX_BET) + ")?")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Invalid bet amount")
        else:
            print("Invalid bet amount")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your bet exceeds your current balance. Your balance is £{balance}")
        else:
            break

    print(f"You are betting £{bet} on {lines} lines. The total bet is £{total_bet}. Balance is £{balance}")

    slots = get_spin(ROWS, COLS, symbol_count)
    #  print(slots)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings} on lines {winning_lines}")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)


main()
