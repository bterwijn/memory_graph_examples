import string

def CaesarCipher(text: str, shift: int, decrypt=False) -> str:
    letters = string.ascii_letters
    ciphered_text = list()

    for letter in text:
        if letter in letters:
            index = letters.index(letter) + shift if not decrypt else letters.index(letter) - shift
            ciphered_text.append(letters[index])
        else:
            ciphered_text.append(letter)

    return ''.join(ciphered_text)

def main() -> None:

    print("1) Encrypt")
    print("2) Decrypt")

    user_input = input("> ").lower()
    try:
        match user_input:
            case "1":
                text = input("Encrypt Text: ")
                shift = int(input("Shift: "))
                print(CaesarCipher(text, shift, False))
            case "2":
                text = input("Decrypt Text: ")
                shift = int(input("Shift: "))
                print(CaesarCipher(text, shift, True))
            case _:
                print("Invalid Choice.")

    except ValueError:
        print("Invalid Input!")

if __name__ == "__main__":
    main()

