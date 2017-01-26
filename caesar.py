def alphabet_position(letter):

    ascii = ord(letter)

    if ascii >= 65 and ascii <= 90:
        num = ascii - 65
    else:
        num = ascii - 97


    return num



def rotate_character(char, rot):

    if char.isalpha():

        new_num = alphabet_position(char)

        cyphered_num = (new_num + rot) % 26

        if char.isupper():

            now_num = cyphered_num + 65
        else:
            now_num = cyphered_num + 97

        new_character = chr(now_num)

        return new_character

    else:
        return char

def encrypt(text, rot):

    new_string = ""
    for sep_char in text:
        new_string = new_string + rotate_character(sep_char, rot)


    return new_string
