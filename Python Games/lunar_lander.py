"""
INTRODUCTION:

Lunar Lander is one of the earliest computer games. With a proper choice of initial values, it is
fairly interesting to play, even though it is a text-only program.

You will take the role of an astronaut in the lunar module attempting to land on the moon’s
surface. Gravity pulls you towards the moon at an increasing rate of speed. In order to land
safely, you must burn fuel to counter gravity’s acceleration to land on the moon at a safe speed
(below 10 m/s). However, be careful, you can only use so much fuel. And if you are too high
when you run out of fuel , you’ll inevitably crash at an unsafe speed.

User determines how much fuel to burn next second, and he/she attempts to burn an amount of fuel appropriate to land safely.
"""

print("INTRODUCTION:")
print("Lunar Lander is one of the earliest computer games. With a proper choice of initial values, it is fairly interesting to play, even though it is a text-only program.")
print("You will take the role of an astronaut in the lunar module attempting to land on the moon’s surface. Gravity pulls you towards the moon at an increasing rate of speed.")
print("In order to land safely, you must burn fuel to counter gravity’s acceleration to land on the moon at a safe speed(below 10 m/s).")
print("However, be careful, you can only use so much fuel. And if you are too high when you run out of fuel, you’ll inevitably crash at an unsafe speed.")
print("Throughouth the game, you will determine how much fuel to burn next second, and you should attempt to burn an amount of fuel appropriate to land safely.\n\n")

game_running = True

#a while loop: while condition is met, run code block inside loop
#while game_running is True , run code block inside loop
while (game_running):

    altitude = 100.0    # meters
    velocity = 0.0      # meters / second
    fuel = 100.0        # leters
    time = int(0)       # seconds passed from start of game
    fuel_force = float(0.15)
        # fuel_force = float(input("What is the force exerted by fuel? A good entry is 0.15. Please enter: "))
        # = TBU --> fuel force = 0.15 meters / second / second
        # MUST CATCH ERRORS
    gravity = float(1.6)
        # gravity = float(input("How strong is the force of gravity? A good entry is 1.6. Please enter: "))
        # = TBU --> gravity = 1.6 meters / second / second
        # MUST CATCH ERRORS
    #while loop: while condition is met, run code block inside loop
    while (altitude > 0):

        # give user the lander's altitude, velocity and fuel.
        print("\nRound " + str(time+1) + ": it has been " + str(time) + " seconds since you have been aboard the lunar lander.")
        print("Your altitude is " + str(altitude) + " meters.")
        print("Your velocity is " + str(velocity) + " meters per second.")
        print("Your fuel reserve is " + str(fuel) + " liters.")
        print("You can burn fuel somewhere between 0 and " + str(fuel) + ".")

        # ask for user input at their turn.
        fuel_burn = input("How much fuel do you want to burn next second? ")
        print("Round " + str(time+1) + " instructions have been received!\n")

        # catch error: what if they enter an invalid amount (i.e. a non-number) for fuel
        try:
            fuel_burn = float(fuel_burn)
        except:
            while (fuel_burn.isdigit() != True):
                print("You did not enter a correct fuel burn value!\nYou entered '" + str(fuel_burn) + "' of data type " + str(type(fuel_burn)) + ".\nPlease enter a positive numeric value.")
                fuel_burn = input("How much fuel do you want to burn next second? ")
            fuel_burn = float(fuel_burn)
            """
            else:
            try:
            except except ValueError as e:
                while isnumeric(fuel_burn) != True:
                    print("You did not enter a correct fuel burn value!\nYou entered '" + str(fuel_burn) + "' of data type " + str(type(fuel_burn)) + ".\n")
                    # print("Official error encountered is: " + str(e) + ".")
                    fuel_burn = input("How much fuel do you want to burn next second? ")
            """
                    # impose limitations on user input
        else:
            fuel_burn = float(fuel_burn)
            if (fuel_burn < 0): # user cannot gain fuel
                print ("You entered a negative amount of fuel burn.\nHowever, you cannot gain fuel.\nHence, you will burn 0 fuel.")
                fuel_burn = float(0)
            elif (fuel_burn > fuel):   # user cannot use fuel he/she does not possess
                print ("You consumed more fuel than you actually had. You ran out of fuel.\nYou actually burnt", fuel, "amount of fuel!\nNow you have no more fuel left!")
                fuel_burn = float(fuel)
            elif (fuel_burn == 0): # user can pass a round.
                fuel_burn = float(0)
                print ("You will burn no fuel per your choice.")
            elif (0 < fuel_burn < fuel): # user is being reasonable and sensible
                fuel_burn = float(fuel_burn)
                print ("You consumed", fuel_burn, "liters of fuel.")
            else:                   # just to make sure -- has been tested that this condition will never happen
                print ("An unexpected error has occured.")
            fuel_burn = float(fuel_burn)

            # confirm that instructions have been successfully processed.
            print("Round " + str(time+1) + " instructions have been approved by command center! We will burn " + str(fuel_burn) + "liters of fuel.\n")

        """
        Process the round!
        Calculate the next second's altitude, velocity, and fuel over the next second.
        """
        
        # time passes
        time += 1
        # gravity pulls you down at an increasing rate
        velocity_after_gravity = float(velocity + gravity)

        # fuel used up, and pushes lander up at the rate of fuel burn.    
        """ debugging
        # type(fuel_burn)
        # type(fuel_force) """
        propellant = fuel_burn * fuel_force
        fuel -= fuel_burn

        # final velocity
        velocity = velocity_after_gravity - propellant

        # altitude drops
        altitude = altitude - velocity
        
        """DEBUGGING: test of data types
        print(type(velocity))
        print(type(gravity))
        print(type(velocity_after_gravity))
        print(type(fuel_burn))
        print(type(fuel_burn_2))
        print(type(fuel_force))
        print(type(propellant))
        """
              
    """
    GAME END
    If altitude is below the ground, the game ends/
    Note: we do not need to test for altitude being <= 0 because this is assumed
    """
    # check to see if landed safely
    if (velocity < 10) == True:
        print ("Congratualations! You have landed safely!\nYou landed at the safe speed of {}, which is lower than 10m/s.\nIt took you {} seconds to land.\nYou still have {} liters of left.".format(velocity, time, fuel))
    # otherwise, the lunar lander has crashed!
    else:
        print ("The lunar lander has crashed!\nYou landed at the unsafe speed of {}, which is the same or higher than 10m/s.\nIt took the lunar lander {} seconds to land.\nYou still have {} liters of fuel left.".format(velocity, time, fuel))
    # Notify user that game has ended
    print ("\nThe game has ended!!!\n")
    # Replay? Prompt user if they want to play again and exit the game.
    play_again = input('Do you want to play again? Please enter "y" or "Y" for "Yes" and "n" or "N" for "No"!')
    # Make sure entry is either "y", "Y", "n", or "N"
    while ((play_again == "Y" or play_again == "y" or play_again == "N" or play_again == "n") != True):
        play_again = input('Your input was not understood!\nDo you want to play again? Please enter only either "y" or "Y" to play again, or either "n" or "N" to exit.')
    # If user wants to play again, keep playing. Otherwise, exit the game.
    if play_again == "N" or play_again == "n":
        print("Ending the game per your request!!!")
        game_running = bool(False)
    elif play_again == "Y" or play_again == "y":
        print("Starting a new game per your request!!!")
        game_running = bool(True)
