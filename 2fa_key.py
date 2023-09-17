import pyotp
import pyperclip
import os

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear_screen()
        print('*-Programme By Mr. Beta-*')
        print('1. Cookies Remove')
        print('2. Number Remove')
        print('3. Generate TOTP Code')
        print('4. Exit')
        choice = input('>> ')

        if choice == '1':
            rc()
        elif choice == '2':
            rn()
        elif choice == '3':
            generate_totp()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please try again.')

def rc():
    print('Remove Cookies Selected')
    try:
        all_id = open(input('Input File Path > '), 'r').read().splitlines()
    except:
        exit('File Not Valid')
    print('Enter Output File Name')
    print('Example : bd69ids.txt')
    save = input('>> ')
    open(f'/sdcard/{save}', 'w').write('')
    for id in all_id:
        try:
            uid, password, cookie = id.split('|')
            print(uid + '|' + password)
            open(f'/sdcard/{save}', 'a').write(uid + '|' + password + '\n')
        except:
            pass

def rn():
    print('Remove Number Selected')
    try:
        all_id = open(input('Input File Path > '), 'r').read().splitlines()
    except:
        exit('File Not Valid')
    print('Enter Output File Name')
    print('Example : bd69ids.txt')
    save = input('>> ')
    open(f'/sdcard/{save}', 'w').write('')
    for id in all_id:
        try:
            count = len(id.split('|'))
            if count == 4:
                number, uid, password, cookie = id.split('|')
                print(uid + '|' + password)
                open(f'/sdcard/{save}', 'a').write(uid + '|' + password + '|' + cookie + '\n')
            elif count == 3:
                number, uid, password = id.split('|')
                print(uid + '|' + password)
                open(f'/sdcard/{save}', 'a').write(uid + '|' + password + '\n')
        except:
            pass

def generate_totp():
    secret_key = input("Enter the secret key for TOTP generation: ").strip()
    totp_code, error = generate_totp_code(secret_key)

    if totp_code:
        print('TOTP Code:', totp_code)
        pyperclip.copy(totp_code)
        print('TOTP Code has been copied to the clipboard.')
    else:
        print('Error:', error)

if __name__ == '__main__':
    menu()
