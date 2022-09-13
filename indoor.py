#prompt the user for input

name = input('You hear clumsy rustling coming from the foliage behind you as your friend tries to free their shoe lace caught on a stray twig; "Is someone there?" ').lower().strip()

#reproduce the user's reply but all lowercase letters


print(f'You reply in a whisper "{name}"') 

# The big take away here is that I can set name as a value by making the string a function with f and then putting the value in {} brackets
#also note the double quotes