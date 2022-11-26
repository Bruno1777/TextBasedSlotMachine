import random

MAX_LINES = 3
ROWS = 3
COLS = 3

symbol_num = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 8,
    "B" : 6,
    "C" : 4,
    "D" : 2
}

def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a digit.")
    return amount


def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else:
                print("Lines must be between [1-" + str(MAX_LINES) + "].")
        else:
            print("Please enter a digit.")
    return lines

def get_sum_of_bets(balance, lines):
    while True:
        bet = input("Enter the amount you want to bet: $ ")
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance:
                break
            else:
                print("Bet total must be less than your current balance.")
        else:
            print("Please enter a digit.")
    return bet

def get_slot_rows(rows, cols, symbol):
    all_symbols = []
    for num, symbol_num in symbol.items():
        for _ in range(symbol_num):
            all_symbols.append(num)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for column in columns:
            print(column[row], " | ", end="")
        print()

def get_winnings(slots, value, lines, bet):
    winnings = 0
    for line in range(lines):
        symbol = slots[0][line]
        for slot in slots:
            symbol_to_check = slot[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet

    return winnings

def game(balance):
    lines = get_num_of_lines()
    bet = get_sum_of_bets(balance, lines)
    total_bet = bet * lines
    if total_bet <= balance:
        print("you are betting " + str(total_bet) + " on " + str(lines))
    else:
        print("You can't bet more than you have.")
        quit

    slots = get_slot_rows(ROWS, COLS, symbol_num)
    print_slot_machine(slots)

    winnings = get_winnings(slots, symbol_value, lines, bet)
    if winnings != 0:
        print("You won $" + str(winnings) +"! congrats")
        balance += winnings
    else:
        print("I'm sorry, you lost.")
        balance = balance - total_bet

def main():
    balance = deposit()
    while balance >= 0:
        game(balance)
    
main()
