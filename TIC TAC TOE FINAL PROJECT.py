'''MULTI-MODE TIC TAC TOE GAME WITH SINGLE PLAYER MODE AND DOUBLE PLAYER MODE.
   SINGLE PLAYER MODE HAS THREE LEVEL OPTIONS AND TWO PLAYER MODE HAS OPTIONS TO PLAY
   A SINGLE GAME OR A TOURNAMENT.
'''
#importing random and time function
import random
import time

grid = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] #creating the list for the grid

tournament = [0 , 0 , 0] #creating a list to store the tournament wins and draws


def display_grid(): #creating a function to display the grid
    
    print(format(' ','18s'),grid[1],"|",grid[2],"|",grid[3])
    print(format(' ','18s'),"--+---+--")
    print(format(' ','18s'),grid[4],"|",grid[5],"|",grid[6])
    print(format(' ','18s'),"--+---+--")
    print(format(' ','18s'),grid[7],"|",grid[8],"|",grid[9])


def grid_reset(): #creating a function to reset the grid
    for i in range (1,10):
        grid[i]=i

               
def winning_condition(Player1,Player2,turn): #creating a function to check the winning conditions 

    #checking if any row column or diagonal matched
    #winning condition for player 1
    if (grid[1] == grid[2] == grid[3] == 'x') or (grid[4] == grid[5] == grid[6] == 'x') or (grid[7] == grid[8] == grid[9] == 'x')\
       or (grid[1] == grid[4] == grid[7] == 'x') or (grid[2] == grid[5] == grid[8] == 'x') or (grid[3] == grid[6] == grid[9] == 'x')\
       or (grid[1] == grid[5] == grid[9] == 'x') or (grid[3] == grid[5] == grid[7] == 'x'):        
        print()
        print("----------------",Player1,"wins","-----------------")
        tournament[0] += 1#Adding into the first index of tournament list if Player 1 wins
        return True
    
    #winning condition for player 2 
    elif (grid[1] == grid[2] == grid[3] == 'o') or (grid[4] == grid[5] == grid[6] == 'o') or (grid[7] == grid[8] == grid[9] == 'o')\
         or (grid[1] == grid[4] == grid[7] == 'o') or (grid[2] == grid[5] == grid[8] == 'o') or (grid[3] == grid[6] == grid[9] == 'o')\
         or (grid[1] == grid[5] == grid[9] == 'o') or (grid[3] == grid[5] == grid[7] == 'o'):       
        print()
        print("----------------",Player2,"wins","-----------------")
        tournament[1] += 1 #Adding into the second index of tournament list if Player 2 wins
        return True
    
    #displaying that the game is a draw when turn becomes equal to 9 and no row or column crossed
    elif turn == 9:        
        print()
        print("---------------- It is a draw ------------------")
        tournament[2] += 1 #Adding into the third index of tournament list if it is a draw
        return True

def medium_level(): #creating a function for the conditions of medium level
    # checking all rows, columns and diagonal to see if any winning condition occurs
    if ((grid[2] == grid[3] == 'x') or (grid[4] == grid[7] == 'x') or (grid[5] == grid[9] == 'x')) and (grid[1] != 'x' and grid[1] != 'o'): 
        grid[1] = 'x' #condition to print computer symbol in box 1
        
    elif ((grid[1] == grid[3] == 'x') or (grid[5] == grid[8] == 'x')) and (grid[2] != 'x' and grid[2] != 'o'):
        grid[2] = 'x' #condition to print computer symbol in box 2
        
    elif ((grid[1] == grid[2] == 'x') or (grid[6] == grid[9] == 'x') or (grid[5] == grid[7] == 'x')) and (grid[3] != 'x' and grid[3] != 'o'):
        grid[3] = 'x' #condition to print computer symbol in box 3
        
    elif ((grid[1] == grid[7] == 'x') or (grid[5] == grid[6] == 'x')) and (grid[4] != 'x' and grid[4] != 'o'):
        grid[4] = 'x' #condition to print computer symbol in box 4
        
    elif ((grid[1] == grid[9] == 'x') or (grid[2] == grid[8] == 'x') or (grid[3] == grid[7] == 'x') or (grid[4] == grid[6] == 'x')) and (grid[5] != 'x' and grid[5] != 'o'):
        grid[5] = 'x' #condition to print computer symbol in box 5
        
    elif ((grid[4] == grid[5] == 'x') or (grid[3] == grid[9] == 'x')) and (grid[6] != 'x' and grid[6] != 'o'):
        grid[6] = 'x' #condition to print computer symbol in box 6
        
    elif ((grid[1] == grid[4] == 'x') or (grid[8] == grid[9] == 'x') or (grid[3] == grid[5] == 'x')) and (grid[7] != 'x' and grid[7] != 'o'):
        grid[7] = 'x' #condition to print computer symbol in box 7
        
    elif ((grid[2] == grid[5] == 'x') or (grid[7] == grid[9] == 'x')) and (grid[8] != 'x' and grid[8] != 'o'):
        grid[8] = 'x' #condition to print computer symbol in box 8
        
    elif ((grid[1] == grid[5] == 'x') or (grid[3] == grid[6] == 'x') or (grid[7] == grid[8] == 'x')) and (grid[9] != 'x' and grid[9] != 'o'):
        grid[9] = 'x' #condition to print computer symbol in box 9

    elif ((grid[2] == grid[3] == 'o') or (grid[4] == grid[7] == 'o') or (grid[5] == grid[9] == 'o')) and (grid[1] != 'x' and grid[1] != 'o'):
        grid[1] = 'x' #condition to print computer symbol in box 1

    elif ((grid[1] == grid[3] == 'o') or (grid[5] == grid[8] == 'o')) and (grid[2] != 'x' and grid[2] != 'o'):
        grid[2] = 'x' #condition to print computer symbol in box 2

    elif ((grid[1] == grid[2] == 'o') or (grid[6] == grid[9] == 'o') or (grid[5] == grid[7] == 'o')) and (grid[3] != 'x' and grid[3] != 'o'):
        grid[3] = 'x' #condition to print computer symbol in box 3

    elif ((grid[1] == grid[7] == 'o') or (grid[5] == grid[6] == 'o')) and (grid[4] != 'x' and grid[4] != 'o'):
        grid[4] = 'x' #condition to print computer symbol in box 4

    elif ((grid[1] == grid[9] == 'o') or (grid[2] == grid[8] == 'o') or (grid[3] == grid[7] == 'o') or (grid[4] == grid[6] == 'o')) and (grid[5] != 'x' and grid[5] != 'o'):
        grid[5] = 'x' #condition to print computer symbol in box 5

    elif ((grid[4] == grid[5] == 'o') or (grid[3] == grid[9] == 'o')) and (grid[6] != 'x' and grid[6] != 'o'):
        grid[6] = 'x' #condition to print computer symbol in box 6

    elif ((grid[1] == grid[4] == 'o') or (grid[8] == grid[9] == 'o') or (grid[3] == grid[5] == 'o')) and (grid[7] != 'x' and grid[7] != 'o'):
        grid[7] = 'x' #condition to print computer symbol in box 7

    elif ((grid[2] == grid[5] == 'o') or (grid[7] == grid[9] == 'o')) and (grid[8] != 'x' and grid[8] != 'o'):
        grid[8] = 'x' #condition to print computer symbol in box 8

    elif ((grid[1] == grid[5] == 'o') or (grid[3] == grid[6] == 'o') or (grid[7] == grid[8] == 'o')) and (grid[9] != 'x' and grid[9] != 'o'):
        grid[9] = 'x' #condition to print computer symbol in box 9

    else:
        box = random.randint(1,9) #randomly selecting the box number                    
        while grid[box] == 'x' or grid[box] == 'o': #restricting the computer from selecting the occupied box number
            box = random.randint(1,9) 
        grid[box] = 'x'

def two_player_game(): #creating a function for the two player game

    #Prompt the user to choose the desired option
    print()
    print(" --> Press 's' to play a SINGLE GAME\n --> Press 't' to play a TOURNAMENT: ")
    print()
    tournament_choice = input("Enter your choice: ")
    while tournament_choice != 's' and tournament_choice != 't':
        print()
        print ("INVALID INPUT")
        tournament_choice = input("Enter a valid option: ") #restricting the player from choosing wroing option
    print()         
    Player1 = input("Enter your name PLAYER 1: ") #prompt the first player to enter the name
    Player1_symbol = 'x'
    print("Your symbol is '",Player1_symbol,"'") #assigning the symbol
    print()
    Player2 = input("Enter your name PLAYER 2: ") #prompt the second player to enter the name
    Player2_symbol = 'o'
    print("Your symbol is '",Player2_symbol,"'") #assigning the symbol
    print()

    #TOSS
    print("--------------------- TOSS ---------------------") 
    toss = random.randint(0,1) 
    print()

    if toss == 0: #when player 1 wins the toss
        winner = Player1 #Assigning player 1 name to variable winner
        second_player = Player2 #Assigning player 2 name to variable second_player
        print(winner,"wins the toss")
                   
        winner_symbol = Player1_symbol #Assigning player 1 symbol to variable winner_symbol
        other_symbol = Player2_symbol  #Assigning player 2 symbol to variable other_symbol
   
    elif toss == 1: #when player 2 wins the toss
        winner = Player2 #Assigning player 2 name to variable winner
        second_player = Player1 #Assigning player 1 name to variable second_player
        print(winner,"wins the toss")
                        
        winner_symbol = Player2_symbol #Assigning player 2 symbol to variable winner_symbol
        other_symbol = Player1_symbol  #Assigning player 1 symbol to variable other_symbol
        
    print()
    #running th double player game one time if user chooses to play a single game
    if tournament_choice == 's':
        print("--------------------- START --------------------")
        double_player(winner,winner_symbol,second_player,other_symbol,Player1,Player2) #calling the double_player function

    #running th double player game 6 times if user chooses to play a tournament    
    elif tournament_choice == 't':
        print("--------------- TOURNAMENT BEGINS --------------")

        for i in range(0,3): #resting the tournament list
            tournament[i] = 0

        for game in range (1,7): #running the loop 6 times
            print()
            print(format(' ','18s'),"( GAME",game,")") #printing the number of current game
            grid_reset() #reseting the grid after each game
            double_player(winner,winner_symbol,second_player,other_symbol,Player1,Player2) #calling the double_player function

        print()
        print(format(' ','15s'),"( SCORE BOARD )") #printing the score board after the tournament ends
        print()
        print(Player1,"wins: ",tournament[0]) #player 1 wins
        print(Player2,"wins: ",tournament[1]) #player 2 wins
        print("      Draw: ",tournament[2]) # number of draws in the tournament
        print()

        if tournament[0] > tournament[1]: ##showing the winner of the tournament
            print("--------",Player1,"wins the tournament","--------")
        elif tournament[0] < tournament[1]:
            print("--------",Player2,"wins the tournament","--------")
        else:
            print("------------- Tournament is a draw -------------") #printing draw if number of wins are equal
            

def double_player(winner,winner_symbol,second_player,other_symbol,Player1,Player2): #creating a function for the running the turns in double player game
    
    print()
    display_grid()
    #running the loop till the length of the grid
    for turn in range(1,len(grid)):
        print()
        
        #condition for the turn of the toss winner        
        if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:            
            print(winner,"it's your turn")
            box = eval(input("Please enter the box number: "))

            #restricting the player from choosing an already occupied box number            
            while grid[box] == 'x' or grid[box] == 'o':
                print()
                print("This box is already occupied")
                box = eval(input("please enter another box number: "))
               
            grid[box] = winner_symbol #printing the symbol of player in the grid box chosen by the player 

        
        #condition for the turn of the other player 
        elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
            print(second_player,"it's your turn")
            box = eval(input("please enter the box number: "))

            #restricting the player from choosing an already occupied box number
            while grid[box] == 'x' or grid[box] == 'o':
                print()
                print("This box is already occupied")
                box = eval(input("Please enter another box number: "))
               
            grid[box] = other_symbol #printing the symbol of player in the box chosen bye the player 
                
        print()
        display_grid() #Printing the grid after each turn by calling the display_grid function
            
        #checking winning condition by calling the winning_condition function
        check = winning_condition(Player1,Player2,turn)
        #ending the game if the condition is true or continuing it if the condition is false
        if check == True:
            break
        else:
            continue 
    

def single_player_game(): #creating a function for the single player game
    
    print()
    print(" --> Press '1' to play EASY LEVEL\n --> Press '2' to play MEDIUM LEVEL\n --> Press '3' to play HARD LEVEL")
    print()
    level = eval(input("Enter your choice: ")) #Asking the user to choose the level
    while level != 1 and level != 2 and level != 3:
        print()
        print ("INVALID INPUT")
        level = input("Enter a valid option: ")
    print()
    if level == 1:
        print("------------------ EASY LEVEL ------------------")
    elif level == 2:
        print("----------------- MEDIUM LEVEL -----------------")
    elif level == 3:
        print("------------------ HARD LEVEL ------------------")
        
    Player1 = 'Computer'
    print()
    Player2 = input("Enter your name: ") #Taking name input from user
    Player2_symbol = 'o'
    print("Your symbol is '",Player2_symbol,"'") #assigning symbol to the user
    print()
    print("Symbol for computer is 'x'")
    
    print()
    print("---------------------- TOSS --------------------")
    toss = random.randint(0,1) #making the toss

    #printing the name of the toss winner
    print()
    if toss == 0:
        print("Computer wins the toss")
    elif toss == 1:
        print(Player2,"wins the toss")
    
    print()
    print("--------------------- START --------------------") #start of the game
    print()
    display_grid() #calling the display_grid function

    #EASY LEVEL    
    if level == 1:        
        for turn in range(1,len(grid)): #running the loop till the length of the list grid
            #delays the execution of each turn for 0.5 second
            time.sleep(0.5)
            print()
            
            #conditions when computer wins the toss
            if toss == 0:
                #condition for the turn of computer
                if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                    print("It's computer's turn")
                    box = random.randint(1,9) #randomly selecting the box number
                    
                    while grid[box]=='x' or grid[box]=='o': #restricting the computer from selecting the occupied box number
                        box = random.randint(1,9) 
                    grid[box] = 'x'
                
                #condition for the turn of the user 
                elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                    print(Player2,"it's your turn")
                    box = eval(input("please enter the box number: ")) #taking input from the user
                    
                    while grid[box] == 'x' or grid[box] == 'o': #restricting the player from selecting the occupied box number
                        print()
                        print("This box is already occupied")
                        box=eval(input("please enter another box number: "))
                                             
                    grid[box] = 'o' #printing the symbol of player in the box chosen bye the player  

            #conditions when user wins the toss
            if toss == 1:
                #condition for the turn of the user
                if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                    print(Player2,"it's your turn")
                    box = eval(input("please enter the box number: ")) #taking input from user

                    while grid[box] == 'x' or grid[box] == 'o':  #restricting the player from selecting the occupied box number
                        print()
                        print("This box is already occupied")
                        box=eval(input("please enter another box number: "))                            

                    grid[box] = 'o' #printing the symbol of player in the box chosen bye the player
                
                #condition for the turn of computer 
                elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                    print("It's computer's turn")                    
                    box = random.randint(1,9) #randomly selecting the box number
                    
                    while grid[box]=='x' or grid[box]=='o': #restricting the computer from selecting the occupied box number
                        box = random.randint(1,9)
                    grid[box] = 'x'

            print()
            display_grid() #printing the symbol of player in the box chosen by the player  

            #checking winning condition by calling the winning_condition function
            check = winning_condition(Player1,Player2,turn)
            #ending the game if the condition is true or continuing it if the condition is false
            if check == True:
                break
            else:
                continue

    #MEDIUM LEVEL
    if level == 2:
        for turn in range(1,len(grid)): #running the loop till the length of the list grid
            time.sleep(0.5) #delays the execution of each turn for 0.5 second
            print()
            if toss == 0:
                if turn == 2 or turn ==4 or turn == 6 or turn == 8:
                    print(Player2,"it's your turn")
                    box = eval(input("please enter the box number: ")) #taking input from user

                    while grid[box] == 'x' or grid[box] == 'o':  #restricting the player from selecting the occupied box number
                        print()
                        print("This box is already occupied")
                        box=eval(input("please enter another box number: "))                            

                    grid[box] = 'o' #printing the symbol of player in the box chosen bye the player

                elif turn ==1 or turn == 3 or turn == 5 or turn == 7 or turn == 9:
                    print("It's computer's turn")
                    medium_level()

            if toss == 1:
                if turn == 1 or turn == 3 or turn == 5 or turn == 7 or turn ==9:
                    print(Player2,"it's your turn")
                    box = eval(input("please enter the box number: ")) #taking input from user

                    while grid[box] == 'x' or grid[box] == 'o':  #restricting the player from selecting the occupied box number
                        print()
                        print("This box is already occupied")
                        box=eval(input("please enter another box number: "))                            

                    grid[box] = 'o' #printing the symbol of player in the box chosen bye the player

                elif turn == 2 or turn == 4 or turn == 6 or turn == 8:
                    print("It's computer's turn")
                    medium_level()

            print()
            display_grid() #printing the symbol of player in the box chosen by the player  

            #checking winning condition by calling the winning_condition function
            check = winning_condition(Player1,Player2,turn)
            #ending the game if the condition is true or continuing it if the condition is false
            if check == True:
                break
            else:
                continue
                    

    
    # HARD LEVEL
    if level == 3:
        for turn in range(1,len(grid)): #running the loop till the length of the list grid
            time.sleep(0.5) #delays the execution of each turn for 0.5 second
            print()

            if toss == 0: #conditions when computer wins the toss

                if turn == 1: #when turn is 1
                    print("It's computer's turn")
                    turn1 = 1
                    grid[1] = "x" #printing the symbol in the grid
   
                elif turn == 2: #when turn is 2 
                    print(Player2,"it's your turn")
                    turn2 = eval(input("Please enter the box number:")) #taking turn input from the player

                    while grid[turn2] == 'x' or turn2 == 'o': #restricting the player from choosing an already occupied box number
                        print() 
                        print("This box is already occupied")
                        turn2 = eval(input("Please enter another box number:"))
                    
                    grid[turn2] = 'o' #printing the symbol in the grid
            
                elif turn == 3:  #when turn is 3
                    print("Its's computer's turn")
                    if turn2 == 3 or turn2 == 5:
                        turn3 = 9
                        grid[9] = "x"
                    else:
                        turn3 = 3
                        grid[3] = "x"
                        
                elif turn == 4: #when turn is 4
                    print(Player2,"it's your turn")
                    turn4 = eval(input("please enter the box number:")) #taking turn input from the player

                    while grid[turn4] == 'x' or grid[turn4] == 'o': #restricting the player from choosing an already occupied box number
                        print()
                        print("This box is already occupied")
                        turn4 = eval(input("please enter another box number:"))
                    
                    grid[turn4] = 'o' #printing the symbol in the grid

                
                elif turn == 5: #when turn is 5
                    print("Its's computer's turn")
                    if turn2 == 2:
                        if turn4 == 4 or turn4 == 7:
                            turn5 = 9
                            grid[9] = 'x'
                        elif turn4 == 5:
                            turn5 = 8
                            grid[8] = 'x'
                        elif turn4 == 6 or turn4 == 9:
                            turn5 = 7
                            grid[7] = 'x'
                        elif turn4 == 8:
                            turn5 = 5
                            grid[5] = 'x'

                    elif turn2 == 3:
                        if turn4 == 5:
                            turn5 = 7
                            grid[7] = 'x'
                        else:
                            turn5 = 5
                            grid[5] = 'x'

                    elif turn2 == 4 or turn2 == 7:
                        if turn4 == 2:
                            turn5 = 9
                            grid[9] = 'x'
                        else:
                            turn5 = 2
                            grid[2] = 'x'

                    elif turn2 == 5:
                        if turn4 == 2:
                            turn5 = 8
                            grid[8] = 'x'
                        elif turn4 == 3:
                            turn5 = 7
                            grid[7] = 'x'
                        elif turn4 == 4:
                            turn5 = 6
                            grid[6] = 'x'
                        elif turn4 == 6:
                            turn5 = 4
                            grid[4] = 'x'
                        elif turn4 == 7:
                            turn5 = 3
                            grid[3] = 'x'
                        elif turn4 == 8:
                            turn5 = 2
                            grid[2] = 'x'

                    elif turn2 == 6 or turn2 == 9:
                        if turn4 == 2:
                            turn5 = 7
                            grid[7] = 'x'
                        else:
                            turn5 = 2
                            grid[2] = 'x'

                    elif turn2 == 8:
                        if turn4 == 2:
                            turn5 = 5
                            grid[5] = 'x'
                        else:
                            turn5 = 2
                            grid[2] = 'x'
                          
                elif turn == 6: #when turn is 6 
                    print(Player2,"it's your turn")
                    turn6 = eval(input("please enter the box number:")) #taking turn input from the player

                    while grid[turn6] == 'x' or grid[turn6] == 'o': #restricting the player from choosing an already occupied box number
                        print()
                        print("This box is already occupied")
                        turn6 = eval(input("please enter another box number:"))
                    
                    grid[turn6] = 'o' #printing the symbol in the grid
                        
                elif turn == 7: #when turn is 7
                    print("Its's computer's turn")
                    if turn2 == 2 and (turn4 == 4 or turn4 == 7):
                        if turn6 == 4 or turn6 == 5 or turn6 == 7 or turn6 == 8:
                            turn7 = 6
                            grid[6] = 'x'
                        else:
                            turn7 = 5
                            grid[5] = 'x'
                    elif turn2 == 2 and (turn4 == 6 or turn4 == 9):
                        if turn6 == 5 or turn6 == 6 or turn6 == 8 or turn6 == 9:
                            turn7 = 4
                            grid[4] = 'x'
                        else:
                            turn7 = 5
                            grid[5] = 'x'
                    elif turn2 == 2 and turn4 == 5:
                        if turn6 == 4 or turn6 == 7:
                            turn7 = 6
                            grid[6] = 'x'
                        elif turn6 == 6 or turn6 == 9:
                            turn7 = 4
                            grid[4] = 'x'
                    elif turn2 == 2 and turn4 == 8:
                        if turn6 == 4 or turn6 == 6 or turn6 == 7:
                            turn7 = 9
                            grid[9] = 'x'
                        else:
                            turn7 = 7
                            grid[7] = 'x'
                            
                    elif turn2 == 3 and turn4 == 5:
                        if turn6 == 2 or turn6 == 4 or turn6 == 6:
                            turn7 = 8
                            grid[8] = 'x'
                        else:
                            turn7 = 4
                            grid[4] = 'x'

                    elif (turn2 == 4 or turn2 == 7) and turn4 == 2:
                        if turn6 == 4 or turn6 == 5 or turn6 == 7 or turn6 == 8:
                            turn7 = 6
                            grid[6] = 'x'
                        else:
                            turn7 = 5
                            grid[5] = 'x'

                    elif turn2 == 5 and turn4 == 2:
                        if turn6 == 3:
                            turn7 = 7
                            grid[7] = 'x'
                        elif turn6 == 4:
                            turn7 = 6
                            grid[6] = 'x'
                        elif turn6 == 6:
                            turn7 = 4
                            grid[4] = 'x'
                        elif turn6 == 7:
                            turn7 = 3
                            grid[3] = 'x'
                    elif turn2 == 5 and turn4 == 3:
                        if turn6 == 2 or turn6 == 4 or turn6 == 6:
                            turn7 = 8
                            grid[8] = 'x'
                        else:
                            turn7 = 4
                            grid[4] = 'x'
                    elif turn2 == 5 and turn4 == 4:
                        if turn6 == 2 or turn6 == 7 or turn6 == 8:
                            turn7 = 3
                            grid[3] = 'x'
                        else:
                            turn7 = 7
                            grid[7] = 'x'
                    elif turn2 == 5 and turn4 == 6:
                        if turn6 == 2 or turn6 == 3 or turn6 == 8:
                            turn7 = 7
                            grid[7] = 'x'
                        else:
                            turn7 = 3
                            grid[3] = 'x'
                    elif turn2 == 5 and turn4 == 7:
                        if turn6 == 2 or turn6 == 4 or turn6 == 8:
                            turn7 = 6
                            grid[6] = 'x'
                        else:
                            turn7 = 2
                            grid[2] = 'x'
                    elif turn2 == 5 and turn4 == 8:
                        if turn6 == 3:
                            turn7 = 7
                            grid[7] = 'x'
                        else:
                            turn7 = 3
                            grid[3] = 'x'
                    elif (turn2 == 6 or turn2 == 9) and turn4 == 2:
                        if turn6 == 4 or turn6 == 6 or turn6 == 8 or turn6 == 9:
                            turn7 = 5
                            grid[5] = 'x'
                        else:
                            turn7 = 4
                            grid[4] = 'x'
                    elif turn2 == 8 and turn4 == 2:
                        if turn6 == 4 or turn6 == 6 or turn6 == 7:
                            turn7 = 9
                            grid[9] = 'x'
                        else:
                            turn7 = 7
                            grid[7] = 'x'

                elif turn == 8: #when turn is 8
                    print(Player2,"it's your turn")
                    turn8 = eval(input("please enter the box number:")) #taking turn input from the player

                    while grid[turn8] == 'x' or grid[turn8] == 'o': #restricting the player from choosing an already occupied box number
                        print()
                        print("This box is already occupied")
                        turn8 = eval(input("please enter another box number:"))
                    
                    grid[turn8] = 'o' #printing the symbol in the grid

                
                elif turn == 9: #when turn is 9
                    print("Its's computer's turn")
                    for i in range(1,len(grid)): #printing computer symbol in the last left box
                        if grid[i] == i:
                            grid[i] = 'x'

                                
            if toss == 1:  #conditions when user wins the toss
                    if turn == 1: #when turn is 1
                        print(Player2,"it's your turn")
                        turn1 = eval(input("please enter the box number:")) #taking turn input from the player
                        grid[turn1] = 'o' #printing the symbol in the grid

                    elif turn == 2: #when turn is 2
                        print("It's computer's turn")
                        if turn1 == 5:
                            turn2 = 1
                            grid[1] = 'x'
                        else:
                            turn2 = 5
                            grid[5] = 'x'

                    elif turn == 3:  #when turn is 3
                        print(Player2,"it's your turn")
                        turn3 = eval(input("please enter the box number:"))  #when turn is 3

                        while grid[turn3] == 'x' or grid[turn3] == 'o': #restricting the player from choosing an already occupied box number
                            print()
                            print("This box is already occupied")
                            turn3 = eval(input("please enter another box number:"))
                        
                        grid[turn3] = 'o' #printing the symbol in the grid

                    elif turn == 4: #when turn is 4
                        print("It's computer's turn")
                        if turn1 == 1:
                            if turn3 == 2:
                                turn4 = 3
                                grid[3] = 'x'
                            elif turn3 == 3 or turn3 == 6 or turn3 == 9:
                                turn4 = 2
                                grid[2] = 'x'
                            elif turn3 == 4 or turn3 == 8:
                                turn4 = 7
                                grid[7] = 'x'
                            elif turn3 == 7:
                                turn4 = 4
                                grid[4] = 'x'

                        elif turn1 == 2:
                            if turn3 == 1 or turn3 == 9:
                                turn4 = 3
                                grid[3] = 'x'
                            else:
                                turn4 = 1
                                grid[1] = 'x'

                        elif turn1 == 3:
                            if turn3 == 1 or turn3 == 7:
                                turn4 = 2
                                grid[2] = 'x'
                            elif turn3 == 2 or turn3 == 4:
                                turn4 = 1
                                grid[1] = 'x'
                            elif turn3 == 6 or turn3 == 8:
                                turn4 = 9
                                grid[9] = 'x'
                            elif turn3 == 9:
                                turn4= 6
                                grid[6] = 'x'

                        elif turn1 == 4:
                            if turn3 == 1:
                                turn4 = 7
                                grid[7] = 'x'
                            elif turn3 == 9:
                                turn4 = 2
                                grid[2] = 'x'
                            else:
                                turn4 = 1
                                grid[1] = 'x'

                        elif turn1 == 5:
                            if turn3 == 2:
                                turn4 = 8
                                grid[8] = 'x'
                            elif turn3 == 3:
                                turn4 = 7
                                grid[7] = 'x'
                            elif turn3 == 4:
                                turn4 = 6
                                grid[6] = 'x'
                            elif turn3 == 6:
                                turn4 = 4
                                grid[4] = 'x'
                            elif turn3 == 7 or turn3 == 9:
                                turn4 = 3
                                grid[3] = 'x'
                            elif turn3 == 8:
                                turn4 = 2
                                grid[2] = 'x'

                        elif turn1 == 6:
                            if turn3 == 1 or turn3 == 7:
                                turn4 = 2
                                grid[2] = 'x'
                            elif turn3 == 3 or turn3 == 8:
                                turn4 = 9
                                grid[9] = 'x'
                            elif turn3 == 2 or turn3 == 4:
                                turn4 = 1
                                grid[1] = 'x'
                            elif turn3 == 9:
                                turn4 = 3
                                grid[3] = 'x'

                        elif turn1 == 7:
                            if turn3 == 1:
                                turn4 = 4
                                grid[4] = 'x'
                            elif turn3 == 3 or turn3 == 6:
                                turn4 = 2
                                grid[2] = 'x'
                            elif turn3 == 2 or turn3 == 4:
                                turn4 = 1
                                grid[1] = 'x'
                            elif turn3 == 8:
                                turn4 = 9
                                grid[9] = 'x'
                            elif turn3 == 9:
                                turn4 = 8
                                grid[8] = 'x'

                        elif turn1 == 8:
                            if turn3 == 1 or turn3 == 9:
                                turn4 = 7
                                grid[7] = 'x'
                            elif turn3 == 2 or turn3 == 4:
                                turn4 = 1
                                grid[1] = 'x'
                            elif turn3 == 3 or turn3 == 6 or turn3 == 7:
                                turn4 = 9
                                grid[9] = 'x'
                            
                        elif turn1 == 9:
                            if turn3 == 1 or turn3 == 4:
                                turn4 = 2
                                grid[2] = 'x'
                            elif turn3 == 2 or turn3 == 6:
                                turn4 = 3
                                grid[3] = 'x'
                            elif turn3 == 3:
                                turn4 = 6
                                grid[6] = 'x'
                            elif turn3 == 7:
                                turn4 = 8
                                grid[8] = 'x'
                            elif turn3 == 9:
                                turn4 = 7
                                grid[7] = 'x'
                       
                    elif turn == 5: #when turn is 5
                        print(Player2,"it's your turn")
                        turn5 = eval(input("please enter the box number:")) #taking turn input from the player

                        while grid[turn5] == 'x' or grid[turn5] == 'o': #restricting the player from choosing an already occupied box number
                            print()
                            print("This box is already occupied")
                            turn5 = eval(input("please enter another box number:"))
                        
                        grid[turn5] = 'o' #printing the symbol in the grid

                    
                    elif turn == 6: #when turn is 6
                        print("It's computer's turn")
                        if turn1 == 5 and turn3 == 2:
                            if turn5 == 3:
                                turn6 = 7
                                grid[7] = 'x'
                            elif turn5 == 4:
                                turn6 = 6
                                grid[6] = 'x'
                            elif turn5 == 6 or turn5 == 9:
                                turn6 = 4
                                grid[4] = 'x'
                            elif turn5 == 7:
                                turn6 = 3
                                grid[3] = 'x'

                        elif turn1 == 5 and turn3 == 3:
                            if turn5 == 4:
                                turn6 = 6
                                grid[6] = 'x'
                            else:
                                turn6 = 4
                                grid[4] = 'x'

                        elif turn1 == 5 and turn3 == 4:
                            if turn5 == 2:
                                turn6 = 8
                                grid[8] = 'x'
                            elif turn5 == 3:
                                turn6 = 7
                                grid[7] = 'x'
                            elif turn5 == 7:
                                turn6 = 3
                                grid[3] = 'x'
                            elif turn5 == 8 or turn5 == 9:
                                turn6 = 2
                                grid[2] = 'x'

                        elif turn1 == 5 and turn3 == 6:
                            if turn5 == 7:
                                turn6 = 3
                                grid[3] = 'x'
                            else:
                                turn6 = 7
                                grid[7] = 'x'

                        elif turn1 == 5 and (turn3 == 7 or turn3 == 9):
                            if turn5 == 2:
                                turn6 = 8
                                grid[8] = 'x'
                            else:
                                turn6 = 2
                                grid[2] = 'x'

                        elif turn1 == 5 and turn3 == 8:
                            if turn5 == 3:
                                turn6 = 7
                                grid[7] = 'x'
                            else:
                                turn6 = 3
                                grid[3] = 'x'

                        elif (turn1 == 1 and turn3 == 2) or (turn1 == 2 and turn3 == 1):
                            if turn5 == 7:
                                turn6 = 4
                                grid[4] = 'x'
                            else:
                                turn6 = 7
                                grid[7] = 'x'

                        elif (turn1 == 1 and turn3 == 3) or (turn1 == 3 and turn3 == 1):
                            if turn5 == 8:
                                turn6 = 4
                                grid[4] = 'x'
                            else:
                                turn6 = 8
                                grid[8] = 'x'

                        elif (turn1 == 1 and (turn3 == 4 or turn3 == 8)) or ((turn1 == 4 or turn1 == 8) and turn3 == 1):
                            if turn5 == 3:
                                turn6 = 2
                                grid[2] = 'x'
                            else:
                                turn6 = 3
                                grid[3] = 'x'

                        elif (turn1 == 1 and (turn3 == 6 or turn3 == 9))or((turn1 == 6 or turn1 == 9) and turn3 == 1)or(turn1 == 9 and turn3 == 4) or (turn1 == 4 and turn3 == 9):
                            if turn5 == 8:
                                turn6 = 7
                                grid[7] = 'x'
                            else:
                                turn6 = 8
                                grid[8] = 'x'

                        elif (turn1 == 1 and turn3 == 7) or (turn1 == 7 and turn3 == 1):
                            if turn5 == 6:
                                turn6 = 2
                                grid[2] = 'x'
                            else:
                                turn6 = 6
                                grid[6] = 'x'

                        elif ((turn1 == 2 or turn1 == 4) and turn3 == 3) or (turn1 == 3 and (turn3 == 2 or turn3 == 4)):
                            if turn5 == 9:
                                turn6 = 6
                                grid[6] = 'x'
                            else:
                                turn6 = 9
                                grid[9] = 'x'

                        elif (turn1 == 2 and (turn3 == 4 or turn3 == 8))or((turn1 == 4 or turn1 == 8) and turn3 ==2 )or(turn1 == 4 and turn3 == 8) or (turn1 == 8 and turn3 == 4):
                            if turn5 == 9:
                                turn6 = 7
                                grid[7] = 'x'
                            else:
                                turn6 = 9
                                grid[9] = 'x'

                        elif ((turn1 == 2 or turn1 == 4) and turn3 == 6) or (turn1 == 6 and (turn3 == 2 or turn3 == 4)):
                            if turn5 == 9:
                                turn6 = 3
                                grid[3] = 'x'
                            else:
                                turn6 = 9
                                grid[9] = 'x'

                        elif ((turn1 == 2 or turn1 == 4) and turn3 == 7) or (turn1 == 7 and (turn3 == 2 or turn3 == 4)):
                            if turn5 == 9:
                                turn6 = 8
                                grid[8] = 'x'
                            else:
                                turn6 = 9
                                grid[9] = 'x'

                        elif ((turn1 == 2 or turn1 == 6) and turn3 == 9) or (turn1 == 9 and (turn3 == 2 or turn3 == 6)):
                            if turn5 == 7:
                                turn6 = 8
                                grid[8] = 'x'
                            else:
                                turn6 = 7
                                grid[7] = 'x'

                        elif (turn1 == 3 and (turn3 == 6 or turn3 == 8)) or ((turn1 == 6 or turn1 == 8) and turn3 == 3):
                            if turn5 == 1:
                                turn6 = 2
                                grid[2] = 'x'
                            else:
                                turn6 = 1
                                grid[1] = 'x'

                        elif ((turn1 == 3 or turn1 == 6) and turn3 == 7) or (turn1 == 7 and (turn3 == 3 or turn3 == 6)):
                            if turn5 == 8:
                                turn6 = 9
                                grid[9] = 'x'
                            else:
                                turn6 = 8
                                grid[8] = 'x'

                        elif (turn1 == 3 and turn3 == 9) or (turn1 == 9 and turn3 == 3):
                            if turn5 == 4:
                                turn6 = 2
                                grid[2] = 'x'
                            else:
                                turn6 = 4
                                grid[4] = 'x'

                        elif (turn1 == 6 and turn3 == 8) or (turn1 == 8 and turn3 == 6):
                            if turn5 == 1:
                                turn6 = 3 
                                grid[3] = 'x'
                            else:
                                turn6 = 1
                                grid[1] = 'x'

                        elif (turn1 == 7 and turn3 == 8) or (turn1 == 8 and turn3 == 7):
                            if turn5 == 1:
                                turn6 = 4
                                grid[4] = 'x'
                            else:
                                turn6 = 1
                                grid[1] = 'x'

                        elif (turn1 == 7 and turn3 == 9) or (turn1 == 9 and turn3 == 7):
                            if turn5 == 2:
                                turn6 = 4
                                grid[4] = 'x'
                            else:
                                turn6 = 2
                                grid[2] = 'x'

                        elif (turn1 == 8 and turn3 == 9) or (turn1 == 9 and turn3 == 8):
                            if turn5 == 3:
                                turn6 = 6
                                grid[6] = 'x'
                            else:
                                turn6 = 3
                                grid[3] = 'x'
                   
                    elif turn == 7: #when turn is 7
                        print(Player2,"it's your turn")
                        turn7 = eval(input("please enter the box number:")) #taking turn input from the player

                        while grid[turn7] == 'x' or grid[turn7] == 'o': #restricting the player from choosing an already occupied box number
                            print()
                            print("This box is already occupied")
                            turn7 = eval(input("please enter another box number:"))
                        
                        grid[turn7] = 'o' #printing the symbol in the grid

                    elif turn == 8: #when turn is 8
                        print("It's computer's turn")
                        if turn1 == 5:
                            if turn3 == 2 and turn5 == 3:
                                if turn7 == 4:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif (turn3 == 2 and turn5 == 4) or (turn3 == 4 and turn5 == 2) or (turn3 == 4 and (turn5 == 8 or turn5 == 9)):
                                if turn7 == 3:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif (turn3 == 2 and (turn5 == 6 or turn5 == 9)):
                                if turn7 == 7:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            if (turn3 == 2 and turn5 == 7) or ((turn3 == 7 or turn3 == 9) and turn5 == 2) or (turn3 == 8 and turn5 == 3): 
                                if turn7 == 4:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif (turn3 == 3 and turn5 == 4) or (turn3 == 4 and turn5 == 3) or (turn3 == 6 and turn5 == 7):
                                if turn7 == 2:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif (turn3 == 4 and turn5 == 7):
                                if turn7 == 9:
                                    turn8 = 2
                                    grid[2] = 'x'
                                else:
                                    turn8 = 9
                                    grid[9] = 'x'

                        elif turn1==1:
                            if turn3 == 2 and turn5 == 7:
                                if turn7 == 6:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif (turn3 == 3 and turn5 == 8) or (turn3 == 8 and turn5 == 3):
                                if turn7 == 6:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif turn3 == 4 and turn5 == 3:
                                if turn7 == 8:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 6 and turn5 == 8:
                                if turn7 == 3:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 7 and turn5 == 6:
                                if turn7 == 8:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 9 and turn5 == 8:
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                        elif turn1 == 2:
                            if turn3 == 1 and turn5 == 7:
                                if turn7 == 6:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif turn3 == 3 and turn5 == 9:
                                if turn7 == 4:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif ((turn3 == 4 or turn3 == 7) and turn5 == 9):
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 6 and turn5 == 9:
                                if turn7 == 7:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            elif turn3 == 8 and turn5 == 9:
                                if turn7 == 4:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif turn3 == 9 and turn5 == 7:
                                if turn7 == 1:
                                    turn8 = 4
                                    grid[4]='x'
                                else:
                                    turn8 = 1
                                    grid[1] = 'x'

                        elif turn1 == 3:
                            if turn3 == 1 and turn5 == 8:
                                if turn7 == 6:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif (turn3 == 2 and turn5 == 9) or (turn3 == 8 and turn5 == 1):
                                if turn7 == 4:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif turn3 == 4 and turn5 == 9:
                                if turn7 == 7:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            elif turn3 == 6 and turn5 == 1:
                                if turn7 == 8:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 7 and turn5 == 8:
                                if turn7 == 1:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 1 
                                    grid[1] = 'x'

                            elif turn3 == 9 and turn5 == 4:
                                if turn7 == 8:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                        elif turn1 == 4:
                            if turn3 == 1 and turn5 == 3:
                                if turn7 == 8:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 2 and turn5 == 9:
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 3 and turn5 == 9:
                                if turn7 == 7:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            elif turn3 == 6 and turn5 == 9:
                                if turn7 == 2:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif turn3 == 7 and turn5 == 9:
                                if turn7 == 2:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif (turn3 == 8 and turn5 == 9) or (turn3 == 9 and turn5 == 8):
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                        elif turn1 == 6:
                            if turn3 == 1 and turn5 == 8:
                                if turn7 == 3:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 2 and turn5 == 9:
                                if turn7 == 7:
                                    turn8 = 8
                                    grid[8] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'
                                    
                            elif turn3 == 3 and turn5 == 1:
                                if turn7 == 8:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 4 and turn5 == 9:
                                if turn7 == 2:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif turn3 == 7 and turn5 == 1:
                                if turn7 == 1:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 1
                                    grid[1] = 'x'

                            elif turn3 == 8 and turn5 == 1:
                                if turn7 == 7:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            elif turn3 == 9 and turn5 == 7:
                                if turn7 == 2:
                                    turn8 = 1
                                    grid[1] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                        elif turn1 == 7:
                            if turn3 == 1 and turn5 == 6:
                                if turn7 == 8:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 2 and turn5 == 9:
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif (turn3 == 3 or turn3 == 6) and turn5 == 8:
                                if turn7 == 1:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 1
                                    grid[1] = 'x'

                            elif turn3 == 4 and turn5 == 9:
                                if turn7 == 2:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif (turn3 == 8 and turn5 == 1) or (turn3 == 9 and turn5 == 2):
                                if turn7 == 6:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                        elif turn1 == 8:
                            if turn3 == 1 and turn5 == 3:
                                if turn7 == 6:
                                    turn8 = 9
                                    grid[9] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif turn3 == 2 and turn5 == 9:
                                if turn7 == 3:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'
                                    
                            elif turn3 == 3 and turn5 == 1:
                                if turn7 == 4:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                            elif turn3 == 4 and turn5 == 9:
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 6 and turn5 == 1:
                                if turn7 == 7:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 7
                                    grid[7] = 'x'

                            elif turn3 == 7 and turn5 == 1:
                                if turn7 == 6:
                                    turn8 = 2
                                    grid[2] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif turn3 == 9 and turn5 == 7:
                                if turn7 == 4:
                                    turn8 = 1
                                    grid[1] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                        elif turn1 == 9:
                            if (turn3 == 1 or turn3 == 4) and turn5 == 8:
                                if turn7 == 3:
                                    turn8 = 6
                                    grid[6] = 'x'
                                else:
                                    turn8 = 3
                                    grid[3] = 'x'

                            elif turn3 == 2 and turn5 == 7:
                                if turn7 == 1:
                                    turn8 = 4
                                    grid[4] = 'x'
                                else:
                                    turn8 = 1
                                    grid[1] = 'x'

                            elif turn3 == 3 and turn5 == 4:
                                if turn7 == 8:
                                    turn8 = 7
                                    grid[7] = 'x'
                                else:
                                    turn8 = 8
                                    grid[8] = 'x'

                            elif turn3 == 6 and turn5 == 7:
                                if turn7 == 2:
                                    turn8 = 1
                                    grid[1] = 'x'
                                else:
                                    turn8 = 2
                                    grid[2] = 'x'

                            elif turn3 == 7 and turn5 == 2:
                                if turn7 == 6:
                                    turn8 = 3
                                    grid[3] = 'x'
                                else:
                                    turn8 = 6
                                    grid[6] = 'x'

                            elif turn3 == 8 and turn5 == 3:
                                if turn7 == 4:
                                    turn8 = 1
                                    grid[1] = 'x'
                                else:
                                    turn8 = 4
                                    grid[4] = 'x'

                    elif turn == 9: #when turn is 9
                        print(Player2,"it's your turn")
                        turn9 = eval(input("please enter the box number:")) #taking turn input from the player

                        while grid[turn9] == 'x' or grid[turn9] == 'o': #restricting the player from choosing an already occupied box number
                            print()
                            print("This box is already occupied")
                            turn9 = eval(input("please enter another box number:"))
                        
                        grid[turn9] = 'o' #printing the symbol in the grid
           
            print()
            display_grid()  #Printing the grid after each turn by calling the display_grid function

            #checking winning condition by calling the winning_condition function
            check = winning_condition(Player1,Player2,turn)
            #ending the game if the condition is true or continuing it if the condition is false
            if check == True:
                break
            else:
                continue
    

def main(): #defining a main function
    
    #printing the beginning of the game
    print("-----------( WELCOME TO TIC TAC TOE )-----------")
    print()
    print(format(' ','18s'),"T | I | C")
    print(format(' ','18s'),"--+---+--")
    print(format(' ','18s'),"T | A | C")
    print(format(' ','18s'),"--+---+--")
    print(format(' ','18s'),"T | O | E")

    main_menu = 'm' #Asignning value 'm' to variable main_menu
    while main_menu == 'm': #running the loop until the value of main_menu is 'm'
        print()
        print(format(' ','16s'),"( MAIN MENU )") #printing main menu heading
        print("________________________________________________")
        print()
        print(" --> Press 1 to play SINGLE PLAYER GAME \n --> Press 2 to play DOUBLE PLAYER GAME \n --> Press any key to EXIT ") #displaying the menu
        print("________________________________________________")
        print()
        game_choice=input("Enter your choice: ") #taking the input from user
        print()

        another_game = 'y' #Asignning value 'y' to variable another_game        
        while another_game == 'y': #running the loop until the value of another_game is 'y'
            grid_reset()             
            if game_choice == '1':
                print("-------------- SINGLE PLAYER GAME --------------")
                single_player_game() #calling the single_player_game function if user chooses 1
            
            elif game_choice == '2':
                print("-------------- MULTI PLAYER GAME ---------------")
                two_player_game() #calling the two_player_game function if user chooses 2
            else:
                break #exiting the game if user presses any other key
            print()
            another_game = input(" --> Do you want to play another game? y/n: ") #asking if the user wants to play another game or not
            while another_game != 'y' and another_game != 'n':
                print()
                print ("INVALID INPUT")
                another_game = input("Enter a valid option: ") #restricting the player from choosing wroing option
                
            print()
                
        print()
        main_menu = input(" --> Press 'm' to go to the MAIN MENU or 'e' to EXIT game: ") #asking if the user want to go to the main menu or exit the game

main() #calling the main function
