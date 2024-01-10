import random

# Defining world variables to pass to functions so everything still works by changing these variables here
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Define the parameters of the slot machine
ROWS = 3
COLS = 3

# Define symbols for the slot machine in a dictionary
symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] # checks first sybol value that following two columns should match
        for column in columns:
            symbol_to_check = column[line]  
            if symbol != symbol_to_check: # sees if following column matches
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items gives both key and value of dictionary. Key: symbol, Value: symbol_count
        for _ in range(symbol_count): # _ is an anonymous variable that can be used when you want to loop throught index values but dont care about count
            all_symbols.append(symbol)

    # logic to pick random values for each row in each column 
    columns = []
    for _ in range(cols):
            column = []
            current_symbols = all_symbols[:] # copying all_symbols list w/ ":" operator to 
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value) # removes the first instance of the value in the list. Do this so we keep track of what we've used from copyed list 
                column.append(value)

            columns.append(column)

    return columns

def print_slot_machine(columns): # transposes the previous column matrix set up as rows to be the appriate orientation we intended
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1: # max index because you can have 3 values but index for third is 2
                print(column[row], end = "  |  ")
            else:
                print(column[row], end = "")
        
        print()

def deposit():
    while True: 
        amount = input("Enter the amount you would like to deposit ")

        if amount.isdigit(): # test to see if input is appropriate
            amount = int(amount) # converts the given string to an int

            if amount > 0: 
                break
            else: print("Amount must be greater than 0")
        
        else:
            print("Please enter a positive number")

    return amount 


def get_number_of_lines():
    while True: 
        lines = input(f"Enter the number of lines you'd like to bet on (MAX:{str(MAX_LINES)})  ")

        if lines.isdigit():
            lines = int(lines)
            
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid line value")

        else: 
            print("Please enter a number")
    
    return lines

def get_bet(): 
    while True: 
        amount = input("Enter the amount you would like to bet on each line $")

        if amount.isdigit(): # test to see if input is appropriate
            amount = int(amount) # converts the given string to an int

            if MIN_BET <= amount <= MAX_BET: 
                break
            else: print(f"Amount must be within ({MIN_BET} : {MAX_BET})")
        
        else:
            print("Please enter a valid bet")

    return amount    


def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"a bet of ${total_bet} exceeds your balance of ${balance}") 
        else: 
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet it equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) 
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. (q tp quit).")
        
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")  

main()
