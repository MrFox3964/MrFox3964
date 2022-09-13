#the goal of the assignment is to output a users input with the spaces replaced with elipses;...)
def main():
    name = input('"YOUR LINE SIR! "') .replace(" ","...")
    shakespear(name)

def shakespear(to="name"):
    print(to)

main()