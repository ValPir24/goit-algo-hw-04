def parse_input(user_input): # Parse input function 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts): # Add user and phone to dict function
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts): # Change user phone function
    name, phone = args
    contacts[name] = phone
    return f"The phone for {name} is succesfully changed to {contacts[name]}"

def show_phone(args, contacts): # Show phone of certain name function
    name = args[0]
    return f"{name.upper()} has phone: {contacts[name]}"

def show_all(contacts): # Show all names and phones function
    return f"All the contacts: {contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
