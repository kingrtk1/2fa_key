import pyotp
import pyperclip
import os

# Define the ASCII art text for the logo
logo = """
██████╗░████████╗██╗░░██╗
██╔══██╗╚══██╔══╝██║░██╔╝
██████╔╝░░░██║░░░█████═╝░
██╔══██╗░░░██║░░░██╔═██╗░
██║░░██║░░░██║░░░██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear_screen()
    print(logo)  # Print the logo
    print('Menu:')
    print('1. Generate 2Factor secret key')
    print('2. Remove Duplicates from a file')
    print('3. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        custom_secret_key = input('Enter your custom secret key: ')
        totp_code, error = generate_totp_code(custom_secret_key)

        if totp_code:
            print('OTP Code:', totp_code)
            pyperclip.copy(totp_code)
            print('OTP Code has been copied to the clipboard.')
        else:
            print('Error:', error)
    elif choice == '2':
        rd()  # Call the function to remove duplicates
    elif choice == '3':
        exit()
    else:
        print('Invalid choice. Please enter 1, 2, or 3.')

    ask_continue()

def generate_totp_code(secret_key):
    secret_key = secret_key.replace(' ', '')  # Remove spaces
    secret_key = secret_key.upper()  # Convert to uppercase

    # Try to generate the TOTP code
    try:
        totp = pyotp.TOTP(secret_key)
        totp_code = totp.now()
        return totp_code, None  # Return the TOTP code and no error
    except Exception as e:
        return None, str(e)  # Return no TOTP code and the error message

# Function to remove duplicates from a file
def rd():
    try:
        file_path = input('File Path >> ')
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        exit('File Not Found!')

    new_path = input('New Path >> ')
    print('Duplicate Removing....')

    lines_seen = set()
    with open(new_path, 'w') as outfile:
        for line in lines:
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)

    print('Duplicate Remove Successful')

def ask_continue():
    while True:
        choice = input('Do you want to continue? (y/n): ')
        if choice.lower() == 'y':
            menu()
        elif choice.lower() == 'n':
            exit()
        else:
            print('Invalid choice. Please enter y or n.')

if __name__ == '__main__':
    menu()  # Start with the menu directly
