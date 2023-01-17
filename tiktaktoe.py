from os import system, name
import random

#func definitions 

#service funtions
# to clear the console
def clear():                  
    if name == 'nt':          #for win
        _ = system('cls')
    else:                     #for linux&mac
        _ = system('clear')
# get initial field list
def define_field():           
    return {a:[".",".","."] for a in range(1,4)}
#check if we have winner
def check_victory(game_field):
    win_symbol = 0
    condition = 1
    messege = ""
    all_lines = []
    columns = [[],[],[]]
    for row in game_field:
        all_lines.append(game_field[row])
        for i in range(0,len(game_field[row])-1):
            columns[i].append(game_field[row][i])
    for column in columns:
        all_lines.append(column)
    first_diag = []
    second_diag = []
    for i in range (1,3):
        first_diag.append(game_field[i][i-1])
        second_diag.append(game_field[i][3-i])
    all_lines.append(first_diag)
    all_lines.append(second_diag)
    for line in all_lines:
        if len(set(line)) == 1:
            win_symbol = line[1]
    if win_symbol == "X":
        messege = "Congratulations! You won!"
        condition = 2
    if win_symbol == "O":
        messege = "oh nyou~~ You lost~~"
        condition = 2
    return (condition, messege)
# draw the field with current state
def field_draw(field):        
    result_line="X123\r\n"
    for i in field:
        result_line += str(i)+"".join(field[i]) +"\r\n"
    print(result_line)
#pause
def input_pause():
    input("Press Enter to continue...\r\n")
#computer marking a spot. Really dumb should rewrite later
def random_mark(game_field):
    while True:
        row = random.randint(1,3)
        column = random.randint(0, 2)
        if game_field[int(row)][int(column)] == ".":
           game_field[int(row)][int(column)] = "O"
           return True
#just list of commands, so nobody gets funny ideas
def get_help():
    print("Choose action (type 'help' for list of commands)\r\n")
    print("List of commands:")
    print("'New game' for new game")
    print("'Mark XY' to mark the spot. X is row, Y is column")
    print("'Exit' or 'close' to exit game")
#mark a spot with bunch of checks
def mark(command, game_field):
    if not (int(command[5]) in range(1, 3) or int(command[6]) in range(1, 3) or len(command) > 7):
        routine(game_field, "Incorrect marking spot")
    else:
        X = int(command[5])
        Y = int(command[6])-1
        if game_field[X][Y] != ".":
            routine(game_field, "Spot is already marked!")
        else:
            game_field[X][Y] = "X"
            new_gamestate,messege = check_victory(game_field)
            if new_gamestate == 1:
                random_mark(game_field)
                routine(game_field)
            else:
                routine(game_field, messege)
    return new_gamestate

#main cycle routine
def routine(game_field, messege = ""):
    clear()
    field_draw(game_field)
    print(messege)
    get_help()


#interface functions
# main command function. really bad with just function, 
# better be finite state machine with external files but not sure if legal.
def interpret_command(command, gamestate, game_field):
    new_gamestate = gamestate
    if command.lower() in ("new game","newgame"):
        clear()
        game_field = define_field()
        new_gamestate = 1
        routine(game_field)
    elif command.lower() in ("exit", "close"):
        input("Thanks for playing!")
        exit()
    elif gamestate in (0,2):
        routine(game_field, "Start a new game by typing 'New game' on next prompt")
    elif command.lower()[:4] == "mark":
        new_gamestate = mark(command, game_field)
    else:
        routine(game_field, "Unknown command!")
    return new_gamestate


#initializing field and other stuff
game_field = define_field()
random.seed()
gamestate = 0

#initial starting dialogue
clear()
print("Welcome to Tik-Tak-Toe!")
routine(game_field)

#main cycle
while True:
    gamestate = interpret_command(input(), gamestate, game_field)

   

