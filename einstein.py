#E=mc²
#so i need the user to input an integer for mass and then for the program to calculate the formula in integer format as well

def main():
    m = int(input("What is the mass? " ))
    E = int(pow(300000000,2)*m)
    print(E)

main()