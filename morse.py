choice = input("Do you wish to Encrypt/Decrypt? ").capitalize()

### ENCRYPTION ###
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

if choice == "Encrypt": 
    text =  input("Enter some text: ").upper()                
    encryptable = True
    encrypted_text = ''

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
elif choice == "Decrypt":
    code = input("Enter Morse Code: ")
    decryptable = True
    # String Split including spaces
    # morse_list = [i for j in code.split() for i in (j, ' ')][:-1]
    morse_list = code.split(" ")
    # print(morse_list)
    decrypted_text = ''

    # function to return key for any value
    def get_key(val):
        for key, value in morse_code_dict.items():
            if val == value:
                return key
    
        return "key doesn't exist"

    while decryptable:
        for code_char in morse_list:                    
            if code_char not in morse_code_dict.values() and code_char != '':
                print(f"You have entered a non-decryptable character {code_char}.")
                decryptable = False 
                break


        else:
            for code_char in morse_list:
                if code_char in morse_code_dict.values():
                    # print(code_char)
                    key = get_key(code_char)
                    decrypted_text += key
                elif code_char == '':
                    if decrypted_text[-1] == " ":
                        pass
                    else:
                        decrypted_text += ' '    

            print(decrypted_text.title())
            decryptable = False 
