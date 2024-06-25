print('''

                           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')

print("Welcome to treasure Island. Your mission is to find the treasure.")

while True:
    road_choice = input("You come upon a fork in the road do you take the left branch or the right branch?").lower()
    if road_choice == "left" or road_choice == "right":
        break

if road_choice == "left":
    while True:
        river_choice = input("You come up on a river what do you wish to do swim or wait for a boat?").lower()
        if river_choice == "swim" or river_choice == "wait":
            break

    if river_choice == "wait":
        house_choice = input("You discover a Gothic house hidden in the trees, " +
                             "There are multiple doors which one do you take red blue or yellow?").lower()
        if house_choice == "yellow":
            print("You found the treasure!! You win!!")
        elif house_choice == "red":
            print("You get burned alive!! Game over!!")

        elif house_choice == "blue":
            print("You were eaten by cannibals!! Game Over!!")
        else:
            print("The world has ended you should've chosen a door!! Game over!!")
    else:
        print("You attacked by a giant Pike! Game over")
else:
    print("You were attacked by bandits robbed and left for dead.! Game over")




