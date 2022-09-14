name = input("What's your name? ")

if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

#another approach

name = input("What's your name? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")

#tightening the code with the match statement

name = input("What's your name? ")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who?")
    