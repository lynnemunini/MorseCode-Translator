text =  input("Enter a string: ").upper()
encrypted_text = ''
morse_code_dict = { 
                    'A':'.-',
                    'B':'-...',
                    'C':'-.-.', 
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.', 
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---', 
                    'K':'-.-',
                    'L':'.-..', 
                    'M':'--', 
                    'N':'-.',
                    'O':'---', 
                    'P':'.--.', 
                    'Q':'--.-',
                    'R':'.-.', 
                    'S':'...', 
                    'T':'-',
                    'U':'..-', 
                    'V':'...-', 
                    'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.', 
                    ')':'-.--.-'
                    }

for char in text:
    if char == ' ':
        encrypted_text += '  '
    else:
        # for key, value in morse_code_dict.items():     # Check dictionary for a match
            if char in morse_code_dict.keys():
                code = morse_code_dict.get(char)
                encrypted_text = encrypted_text + code + ' '
            else:
                print(f"You have entered a non-english character {char}.") 

print(encrypted_text)     
print(len(encrypted_text))                                 