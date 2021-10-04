"""
CIT 591 - week 3 assignment - Tower Blaster
Name: SINA ALIPOUR-NAZARI
PennID: 20359038

STATEMENT OF WORK:
- I used no resources, except for lecture materials.
- No people helped me (including TAs/Instructor).
- I completed this work alone without help.
"""

# import random library, required for shuffling
import random

def  setup_bricks():
    """
● Runs at beginning of the game.
● Creates a main pile of 60 bricks, represented as a list containing the integers 1 – 60.
● Creates a discard pile of 0 bricks, represented as an empty list.
● Returns both lists.
    """
    # initializes a list for main deck
    main_deck_init = []
    # add integers 1-60, in order, to the main pile list
    for n in range (1, 61, 1):
        main_deck_init.append(n)
        
    # create an empty discard pile
    discard_deck_init = []
    
    # debugging
    # print("main deck init:", main_deck_init)
    # print("discard deck init:", discard_deck_init)

    # return main pile and discard pile
    return main_deck_init, discard_deck_init


def shuffle_bricks(bricks):
    """
● Shuffles the given list of bricks.
● Runs at the beginning of the game and when discard pile is returned to main pile
● This function does not return anything.
● imports the random module.
    """
    # import random library, required for shuffling
    # import random # already imported

    # shuffle the list of bricks
    random.shuffle(bricks)


def check_bricks(main_pile, discard):
    """
● Checks if there are any cards left in the given main pile of bricks.
● If no cards left, shuffles discard pile and moves those bricks to the main pile.
● Then turns over the top card to be the start of the new discard pile.
    """
    # debugging
    # print("check_bricks running")
    if len(main_pile) == 0:
        # shuffles discard pile using the shuffle(bricks) function.
        shuffle_bricks(discard)

        # debugging
        # print("shuffled discard:", discard)
        
        # puts discard pile back in main pile
        main_pile.extend(discard)
        # clears items in discard pile
        discard.clear()

        # debugging
        # print("main pile after extend:", main_pile)
        # print("discard pile after clear:", discard)
        
        # puts top card on main pile back into discard pile
        discard.insert(0, main_pile.pop(0))

        # debugging
        # print("shuffled discard after returning top card:", discard)
        # print("main pile after returning top card:", main_pile)

        
def check_tower_blaster(tower):
    """
● Given a tower (user pile or  computer pile), determines if tower stability has been achieved - i.e. if bricks are in ascending order.
● Returns a boolean value True if tower blaster has been achieved and returns False if it has not been achieved.
    """
    # makes list tower2 and takes a snapshot of list tower
    tower2 = tower.copy()
    # sorts tower2 in ascending order.
    tower2.sort()
    # if the tower order is the same as the ascending sorted tower, returns True to indicate tower is stable
    if tower2 == tower:
        return True
    # if stability has not been achieved, returns False
    else:
        return False
    

def get_top_brick(brick_pile):
    """
● Removes and return the top brick (an integer) from any given pile of bricks.
● Used at the start of game play for dealing bricks
● Also used at each player’s turn to take the top brick from either the discard brick pile or the main pile.
● Returns an integer.
    """
    # isolate the value of top brick (first item in list) from the selected brick pile
    top_brick = brick_pile[0]
    # remove the top brick (first item in list) from the selected brick pile
    brick_pile.pop(0)
    # function returns the top brick from the pile
    return top_brick


def deal_initial_bricks(main_pile):
    """
● SThis function runs at beginning of game.
● Deals two sets of 10 bricks each, from main_pile.
● Following the conventions of dealing cards:
    1) deals one brick to the computer, one to the user, one to the computer, one to the user, and so on.
    2) The computer is always the first person that gets dealt to and always plays first.
    3) Places bricks one on top of the other.
● returns a tuple containing two lists - one representing user’s hand and computer’s hand.
    """
    # deal 10 cards for computer and human in order
    for n in range(0, 10, 1):  # repeats this instruction for 10 times
        # debugging
        # print("dealing hand count:", n)
        # print("main_pile:", main_pile)
        
        # draw a card from top of main pile and put it on top in the computer pile
        top_brick = get_top_brick(main_pile)
        computer_pile.insert(0, top_brick)
        # debugging
        # print("after dealing to computer...")
        # print("computer pile:", computer_pile)
        # print("main_pile:", main_pile)
        
        # draw a card from top of main pile and put it on top of human pile
        top_brick = get_top_brick(main_pile)
        human_pile.insert(0, top_brick)
        # debugging
        # print("after dealing to human...")
        # print("human pile:", human_pile)
        # print("main_pile:", main_pile)
    # debugging
    # print("cards left in main pile:", len(main_pile))
    
    # returns updated computer tower and human tower
    return computer_pile, human_pile


def add_brick_to_discard(brick, discard):
    """
● Adds the given brick (represented as an integer) to the top of the given discard pile list
● Does not return anything.
    """
    # insert the brick on top of the discard pile (first element in list)
    discard.insert(0, brick)


def human_play(human_pile, main_pile, discard):
    """
    This function represents what happens in a human turn. The human gets a choice to play from discard or main pile.
    If he/she chooses to play from main pile, he/she gets to choose whether to use the card.
    If he/she chooses to play from discard pile, he/she gets no choice.
    Once he/she is set to use the card in hand, human replaces one card in his/her tower with the card in hand.
    """
    # gives player some basic needed information
    print("Human turn!")
    print("Human pile looks like:", human_pile)
    print("Top card on discard pile:", discard[0])

    # ask human which pile to pick card from
    human_choice_of_pile = "n"  # ensures the while loop can start
    # while loop helps collect a pre-determined input of "m" or "d"
    while not ((human_choice_of_pile == "m") or (human_choice_of_pile == "d")):
        human_choice_of_pile = input("Do you want to use the main pile or discard pile? Enter 'm' for main pile and 'd' for discard pile.")

    # what happens if human chooses to pick card from main pile
    if human_choice_of_pile == "m":
        # variable brick_pile, representing the working pile, is set to main_pile
        brick_pile = main_pile
        # debugging
        # print("You chose to turn the top card on main pile.")

    # what happens if human chooses to pick card from main pile
    elif human_choice_of_pile == "d":
        # variable brick_pile, representing the working pile, is set to discard_pile
        brick_pile = discard
        # debugging
        # print("You chose to pick from the discard pile.")

    # pick up the card from your chosen pile (working pile).
    card_in_hand = get_top_brick(brick_pile)
    print("Brick in your hand:", card_in_hand)

    # if human picks the main pile...
    if human_choice_of_pile == "m":
        # runs the function to ask human for input and collect the input
        did_human_play = human_choice_to_play()
        # and if human decides to use the card...
        if did_human_play == True:
            # he/she replaces the card and discards the card being replaced
            human_replaces_card(card_in_hand, human_pile, discard)
        # if human picks the main pile and decides not to use the card...
        elif did_human_play == False:
            # debugging
            # print("You chose not to insert the card into your deck.")
            # he/she puts the card in their hand back in discard
            add_brick_to_discard(card_in_hand, discard)
            # debugging
            # print("Discard looks like:", discard)
    # However, If human chose to pick a card from the discard pile, he/she won't get a choice not to play the card
    elif human_choice_of_pile == "d":
        # he/she will have to pick a card from their tower to replace the card with.
        human_replaces_card(card_in_hand, human_pile, discard)

    # return the updated human pile
    return human_pile


def human_replaces_card(card_in_hand, human_pile, discard):
    """
    This is a function that replaces the card in human tower with the card human is holding.
    It only runs if the human decides to play the card he/she has picked up."
    """
    
    # This piece of code allows human to pick which brick from the human tower to replace
    brick_to_be_replaced = 0  # this makes sure the while loop begins
    # while loop allows to catch errors until a correct input is made.
    while brick_to_be_replaced not in human_pile: # loop repeats until a brick from within the human_pile is selected
        brick_to_be_replaced = int(input("Which brick do you want to replace?")) # collects entry on brick to be replaced and converts to integer
    
    ''' debugging
    # print("Game pile before picking up the brick:", brick_pile)
    # print("Brick in your hand:", card_in_hand)
    '''

    print("You replaced " + str(brick_to_be_replaced) + " with " + str(card_in_hand) + ".")  # just an update to human player
    # replace the card in tower with the card in hand, and discard the card removed from tower.
    find_and_replace(card_in_hand, brick_to_be_replaced, human_pile, discard)
        
def human_choice_to_play():
    """ This function is called when human chooses to peek at the main pile.
    It allows for human player to choose whether to use the card they have picked up.
    """ 
    does_human_want_to_play = "g"   # dummy variable to make sure while loop starts
    # while loop to catch errors if the right entry of "y" ir "n"
    while not ((does_human_want_to_play == "y") or (does_human_want_to_play == "n")):
        # asks user if they want to use the card they picked until they make a correct entry
        does_human_want_to_play = input("Do you want to use the card? Enter 'n' to discard and 'y' to place the card in your tower.")
    # if human enters "y", returns True
    if does_human_want_to_play == "y":
        return True
    # human enters "n", returns False
    elif does_human_want_to_play == "n":
        return False
    
def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):

    """
    ● Checks to make sure the given brick to be replaced (an integer) is truly a brick in the given tower.
    ● Finds the brick to be replaced (an integer) in the given tower and replaces it with the given new brick.
    ● Puts the brick_to_be_replaced on top of the given discard pile.
    ● Return True if the given brick is replaced, otherwise return False.
    """
    # debugging
    # print("running find_and_replace function.")
    # print("tower:", tower, type(tower))
    # print("tower[1]:", tower[1], type(tower[1]))
    # print("brick_to_be_replaced:", brick_to_be_replaced, type(brick_to_be_replaced))
    # print("brick found?:", brick_to_be_replaced in tower)
    
    # make sure that the given brick to be replaced is truly a brick in the given tower.
    if brick_to_be_replaced in tower:
        # Replace the brick to be replaced in the given tower and with the given new brick.
        tower.insert(tower.index(brick_to_be_replaced), new_brick)

        # then, put brick to be replaced in the discard pile
        tower.pop(tower.index(brick_to_be_replaced))
        add_brick_to_discard(brick_to_be_replaced, discard)

        #debugging
        # print("The brick number " + str(brick_to_be_replaced) + " from the tower replaced with the new brick " + str(new_brick) + "!")
        # print("tower after replacement:", tower)
        # print("discard after replacement:", discard)

        # debugging
        # print("Card successfully replaced.")
        
        # return True to indicate function of brick transfer was successful
        return True
    # otherwise return False to indicate function of brick transfer was unsuccessful
    else:
        # debugging
        # print("Card not successfully replaced.")
        return False # return False to indicate function of brick transfer was not successful
    

def computer_play(tower, main_pile, discard):
    """
● The computer follows a deterministic strategy to play its card.
First it tries to find a use for the top brick from the discarded brick pile.
If it is successful, it will use that card.
Otherwise, it will try to pick a card from the main pile.

In evaluating the decisions, the computer tries to avoid disastrous outcomes by making sure:
- all cards at the top are small numbers
- all cards at the bottom are large numbers
- neither choice of a card blocks the chances of winning the game by making sure the distance between towers is same or larger than the size difference between towers.
Then, the computer makes sure each card is aligned so that each card from top to bottom is smaller than the card after it.

- Computer has access to the same information that the human gets access to in its turn.
- For example, the computer will at no point get to know any of the bricks in the main pile or the discard pile before making its decision.

● Function returns the new tower for the computer.
    """
    print("Computer turn!")

    # computer starts its turn by evaluating the discard pile
    card_in_hand = discard.pop(0)
    print("Computer picked ", card_in_hand, " from discard pile.")

    # debugging
    # print("Computer holds and evaluates the discard pile's top card: " + str(card_in_hand))
    # print("card in hand:", card_in_hand)
    # print("Discard pile after picking up the card:", discard)

    # checks if the card in hand picked from discard pile is useful, returns a bool value and the card to be replaced
    is_brick_replaced, brick_to_be_replaced = is_card_useful(card_in_hand)

    # debugging
    # print("is_brick_replaced:", is_brick_replaced)
    # print("brick_to_be_replaced:", brick_to_be_replaced)

    # if computer likes the card... it inserts the card in computer pile and discards
    if is_brick_replaced == True:
        # debugging
        # print("Computer likes the top card in discard pile: " + str(card_in_hand))
        # replace chosen card with card in hand, and discard chosen card 
        find_and_replace(card_in_hand, brick_to_be_replaced, computer_pile, discard)
        print("Computer replaced a brick.")
    # if computer did not find the discard pile card useful, it turns to the main pile and repeats the same process.
    elif is_brick_replaced == False:
        # First, it returns the discard pile's top card back onto the discard pile
        add_brick_to_discard(card_in_hand, discard)

        #debugging
        # print("Computer holds and evaluates the main pile's top card: " + str(card_in_hand))
        # print("card in hand:", card_in_hand)
        # print("Pile after picking up the card:", main_pile)

        # computer peeks at the top card from main pile
        card_in_hand = main_pile.pop(0)
        print("Computer picked ", card_in_hand, " from main pile.")

        # computer decides if the top card from main pile is useful. Returns a bool and the card to be replaced.
        is_brick_replaced, brick_to_be_replaced = is_card_useful(card_in_hand)

        # debugging
        # print("is_brick_replaced:", is_brick_replaced)
        # print("brick_to_be_replaced:", brick_to_be_replaced)

        # computer gets to pick if it wants to use the it picked from the main pile
        if is_brick_replaced == True: # if it likes the card
            # debugging
            # print("Computer likes the top card in main pile: " + str(card_in_hand))
            # then it replaces the card it wants to replace and discards it
            find_and_replace(card_in_hand, brick_to_be_replaced, computer_pile, discard)
            print("Computer replaecd a brick.")
        else: # if computer does not like the card from main pile either...
            # then it puts the card back into the discard pile
            add_brick_to_discard(card_in_hand, discard)
            
    # function returns the updated computer pile
    return computer_pile


def is_card_useful(card_in_hand):
    """ This function is how the computer decides if the card in its hand is useful it it.
    If computer finds it useful, it returns a True and the card that it wants to replace it with.
    """

    # first off, computer breaks down its pile into beginning, middle, and end.
    if card_in_hand < 20:     # if the card in hand is smaller than 20
        tower_range = computer_pile[0:3] # computer is going to look to use it in the top 3 of its tower.
        range_min = 1 # sets minimum useful card in this range
        range_max = 19 # sets maximum useful card in this range
    elif 20 <= card_in_hand <= 40: # if the card in hand is between 20 and 40 (including 40)
        tower_range = computer_pile[3:7]
        range_min = 20 # sets minimum useful card in this range
        range_max = 40 # sets maximum useful card in this range
    else:
        tower_range = computer_pile[7:10] # if the card in hand > 40
        range_min = 41 # sets minimum useful card in this range
        range_max = 60 # sets maximum useful card in this range

    # this is where max/min analysis starts to make sure cards within a tower_range don't make it impossible to achieve tower blaster.
    # uses a while loop to iterate through  cards in card range

    # debugging
    # print("starting max/min analysis start")

    test = False # initialize test, makes sure while loop can start
    # debugging
    # print("while loop begins.")
    # print("test:", test)
    while test is False:  # while loop runs until test turns to True
        # this for loop checks to see if each of the cards in the range of cards are smaller than the minimum brick size that could be placed in that region.
        for card_position in range(0, len(tower_range), 1):  # for each card in tower range
            # finds the minimum useful card number in that card position
            useful_card_min = range_min + card_position

            # debugging print("starting min analysis")
            # print("card_position:", card_position)
            # print("useful min:", useful_card_min)

            # gets the real value of the card in that position
            card_value = tower_range[card_position]

            # This if statement determines if card in hand is useful to the problem computer is facing
            # compares the real card value and the minimum card value for that position to see if there is a minimum value problem AND compares the card in hand with the value of the problematic card to see if the card in hand is useful.
            if (card_value < useful_card_min) and (card_in_hand > card_value):  # if true (i.e. if card in hand is definitely useful) returns true and breaks the loop
                # debugging
                # print("This is a minimum problem.... we found a card > ", useful_card_min)
                return True, card_value  # return True and the value of the card to be replaced
                test = True  # terminates the while loop

        # this for loop checks to see if each of the cards in the range of cards, iterated in reverse order, are larger than the largest brick size that could be placed in that region.
        for card_position_r in range(len(tower_range), 0, -1):  # for each card in tower range iterated in reverse order
            # finds the maximum useful card in that card position
            useful_card_max = range_max - card_position

            # debugging
            # print("Starting max analysis")
            # print("card_position_r:", card_position_r)
            # print("useful max:", useful_card_max)
            
            # gets the real value of the card in the position
            card_value = tower_range[-card_position]

            # This if statement determines if card in hand is useful to the problem computer is facing
            # compares the real card value and the maximum card value for that position to see if there is a maximum value problem AND compares the card in hand with the value of the problematic card to see if the card in hand is useful.    
            if (card_value > useful_card_max) and (card_in_hand < card_value):  # if true (i.e. if card in hand is definitely useful) returns true and breaks the loop
                # debugging
                # print("This is a minimum problem.... we found a card > ", useful_card_min)
                return True, card_value  # return true to indicate a replacement will happen, and the value of the problem card to be replaced
                test = True  # terminates the while loop

        # This for loop checks to see if the entire tower is in ascending order by checking each card against its next card
        for card_pair in range(1, len(tower_range), 1):  # for each card (card pair) starting from the first (top) position in the tower range and ending in the second last card in the range (last card pair)
            # identifies the value of both cards in a pair of cards
            card1 = tower_range[card_pair - 1]
            card2 = tower_range[card_pair]
            # checks see if the card on top of a pair of cards is in the wrong order - i.e. larger in brick of the prick is on top - and if so, returns True
            if (card1 > card2) and (card_in_hand > card2):  # if the order is right, return True and the card to be replaced, and break the loop.
                # debugging
                # print("bad card pair.... replacing second card in card pair")
                return True, card2  # returns true to indicate a replacement will happen, as well as the value of the problem card to be replaced
                test = True  # terminates the while loop
            # checks see if the card on top of a pair of cards is in the wrong order - i.e. larger in brick of the prick is on top - and if so, returns True
            elif (card1 > card2) and (card_in_hand < card1):
                # debugging
                # print("bad card pair.... replacing first card in card pair")
                return True, card1  # returns true to indicate a replacement will happen, and the first card is pair will be replaced
                test = True # terminates the while loop
            
        # if we performed all three tests on the full tower range of interest, and no use-case is found for the card...
        # then function returns False to indicate function failed to place the card_in_hand
        print("Computer did did not like the card.")
        return False, 0  # returns False and a placeholder value of card 0 for consistency of data types
        test = True  # terminates while loop

        
def main():
    """
● This function runs the Tower Blaster game in appropriate gameplay.
● Computer and Human play until one of them gets Tower Blaster, which means their tower stability has been achieved.
    """
    # introduce two lists to represent the computer pile and human pile
    global computer_pile
    global human_pile
    computer_pile = []
    human_pile = []

    # debugging
    # print("setup_bricks runs") 

    # sets up the main deck and the discard deck; arranges main deck in order
    main_deck, discard_deck = setup_bricks()

    ''' debugging
    #print("main_deck: ", main_deck)
    #print("discard_deck: ", discard_deck)
    #print("shuffle_bricks runs")
    '''

    # shuffles main deck
    shuffle_bricks(main_deck)
    ''' debugging
    print("main_deck after shuffling: ", main_deck)
    print("discard_deck: ", discard_deck)
    '''

    # at the beginning of the game, deals 10 cards to computer and human each, using the right conventions of dealing cards 
    deal_initial_bricks(main_deck)
    print("cards have been dealt.")
    ''' debugging
    print("main_deck:", main_deck)
    print("discard_deck:", discard_deck)
    '''
    print("Computer initial pile:", computer_pile)
    print("Cuman initial pile:", human_pile)
    
    print("Top card from main pile was placed in discard pile.")
    add_brick_to_discard(get_top_brick(main_deck), discard_deck)
    ''' debugging
    print("main_deck: ", main_deck)
    print("discard_deck: ", discard_deck)
    '''

    # this is where the game really begins with a while loop that allows for computer and human to take turns.
    game_is_on = True  # this value makes sure while loop can begin
    # while loop makes sure game ends when one party achieves tower blaster
    while game_is_on is True:
        
        # computer turn
        computer_pile = computer_play(computer_pile, main_deck, discard_deck)

        ''' debugging
        print("main_deck: ", main_deck)
        print("discard_deck: ", discard_deck)
        print("computer_pile: ", computer_pile)
        print("human_pile: ", human_pile)
        '''
        # check to see if computer achieved tower blaster        
        game_is_on = not (check_tower_blaster(computer_pile))
        if (check_tower_blaster(computer_pile)):
            print("Computer achieved Tower Blaster. Computer won.")

        ''' debugging
        print("tower blaster achieved?", check_tower_blaster(computer_pile))
        print("game is on?", game_is_on)
        '''

        # check to see if main pile is empty.... if yes, shuffle discard pile and restore to main pile
        check_bricks(main_deck, discard_deck)

        # computer turn
        human_pile = human_play(human_pile, main_deck, discard_deck)

        ''' debugging
        print("main_deck: ", main_deck)
        print("discard_deck: ", discard_deck)
        print("computer_pile: ", computer_pile)
        '''
        print("Updated human_pile: ", human_pile)

        # check to see if human achieved tower blaster        
        game_is_on = not (check_tower_blaster(human_pile))
        if (check_tower_blaster(human_pile)):
            print("Human achieved Tower Blaster. Human won.")

        ''' debugging
        print("tower blaster achieved?", check_tower_blaster(computer_pile))
        print("game is on?", game_is_on)
        '''

        # check to see if main pile is empty.... if yes, shuffle discard pile and restore to main pile
        check_bricks(main_deck, discard_deck)
    # if the while loop ends, we know the game has ended.
    print("Game has ended.")


if __name__ == "__main__":
    main()
