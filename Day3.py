# Day 3
# Build a Game where the user has to make choices.

print('''
*******************************************************************************
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           ||.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You\'re at a cross road. Where do you want to go? Type 'left' or 'right' \n")
if(direction.lower() == "left"):
    lake_direction = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if(lake_direction.lower() == "wait"):
        colour = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        if(colour.lower() == "yellow"):
            print("Congratulations, you found the treasure!")
        elif(colour.lower() == "red"):
            print("You were burned by fire. Game Over!")
        elif(colour.lower() == "blue"):
            print("You were eaten by beasts. Game Over!")
        else:
            print("You tripped and died. Game Over!")
    else:
        print("You were attacked by a trout. Game Over!")
else:
    input("You fell into a hole. Game Over!")
