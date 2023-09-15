import pyotp
import pyperclip
import subprocess

# Define the ASCII art text for the logo
logo = """
██████╗░████████╗██╗░░██╗
██╔══██╗╚══██╔══╝██║░██╔╝
██████╔╝░░░██║░░░█████═╝░
██╔══██╗░░░██║░░░██╔═██╗░
██║░░██║░░░██║░░░██║░╚██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

def generate_totp_code(secret_key):
    secret_key = secret_key.replace(' ', '')  # Remove spaces
    secret_key = secret_key.upper()  # Convert to uppercase

    # Try to generate the TOTP code
    try:
        totp = pyotp.TOTP(secret_key)
        totp_code = totp.now()
        return totp_code
    except pyotp.utils.OtpError:
        return "Invalid Secret Key"

while True:
    print(logo)  # Display the logo

    # Ask the user for the secret key
    secret_key = input("Enter the secret key (leave empty for default): ").strip()

    # If the user didn't provide a secret key, use the default
    if not secret_key:
        secret_key = 'MOYP X7QM QRBR IZDH QP7O LWXF WSQO LQNN'

    # Generate TOTP code
    totp_code = generate_totp_code(secret_key)

    # Display and copy the TOTP code to the clipboard
    print('OTP Code:', totp_code)
    pyperclip.copy(totp_code)
    print('OTP Code has been copied to the clipboard.')

    # Ask if the user wants to run the script again
    run_again = input('Do you want to run the script again? (y/n): ').lower()
    if run_again != 'y':
        break

print('Exiting the script.')
