import pyotp
import pyperclip

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

if __name__ == "__main__":
    while True:
        secret_key = input("Enter the secret key: ").strip()
        totp_code, error = generate_totp_code(secret_key)

        if totp_code:
            print('TOTP Code:', totp_code)
            pyperclip.copy(totp_code)
            print('TOTP Code has been copied to the clipboard.')
        else:
            print('Error:', error)

        run_again = input('Do you want to run the script again? (y/n): ').strip().lower()
        if run_again != 'y':
            break

    print('Exiting the script.')
