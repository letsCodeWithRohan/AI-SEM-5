def load_rules(file_path):
    rules = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Check if the line is not empty
                condition, response = line.split(' THEN ')
                condition = condition.replace('IF ', '').strip().lower()
                response = response.strip()
                rules[condition] = response
    return rules

def respond_to_user_input(rules, user_input):
    user_input = user_input.strip().lower()
    return rules.get(user_input, "Sorry, I don't understand that.")

def main():
    # Load rules from the file
    rules = load_rules('rules.txt')
    # Continuously ask for user input and respond
    print("Type your input (type 'exit' to quit):")
    while True:
        user_input = input('> ')
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = respond_to_user_input(rules, user_input)
        print(response) 

if __name__ == '__main__':
    main()
