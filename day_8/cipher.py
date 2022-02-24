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
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift, direction):
    if direction == "encode":
        new_text = []
        for char in text:
            index_in_alphabet = alphabet.index(char)
            char = alphabet[index_in_alphabet + shift]
            new_text.append(char)
            
        new_str=""
        for char in new_text:
            new_str += char
            
        print(new_str)
        
    elif direction == "decode":
        new_text = []
        for char in text:
            index_in_alphabet = alphabet.index(char)
            char = alphabet[index_in_alphabet - shift]
            new_text.append(char)

        new_str = ""
        for char in new_text:
            new_str += char

        print(new_str)
        
encrypt(text,shift, direction)