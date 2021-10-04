"""
Your name: SINA ALIPOUR-NAZARI
Your PennID: 20359038

STATEMENT OF WORK:
- I used no resources, except for:
    A) StackOverflow to look up these:
            'import time'
            'time.sleep(seconds)'
    B) Python Docs (F1 in IDLE)
            'import random'
            'random.randint(lowerint, upperint)'
- No people helped me (including TAs/Instructor).
- I completed this work alone without help.
"""

import time

# print instructions
def print_instructions():
    """This function introduces the game to the human player.
    """
    # print intstructions for the game
    print("Pig​ is a very simple game. Two players take turns; on each turn, a player rolls a six-sided die as many times as she wishes, or until she rolls a 6.\nEach number she rolls, except a 6, is added to her score this turn; but if she rolls a 6, her score for this turn is zero, and her turn ends.\nAt the end of each turn, the score for that turn is added to the player's total score. The first player to reach or exceed 50 wins.\n\nFor example:\n\tAlice rolls 3, 5, 3, 1, and stops. Her score is now 12.\n\tBob rolls 5, 4, 1, 1, 2, and stops. His score is now 13.\n\tAlice rolls 5, 3, 3, 5, 4, and stops. Her score is now 32 (12 + 20).\n\tBob rolls 4, 6. He has to stop, and his score is still 13 (13 + 0).\n\tetc.\n\nTo make the game  fair, if the first player reaches or exceeds 50, the second player gets one additional turn. However, if the second player is the first to reach 50, the first player does not get an additional turn.\nYou will play against the computer. The computer always goes first, so you get one more turn if the computer is the first to reach 50.\nIf both players are tied with 50 or more, each gets another turn until the tie is broken. Each player must roll the die at least once per turn.")
    print("")
    
def ask_yes_or_no(prompt):
    """This function takes a question (prompt) parameter and prompts the user to answer "Y", "y", "N", or "N".
    It returns True if input is "y" or "Y", and returns False if input is "n" or "N".
    """
    # assign a dummy variable
    user_input = "init"
    # check if input is a valid entry: 'y', 'Y', 'n', or 'N', and repeats until a valid entry is made.
    while (True != (user_input == "y" or user_input == "Y" or user_input == "n" or user_input == "N")):
        # if input is not valid, prompts user to enter a valid entry.
        user_input = input("{} Please enter 'y', 'Y', 'n', or 'N'!".format(prompt))

    # 'Y' and 'y' return an answer of True
    if user_input[0] == "y":
        yes_or_no_answer = True
    elif user_input[0] == "Y":
        yes_or_no_answer = True

    # 'N' or 'n' return an answer of False
    elif user_input[0] == "N":
        yes_or_no_answer = False
    elif user_input[0] == "n":
        yes_or_no_answer = False

    # function outputs (returns) the answer
    return yes_or_no_answer

def roll(list_of_dice):
    """This function generates a random number from 1-6.
    If the die rolls anything but a 6, the die score is appended to the list of dice scores.
    If the user decides not to play further, they can collect their dice points, and stop playing.
    If the die a 6, the turn's dice score is reset to zero, and the player's turn ends.
    """

    # import library for random number generator
    import random
    
    print("Rolling die....")
    time.sleep(2)
    # generate a random number between 1 and 6
    die = random.randint(1,6)
    print("The die rolled out to be", die)
    time.sleep(2)
    print("")

    # If die rolls a 6, the list of dice is purged, die score is set to 0, and a breaker function is set to True
    if die == 6:
        list_of_dice = []
        breaker = True
        die = 0
        print("The die rolled out a 6. The player's turn has been wasted.")
    # If die rolls anything but a 6, the die score is appended to the list of dice scores, and a bool function called 'breaker' is set to False.
    else:
        breaker = False
        list_of_dice.append(die)

    # output of the funtion is a tuple with a) list of dice, and b) the breaker function
    return (list_of_dice, breaker)

def add_up_dice(list_of_dice):
    """
    This function takes the list of dice in a turn as the parameter, adds up the score for all the dice played that turn.
    """
    # resets sum of dice to 0
    sum_of_dice = 0

    # adds up all the dice scores in the list of dice that have been played that turn.
    # for statement repeats the operation for the number of times a list is played - i.e. until all dice played have been added up.
    for die in list_of_dice:
        # adds up the next die score to previous die score... 
        sum_of_dice += die

    # function outputs the sum of the player's score for that turn.
    return sum_of_dice

def will_computer_roll_again(computer_score, human_score, list_of_dice):
    """This function outlines the mathematical calculations the computer makes to determine if it will roll the die or terminate its turn.
    """
    # computer's mental mathematics
    computer_mental_sum_of_dice = add_up_dice(list_of_dice)
    computer_mental_score = computer_score + computer_mental_sum_of_dice

    # initial conditions
    computer_risky_behavior = False
    computer_conservative_behaviour = False

    # define risky behaviour
    if human_score >= 35 and (human_score >= computer_mental_score + 4):
        computer_risky_behaviour = True
    else:
        computer_risky_behaviour = False

    # define conservative behaviour
    if computer_score >= 35 and (computer_mental_score >= human_score + 11):
        computer_conservative_behaviour = True
    else:
        computer_conservative_behaviour = False

    # under risky behaviour, computer tries to collect more points at the risk of losing all points.
    if computer_risky_behaviour == True:
        computer_decision = True

    # under conservative behaviour, computer collects points.
    elif computer_conservative_behaviour == True:
        computer_decision = False

    #under normal conditions, computer tries to collect a minimum of 7 points from each turn.
    else:
        if computer_mental_sum_of_dice >= 7:
            computer_decision = False
        else:
            computer_decision = True

    return computer_decision

def roll_again_decision(computer_score, human_score, whose_playing):
    """ This function relays the decision of the computer or the human player as to whether they want to roll the next die."
    The computer and the human player use different mechanisms for making their decision.
    """

    # if it is the computer's turn, run the computer decision making mechanism
    if whose_playing == "computer":
        # output is a boolean
        return will_computer_roll_again(computer_score, human_score, list_of_dice)
    # if it is the human's turn, ask the user if they want to roll again.
    elif whose_playing == "human":
        # output is a boolean
        return ask_yes_or_no("Do you want to roll again?")
        

def turn(computer_score, human_score, whose_playing):
    """This function describes what happens in a turn.
    At the beginning of the turn, the player rolls the dice once.
    Afterward, it keeps rolling dice unless/until the player decides to terminate the turn or a die rolls a 6.
    Each roll adds to the count of rolls in that turn.
    At the end of each turn, the list of dice that turn are summed and the score for that turn is added to the player's total score.
    """
    print("It is the " + str(whose_playing) + "'s turn!\n")
    time.sleep(0.5)
    # reset roll count to 0
    roll_count = 0
    global list_of_dice
    list_of_dice = []
    # for every roll in this turn, the following takes place
    for roll_count in range(0, 1000, 1):
        # if it is the player's first roll in the turn, they are forced to take the roll.
        if roll_count == 0:
            print("This turn's roll count is " + str(roll_count) + ". Each player will roll the die at least once each turn.")
            time.sleep(0.5)
            # and the output of the first roll of dice to the list of dice and a breaker (whether they rolled a 6)
            list_of_dice, breaker = roll(list_of_dice)
            # we add the first roll to the count of rolls
            roll_count += 1
            # if breaker is on (i.e. they rolled a 6) the turn is terminated.
            if breaker == True:
                break
            
        else: #if it is not the player's first roll, he player will keep rolling until they either decide not to play again or they roll a 6.
            # the player keeps rolling until they decide to stop, using the roll_again_decision function!
            while roll_again_decision(computer_score, human_score, whose_playing) == True:
                print("Did the", whose_playing, "decide to play again?")
                time.sleep(0.5)
                print(True)

                # every time the player rolls and does not bring a 6, the roll's score adds up to the list of dice.
                list_of_dice, breaker = roll(list_of_dice)
                # and after every roll, we add one to the number of rolls they've had that turn
                roll_count += 1

                # if they have rolled a 6, their turn is terminated
                if breaker == True:
                    break

            # if the user decided not to play, the turn terminates, and a text output informs the user they chose to terminate.           
            else:
                print("Did the", whose_playing, "decide to play again?", False, "\n")
                time.sleep(0.5)
                print(whose_playing, "has now rolled", roll_count, "times in this turn.")
                
            # when the turn is terminated by choice or because the player rolls a 6, the loop of rolls breaks.
            break

    # at the end of every turn...
    # we add up the score of all rolls in the turn
    sum_of_dice = add_up_dice(list_of_dice)

    # prints sum of all rolls
    print ("Sum of this turn is " + str(sum_of_dice) + " from " + str(roll_count) + " number of rolls.")

    # returns sum of dice for adding to human score and computer score
    return sum_of_dice

def computer_move(computer_score, human_score):
    """This function runs the computer's turn by informing the turn function that the computer is playing
    It output's the computer's score for the turn.
    See the turn function's DocStrings for more details.
    """
    #set player to computer
    whose_playing = "computer"
    # runs the turn function while identifying the computer as the player, and outputs the computer's socre for the turn.
    sum_of_dice = turn(computer_score, human_score, whose_playing)
    # adds the computer's turn's score to its previous score
    global computer_sc
    computer_sc = computer_sc + sum_of_dice

def human_move(computer_score, human_score):
    """This function runs the human's turn by informing the turn function that the human is playing.
    It output's the human's score for the turn.
    See the turn function's DocStrings for more details.
    """
    # set player to human
    whose_playing = "human"
    # runs the turn function while identifying the human as the player, and outputs the computer's socre for the turn.
    sum_of_dice = turn(computer_score, human_score, whose_playing)
    # adds the human's turn's score to their previous score
    global human_sc
    human_sc = human_sc + sum_of_dice


def show_current_status(computer_score, human_score):
    """This function displays the current status of the game: Who's got how many points and who is ahead by how much?
    """
    time.sleep(1)
    print("\n")
    # displays the human score
    print("The human score is: ", human_sc)
    # displays the computer score
    print("The computer score is: ", computer_sc)

    # compares the human score with computer score
    if (human_score > computer_score): # when human is ahead
        print ("You are ahead of the computer by: ", human_sc - computer_sc)
    elif (human_score < computer_score): # when human is behind
        print ("You are behind the computer by: ", computer_sc - human_sc)
    elif (human_score == computer_score): # in case of a tie
        print ("You and the computer are tied at: ", human_sc)
    time.sleep(1)
    print("\n")
    
def is_game_over(computer_score, human_score):
    """ This function checks if the game is finished or it shoud continue.
    """
    # check if one or more player(s) reached score of 50 or more
    if (computer_score >= 50) or (human_score >= 50):
        # if one player has reached 50 but the scores are equal, we play another round - i.e. do not finish the game.
        if human_score == computer_score:
            print ("you finished equal... get ready for an exciting tie breaker.\n")
            # False means "game is not over"
            return False
        
        # if one or more players has reached 50 but scores are different, game ends
        else:
            # True means "game is over"
            return True
        
    # if neither player has reaches score of 50, game continues
    else:
        # False means "game continues"
        return False

def show_final_results(computer_score, human_score):
    """Once the program has decided the game is over, this function informs the user of the winner of the game, and by how many points.
    """
    time.sleep(1)
    print("\n\nGame is over!")
    time.sleep(1)

    # if human lost, we tell the user they lost by some points
    if computer_score > human_score:
        print ("Human lost by: ", computer_score - human_score)

    # if human won, we tell the user they won by some points.
    if human_score > computer_score:
        print ("human wins by: ", human_score - computer_score)

def main():
    """This function determines the game's game-play and the sequence of events.
    The computer plays first, and then the human plays.
    Because the computer plays first, the game can only end after both the computer and the human have played the same turn -- i.e. after the human's turn.
    Once the game ends with a winner, the program asks the human player if they want to play again, and could restart the game.
    """
    # print game instructions
    print_instructions()

    # confirm they have read instructions
    start = input("Please confirm you have read the instructions by typing 'YES'.")
    while start != 'YES':
    #make sure they have read instructions and can follow instructions before they move forward.
        start = input("Please say 'YES' to confirm you have read the instructions.")
    print("\nThank you for reading the instructions\n")

    # set an initial game_is_playing variable to True to make sure game starts in the first round.
    game_is_playing = True

    # game play starts here.... the game repeats until the user ends it -- user gets to select no at the end of each round of the game.
    while game_is_playing == True:
        # catching input of 'START' makes sure user is ready to start the game.
        start = input("Please say 'START' to begin the game.")
        while start != 'START':
            # makes sure user can read and follow instructions -- or else gameplay won't begin
            start = input("Please say 'START' to begin the game.")
        print("Starting a new game\n")

        # set up global variables for human score and computer score
        global human_sc
        global computer_sc

        # before beginning the game, reset player scores to 0, and inform the players of the score   
        human_sc = 0
        computer_sc = 0

        print("human score:", human_sc)
        print("computer score:", computer_sc)
        print("")
    
        # play many turns, the gameplay is as follows 
        for turn in range(0, 1000, 1):
            # computer's turn to play
            computer_move(computer_sc, human_sc)
            # shows current status
            show_current_status(computer_sc, human_sc)
            # human's turn to play
            human_move(computer_sc, human_sc)
            # shows current status
            show_current_status(computer_sc, human_sc)
            # at the end of turn, check to see if game has ended
            if is_game_over(computer_sc, human_sc) == True:
                # if game has actually ended... show final results and stop the loop of turns
                show_final_results(computer_sc, human_sc)
                break
        # if game has ended, ask user if they want to play again and set "game_is_playing" to either stop or replay.
        game_is_playing = ask_yes_or_no("Play again?")
        time.sleep(2)

# The game begins by calling the main() function.
if __name__ == '__main__':
    main()
