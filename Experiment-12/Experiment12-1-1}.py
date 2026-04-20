# Phone Number Database Management

n = int(input().strip())
contacts = {}

for _ in range(n):
    command = input().strip().split()

    if command[0] == "ADD":
        name = command[1]
        phone = command[2]
        # Add or update contact
        contacts[name] = phone

    elif command[0] == "REMOVE":
        name = command[1]
        # Remove if exists, ignore otherwise
        contacts.pop(name, None)

    elif command[0] == "DISPLAY":
        if not contacts:
            print("No contacts")
        else:
            # Display sorted by name
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")
