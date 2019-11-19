def rotate_string(text, rot):
    dict_u = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    dict_l = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    list_u = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    translate_dict_u = dict(enumerate(list_u))
    list_l = ("abcdefghijklmnopqrstuvwxyz")
    translate_dict_l = dict(enumerate(list_l))
    new_message = ''
    for letter in text:
        if letter.isupper():
            old_upper = dict_u.get(letter)
            shifted_upper = (old_upper + rot)%26
            new_upper = translate_dict_u.get(shifted_upper)
            new_message += new_upper
        elif letter.islower():
            old_lower = dict_l.get(letter)
            shifted_lower = (old_lower + rot)%26
            new_lower = translate_dict_l.get(shifted_lower)
            new_message += new_lower
        elif letter.isalpha() == False:
            new_message += letter
    return new_message
