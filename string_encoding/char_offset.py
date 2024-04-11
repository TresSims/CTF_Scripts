# Subtract string index from unicode point value
def decode(input_string):
    i = 0
    decoded_string = ""
    for char in input_string:
        new_char = chr(ord(char) - i)
        decoded_string += new_char
        i += 1
    
    print(decoded_string)

# Add string index to unicode point value
def encode(input_string):
    i = 0
    encoded_string = ""
    for char in input_string:
        new_char = chr(ord(char) + i)
        encoded_string += new_char
        i += 1
    
    print(encoded_string)

if __name__ == "__main__":
    operation = input("Encode or decode? [e/d]: ")
    user_input_string = input("What value to encode or decode?: ")

    # choose whether to encode or decode a string
    if(operation == "e"):
        encode(user_input_string)
    elif(operation == "d"):
        decode(user_input_string)
    else:
        print("Sorry, I didn't get that.")