import random
import string

def generatepass(length=16, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    while True:
        length_input = input("Length of password (default 16): ").strip()
        if length_input == '':
            length = 16
            break
        if length_input.isdigit() and int(length_input) > 0:
            length = int(length_input)
            break
        print("Please enter a valid positive number or press Enter for default.")

    symbols_input = input("Include symbols? (Y/n): ").strip().lower()
    use_symbols = True if symbols_input in ['', 'y', 'yes'] else False

    password = generatepass(length, use_symbols)
    print(f"Password: {password}")
