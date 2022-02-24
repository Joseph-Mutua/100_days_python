# def greet(name, weekday, location):
#     print(f"Good Morning {name}")
#     print(f"Hope you're having a beautiful {weekday} morning")
#     print(f"Our servers show you're playing from {location}")


# greet(location="Juja",name="Mutua", weekday="Friday",)

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# #e.g.
# #plain_text = "hello"
# #shift = 5
# #cipher_text = "mjqqt"
# #print output: "The encoded text is mjqqt"

# ##HINT: How do you get the index of an item in a list:
# #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',

            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    new_text = []
    for char in text:
        if char in alphabet:
            index_in_alphabet = alphabet.index(char)
            new_char = alphabet[index_in_alphabet + shift]
            new_text.append(new_char)
        else:
            new_text += char

        new_str = ""
        for char in new_text:
            new_str += char

    print(f"The encoded string is {new_str}")


def decrypt(text, shift):
    new_text = []
    for char in text:
        if char in alphabet:
            index_in_alphabet = alphabet.index(char)
            new_char = alphabet[index_in_alphabet - shift]
            new_text.append(new_char)
        else:    
            new_text += char

        new_str = ""
        for char in new_text:
            new_str += char

    print(f"The decoded string is {new_str}")


def caesar_cipher(text, shift, direction):
    shift = shift % 26
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(text, shift, direction)
    result = input("Type 'yes' if you want to continue, otherwise type 'no' \n")

    if result == "no":
        should_continue = False
        print("Goodbye")
