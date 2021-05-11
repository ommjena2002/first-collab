command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("The Car is starting...")
    elif command == "stop":
        print("The Car stopped...")
    elif command == "left":
        print("The Car is turning left...")
    elif command == "right":
        print("The Car is turning right...")
    elif command == "quit":
        break
    else:
        print("I don't understand that")