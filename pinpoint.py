from random import *
from time import *
from os import *

system("title PinPoint")
system("color 0a")

def txt_check(text):
    if text == "exit()":
        return "y"
    else:
        return "n"
    
def print_board(board):
    i = 1
    print "COL             1       2       3       4       5       6       7       8       9       10      11      12      13      14      15"
    print "                .       .       .       .       .       .       .       .       .       .       .       .       .       .       ."
    print "R               .       .       .       .       .       .       .       .       .       .       .       .       .       .       ."
    print "O               .       .       .       .       .       .       .       .       .       .       .       .       .       .       ."
    print "W               .       .       .       .       .       .       .       .       .       .       .       .       .       .       .\n"
    
    for row in board: # can be board
        if i < 10:                
            print i , "- - - - - - ",
        else:
            print i , "- - - - - -",
        print row[0]+"  |  "+row[1]+"  |  "+row[2]+"  |  "+row[3]+"  |  "+row[4]+"  |  "+row[5]+"  |  "+row[6]+"  |  "+row[7]+"  |  "+row[8]+"  |  "+row[9]+"  |  "+row[10]+"  |  "+row[11]+"  |  "+row[12]+"  |  "+row[13]+"  |  "+row[14]
        print
        i += 1

def guess_input(fbreak = 0,guess_col = 0,guess_row = 0):
        
    while True:
        guess_row = raw_input("Guess ROW: ")
        if txt_check(guess_row) == "y":
            fbreak = 1
            break
        while guess_row.isdigit() == False:
            guess_row = raw_input("Guess only a number for ROW: ")
            if txt_check(guess_row) == "y":
                fbreak = 1
                break
        if fbreak == 1: break
        guess_row = int(guess_row)
        if guess_row <= 15 and guess_row >= 1: break
        else: print "Enter only 1 to 15..."

    while True and fbreak == 0:
        guess_col = raw_input("Guess COL: ")
        if txt_check(guess_col) == "y":
            fbreak = 1
            break
        while guess_col.isdigit() == False:
            guess_col = raw_input("Guess only a number for COL: ")
            if txt_check(guess_col) == "y":
                fbreak = 1
                break
        if fbreak == 1: break
        guess_col = int(guess_col)
        if guess_col <= 15 and guess_col >= 1: break
        else: print "Enter only 1 to 15..."
        
    return (guess_col,guess_row,fbreak)

def checking_option_value(pin_row_fun,pin_col_fun,guess_row_fun,guess_col_fun,option_fun=0): # To find the value of option used later (UDRL)
#
    if guess_col_fun == pin_col_fun:
        if guess_row_fun > pin_row_fun:
            option_fun = 4
        elif guess_row_fun < pin_row_fun:
            option_fun = 3
#
    elif guess_row_fun == pin_row_fun:
        if guess_col_fun > pin_col_fun:
             option_fun = 2
        elif guess_col_fun < pin_col_fun:
             option_fun = 1
#
    elif guess_col_fun > pin_col_fun:
        if guess_row_fun > pin_row_fun:
            while option_fun == 3 or option_fun == 0:
                option_fun = randint(2,4)
        elif guess_row_fun < pin_row_fun:
            option_fun = randint(2,3)
#
    elif guess_col_fun < pin_col_fun:                
        if guess_row_fun > pin_row_fun:
            while option_fun == 2 or option_fun == 3 or option_fun == 0:
                option_fun = randint(1,4)
        elif guess_row_fun < pin_row_fun:
            while option_fun == 2 or option_fun == 0:
                option_fun = randint(1,3)
#
    if option_fun == 1: option_fun = "{R}" # Check coversions for options here
    elif option_fun == 2: option_fun = "{L}"
    elif option_fun == 3: option_fun = "{D}"
    elif option_fun == 4: option_fun = "{U}"
    
    return option_fun

def StatementAfterRow(i,r,c):
    print "Remember the exit() function can be used to end this game!!"
    print "The pin is",
    if i == "R": print "towards the right of",
    elif i == "L": print "towards the left of",
    elif i == "D": print "below",
    elif i == "U": print "above",
    print "your cordinate.\nYou previously entered - [ COL -" , c , "| ROW -" , r , "]\n"
    
def print_win():
    print """

0               0        0000000000000000000         0  0     0     0  0 
 0             0         0                 0         0   0   0 0   0   0
  0           0          0    000   000    0         0    0 0   0 0    0
   0         0           0    0 0   0 0    0         0     0     0     0
    0       0            0    000   000    0         0        0        0
     0     0             0                 0         0        0        0
      0   0              0                 0         0        0        0    
       0 0               0                 0         0        0        0
        0                0   0         0   0         0        0        0
        0                0   0         0   0         0        0        0
        0                0   0         0   0         0     0     0     0
        0                0   0         0   0         0     0 0   0     0
        0                0   0         0   0         0     0  0  0     0
        0                0   00000000000   0         0     0   0 0     0
        0                0                 0         0     0     0     0
        0                0000000000000000000         0000000000000000000

"""

def intro():
        pin_board1 = []
        for blah_blah in range(15):
            pin_board1.append(["{ }"] * 15)
        system("cls");print "Ok! Welcome to PinPoint...";print "\n1) First we will have a look at the board.\n";skip = raw_input("Press enter to go to next instruction: ");print_board(pin_board1);print "2) Notice the top part is colomn and left being row...";print "3) The row is always entered first and then the colomn...";print "4) Your marker is placed in the coordinate entered...\n";skip = raw_input("Press enter to go to next instruction: ");system("cls");print "Now say you enter [COL-7 and ROW-8]";skip = raw_input("Press enter to go to next instruction: ");pin_board1[7][6] = "{L}";print_board(pin_board1);print "Now the loaction (7,8) is L, which means that the pin is left of (7,8),i.e, any col < 7!!!\nSimilarly it can show R(right) , U(up) , D(down)...";skip = raw_input("Press enter to go to next instruction: ");system("cls");print "Using these giudelines you have to find the pin\s!\nIf you find it, the board will look like this(in medium and hard levels which we will come to later)...\nLook at (7,8) again";skip = raw_input("Press enter to go to next instruction: ");pin_board1[7][6] = "{\21}";print_board(pin_board1);skip = raw_input("Press enter to go to next instruction: ");system("cls");print "Now let us talk about the kinds of levels 1)Easy 2)Medium 3)Hard\nFirst we talk about easy!! (P.S.: Look at the heading in window bar (even during games))";skip = raw_input("Press enter to go to next instruction: ");system("cls");system("title Easy's intro");print "1) In easy, there is only one pin to find and once you find it you win.";print "2) The letters at the coordinate signify this pin only.";print "And........ That is it! Simple right?\n";skip = raw_input("Press enter to go to next instruction: ");print "Here is an example...";pin_board1[8][6] = "{U}";pin_board1[6][6] = "{D}";pin_board1[7][7] = "{L}";pin_board1[7][5] = "{R}";print_board(pin_board1);skip = raw_input("Press enter to go to next instruction: ");system("cls");system("title Medium's intro");print "1) For medium level there are 2 pins to find, so it gets confusing...";print "2) The colour of the screen text will change to diffrentiate between pin1 or pin2...";print "Something like this...";system("color 0b");sleep(1);system("color 0d");sleep(1);system("color 0a");sleep(1);system("color ");print "Got it? This way you will know what location was for which pin, if you can roughly remember the location entered in the past few turnes...";skip = raw_input("Press enter to go to next instruction: ");system("cls");system("title Hard's Intro");print "The hard level is just killer!!";print "This is similar to the second level but no color change.";print "So, you realy have to analise and board...\n";skip = raw_input("Press enter to go to next instruction: ");system("cls");print "\t\t\t\t\t\t***************** IMPORTANT ******************\n";print "Use the 'exit()' function to exit the game where ever you can enter a value in the game( i.e. just type exit() and it will exit the game )...";skip = raw_input("Press enter to go to next: ");print "\n\n\nGood luck! You will love it, the levels involve fun(easy) , memory(medium) and analytical thinking(hard)!!";print "\n\nYou now can choose a level !!!";skip = raw_input("Press enter to go game page: ");system("title PinPoint");system("cls")   

if raw_input("Enter y to learn the game (use intro() in middle of game): ").upper() == "Y":
    intro()
        
while 1: # New game...

    system("cls")
    system("color 0b")
    game_choice = raw_input("Enter 1:Easy | 2:Medium | 3:Hard : ")
    txt = txt_check(game_choice)
    if txt == "y":
        break    
    while game_choice not in "123" or game_choice == "":
        game_choice = raw_input("Enter 1,2 or 3 only : ")
        txt = txt_check(game_choice)
        if txt == "y":
            break
    game_choice = int(game_choice)
    system("cls")
    if game_choice == 1:
        system("title PinPoint (Easy)")
        system("color 0d")
    elif game_choice == 2:
        system("title PinPoint (Medium)")
    elif game_choice == 3:
        system("title PinPoint (Hard)")
        system("color 0d")

    pin_board = []
    for blah_blah in range(15):
        pin_board.append(["{ }"] * 15)

    print "\n\n\n"

    pin_col1,pin_row1 = randint(1,len(pin_board[0])-1),randint(1,len(pin_board))
    pin_col2,pin_row2 = randint(1,len(pin_board[0])-1),randint(1,len(pin_board))
    while pin_col1 == pin_col2 and pin_row1 == pin_row2:
        pin_col1,pin_row1 = randint(1,len(pin_board[0])-1),randint(1,len(pin_board))

    time1 = clock() # Initial time check
    print_board(pin_board)

    count = tries = c = temp = remaining = check1 = check2 = fbreak = 0
    
    while 1: # In game...

        tries += 1        
        if tries > 40:
            print "Sorry you LOST! All your 40 tries are over!"
            break        
       
    ## Print out the outputs below by uncommenting
##        print pin_col1
##        print pin_row1 , "\n"
##        print pin_col2
##        print pin_row2 , "\n"

        if game_choice == 1:
            system("title PinPoint (Easy)")
            pin_col,pin_row = pin_col1,pin_row1
        elif game_choice == 3 or game_choice == 2:
            rand = randint(1,2)
            if check1 == 2: # Placing pin2 if pin1 is found
                if game_choice == 2: system("color 0e")
                pin_col,pin_row = pin_col2,pin_row2
            elif check2 == 3:  # Placing pin1 if pin2 is found
                if game_choice == 2: system("color 0d")
                pin_col,pin_row = pin_col1,pin_row1
            elif rand == 1:
                if game_choice == 2: system("color 0d")
                pin_col,pin_row = pin_col1,pin_row1
            elif rand == 2:
                if game_choice == 2: system("color 0e")
                pin_col,pin_row = pin_col2,pin_row2

        print "Enter cordinates to check for pin... Try Number:" , tries , "(" , (41-tries) , "left )"
        while True:
            guess_col,guess_row,fbreak = guess_input()
            if fbreak == 1:
                system("cls")
                break
            if pin_board[guess_row-1][guess_col-1] == "{ }": break
            else: print "That has already been entered before!\n\n"
        if fbreak == 1:
            break

        option = 0 # Later converted to a letter        
#
        if game_choice == 1: # For easy level
            if guess_row == pin_row and guess_col == pin_col:
                time2 = clock() # This is for checking the time after the win! (easy mode)
                system("cls")
                sleep(0.25)
                print "Wow! You have found the pin in" , tries , "tries! You took" , time2 - time1 , "seconds...\n\n"                    
                print_win()
                break
            else:
                option = checking_option_value(pin_row,pin_col,guess_row,guess_col)
                pin_board[guess_row-1][guess_col-1] = option
                system("cls")
            StatementAfterRow(option[1],guess_row,guess_col)

#                
        elif game_choice == 3 or 2: # This is for medium or hard level
            if guess_row == pin_row1 and guess_col == pin_col1:
                pin_board[guess_row-1][guess_col-1] = "{\21}"
                if check2 != 3:                            
                    system("cls")
                    sleep(0.25)
                    print "Wow! You have found a pin in" , tries , "tries!\nYou previously entered [ ROW -" , guess_row , "| COL -" , guess_col , "]\n"
                    print_board(pin_board)
                temp += 1 
                check1 = 2
                if temp != 2:
                    continue 
            elif guess_row == pin_row2 and guess_col == pin_col2:
                pin_board[guess_row-1][guess_col-1] = "{\21}"
                if check1 != 2:
                    system("cls")
                    sleep(0.25)
                    print "Wow! You have found a pin in" , tries , "tries!\nYou previously entered [ ROW -" , guess_row , "| COL -" , guess_col , "]\n"
                    print_board(pin_board)
                temp += 1
                check2 = 3
                if temp != 2:
                    continue 
            if temp == 2:
                time2 = clock() # This is for checking the time after the win! (hard level)
                system("cls")
                sleep(0.25)
                print "Great job you won the game by finding both the pins... You took" , time2 - time1 , "seconds..."
                print_win()
                print 
                break # Game over
#
            else:
                option = checking_option_value(pin_row,pin_col,guess_row,guess_col) # Calling the function to check the value of option...
                pin_board[guess_row-1][guess_col-1] = option

            system("cls")
            sleep(0.25)
            StatementAfterRow(option[1],guess_row,guess_col)
    
        print_board(pin_board)
        

    if raw_input("\nEnter 'E' if you want to exit the window or press enter to play another game: ").upper() == "E":
        break
    print "\n\n\n"
