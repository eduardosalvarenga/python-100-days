# Create a Encoder and Decoder using Caesar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, start_shift, start_direction):
    txt = ""
    if start_direction == "decode":
        start_shift *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + start_shift
            txt += alphabet[new_position]
        else:
            txt += char
    print(f"The {direction}d text is {txt}")


from art import logo

print(logo)

restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, start_shift=shift, start_direction=direction)

    result = input("Do you want to restart the cipher program? Type yes or no\n")
    if result == "no":
        restart = False
        print("Goodbye!")