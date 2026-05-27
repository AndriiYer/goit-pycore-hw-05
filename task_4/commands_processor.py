from decorators import input_error

def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


