import random
import string

def generatepass(length=16, use_symbols=True):
    # Start with letters (uppercase + lowercase) and digits
    chars = string.ascii_letters + string.digits
    # If user wants symbols, add punctuation characters
    if use_symbols:
        chars += string.punctuation

    # Randomly pick 'length' characters from the pool 'chars'
    return ''.join(random.choice(chars) for _ in range(length))

def pause():
    input("Press any key to continue...")

if __name__ == "__main__":
    while True:
        length_input = input("Length of password (default 16): ").strip()
        # If user presses Enter, use default length 16
        if length_input == '':
            length = 16
            break
        # Check if input is a positive number
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        print("Please enter a valid positive number or press Enter for default.")

    symbols_input = input("Include symbols? (Y/n): ").strip().lower()
    # Accept 'y', 'yes', or empty input as True; anything else as False
    use_symbols = True if symbols_input in ['', 'y', 'yes'] else False

    # Generate the password with chosen options
    password = generatepass(length, use_symbols)
    print(f"Password: {password}")
    pause()