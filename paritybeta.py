def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
def is_even(n):
    return True if n % 2 == 0 else False
main()
#here i created a function that tells the computer if the value of the remainder is 0 the function is true and the program will issue the command
#if it returned false the main program uses else to print odd
#finally you can change the created function to just simplify the question
#return n % 2 == 0 (it already is a true or false question, this just says return if the remainder is 0)
#both are fine it's just the simplest way to write this
