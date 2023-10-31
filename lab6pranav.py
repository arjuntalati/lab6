def encoded(digit):
    encoder = ''
    for x in digit:
        encoded = str((int(x) + 3) % 10)
        encoder += encoded
    return encoder
def decoded(encoder):
    decPassword = ""
    if len(encoder) != 8 or not encoder.isdigit():
        print("Invalid input. Encoded password must be an 8-digit string containing only integers.")
        return None

    for digit in encoder:
        decDigit = str((int(digit) - 3) % 10)
        decPassword += decDigit

    return decPassword


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1.Encode')
        print('2.Decode')
        print('3.Quit')

        selection = int(input('Please enter an option: '))
        if selection == 1:
            password = (input('Please enter a password to encode: '))
            print('Your password has been encoded and stored!')
            encodedPassword = encoded(password)
        if selection == 2:
            decodedPassword = decoded(encodedPassword)
            print(f"The encodes password was {encodedPassword}, and the original password is {decodedPassword}.")
        if selection == 3:
            exit()





if __name__ == '__main__':
    main()
