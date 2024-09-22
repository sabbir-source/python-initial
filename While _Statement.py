command = ""
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        print("you are ready to go!")
    elif command == "stop":
        print("car is going to stop!")
    elif command == "help":
        print("start :- you are ready to go" "stop :- car is going yo stop")
    else:
        print("sorry! I don't understand.")
