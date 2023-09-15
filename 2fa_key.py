import pyotp
import pyperclip
import binascii

# Define the ASCII art text for the logo
logo = """
██████╗░████████╗██╗░░██╗
██╔══██╗╚══██╔══╝██║░██╔╝
██████╔╝░░░██║░░░█████═╝░
██╔══██╗░░░██║░░░██╔═██╗░
██║░░██║░░░██║░░░██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

INVALID_WORDS = ['INVALID', 'ERROR', 'NOTALLOWED', 'PASSWORD']

def is_valid_secret_key(secret_key):
    # Check if the secret key contains any invalid words
    for word in INVALID_WORDS:
        if word in secret_key:
            return False
    return True

def generate_totp_code(secret_key):
    secret_key = secret_key.replace(' ', '')  # Remove spaces
    secret_key = secret_key.upper()  # Convert to uppercase

    # Check if the secret key is valid
    if not is_valid_secret_key(secret_key):
        print('Invalid Secret Key: Contains forbidden words')
        return None

    # Try to generate the TOTP code
    try:
        totp = pyotp.TOTP(secret_key)
        totp_code = totp.now()
        return totp_code
    except binascii.Error:
        print('Invalid Secret Key: Incorrect padding')
        return None

while True:
    print(logo)  # Display the logo

    # Ask the user for the secret key
    secret_key = input("Enter the secret key (leave empty for default): ").strip()

    # If the user didn't provide a secret key, use the default
    if not secret_key:
        secret_key = ''

    # Display the secret key
    print('Secret Key:', secret_key)

    # Generate TOTP code
    totp_code = generate_totp_code(secret_key)

    if totp_code:
        # Display and copy the TOTP code to the clipboard
        print('TOTP Code:', totp_code)
        pyperclip.copy(totp_code)
        print('TOTP Code has been copied to the clipboard.')

    # Ask if the user wants to run the script again
    run_again = input('Do you want to run the script again? (y/n): ').lower()
    if run_again != 'y':
        break

print('Exiting the script.')
