text =  input("Enter a string: ").upper()

### ENCRYPTION ###
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
encryptable = True

while encryptable:
    for char in text:                    
        if char not in morse_code_dict.keys() and char != ' ':
            print(f"You have entered a non-encryptable character {char}.")
            encryptable = False 
            break
    else:
        for char in text: 
            if char == ' ':
                encrypted_text += '  '               
            elif char in morse_code_dict.keys():
                code = morse_code_dict.get(char)
                encrypted_text = encrypted_text + code + ' '             

    print(encrypted_text)    
    encryptable = False 
    # print(len(encrypted_text))

### DECRYPTION ###
