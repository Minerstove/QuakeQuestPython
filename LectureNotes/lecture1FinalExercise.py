mixed_code = "rstj rs {ifd z-}'kzze jzmzekpue-ez" #"defz de myvt lpno{llu zl'lu{bgupul"
alphabet = "abcdefghijklmnopqrstuvwxyz{}'-"

def ceasarCypher_decoder(ciphertext, shift, alphabet):
    decrypted_text = ""
    for char in ciphertext:
        if char in alphabet:  # Only shift characters in the provided alphabet
            char_index = alphabet.index(char)
            decrypted_index = (char_index + shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_index]
        else:
            decrypted_text += char  # Keep characters not in the alphabet unchanged
    return decrypted_text
    
def brute_force_caesar_extended(ciphertext, alphabet):
    for shift in range(1, len(alphabet)):  # Try all possible shifts
        print(f"Shift by {shift}: {ceasarCypher_decoder(ciphertext, shift, alphabet)}")

def nokiaCode_decorder():
    nokiaCode = ["6", "33", "7777", "7777", "2", "4", "33", "0", "444", "66", "8", "44", "33", "7", "666", "33", "6"]
    letter_list = []
    for code in nokiaCode:
        match code[0]:
            case "0":
                if (len(code) == 1):
                    letter_list.append(' ')
            case "1":
                if (len(code) == 1):
                    letter_list.append('?')
            case "2":
                if (len(code) == 1):
                    letter_list.append('a')
                elif (len(code) == 2):
                    letter_list.append('b')
                elif (len(code) == 3):
                    letter_list.append('c')
            case "3":
                if (len(code) == 1):
                    letter_list.append('d')
                elif (len(code) == 2):
                    letter_list.append('e')
                elif (len(code) == 3):
                    letter_list.append('f')
            case "4":
                if (len(code) == 1):
                    letter_list.append('g')
                elif (len(code) == 2):
                    letter_list.append('h')
                elif (len(code) == 3):
                    letter_list.append('i')
            case "5":
                if (len(code) == 1):
                    letter_list.append('j')
                elif (len(code) == 2):
                    letter_list.append('k')
                elif (len(code) == 3):
                    letter_list.append('l')
            case "6":
                if (len(code) == 1):
                    letter_list.append('m')
                elif (len(code) == 2):
                    letter_list.append('n')
                elif (len(code) == 3):
                    letter_list.append('o')
            case "7":
                if (len(code) == 1):
                    letter_list.append('p')
                elif (len(code) == 2):
                    letter_list.append('q')
                elif (len(code) == 3):
                    letter_list.append('r')
                elif (len(code) == 4):
                    letter_list.append('s')
            case "8":
                if (len(code) == 1):
                    letter_list.append('t')
                elif (len(code) == 2):
                    letter_list.append('u')
                elif (len(code) == 3):
                    letter_list.append('b')
            case "9":
                if (len(code) == 1):
                    letter_list.append('w')
                elif (len(code) == 2):
                    letter_list.append('x')
                elif (len(code) == 3):
                    letter_list.append('y')
                elif (len(code) == 4):
                    letter_list.append('z')
    final_word = "".join(letter_list)
    return final_word

def boardCode_decoder():
    original_string = '2Cm7zRRDo0+zetF#GVm0t9Metz!4a8dr9e&idt,sS2pDoa#3i05nm#'
    result_string = ""
    for char in original_string:
        if (char in "7 Deadly Sins") and (char in "Dolley's"):
            continue
        else:
            result_string += char

    result_string_2 =""
    for char in result_string:
        if (char in "2,529 CRV & 37 Suzuki cars :D") or (char in "Mama+papa") or (char in "Finland 1829!"):
            result_string_2 += char
        else:
            continue

    result_string_3 = ""
    for char in result_string_2:
        if (char not in "Get some methoxyl! #2935 & 48oz"):
            result_string_3 += char
        else:
            continue

    final_str = "------- ------- -----"
    words = final_str.split(' ') # split the str using spaces
    final_words = []
    end = 0
    for i, word in enumerate(words):
        start = end
        end += len(word)
        final_words.append(result_string_3[start:end]) # slicing, get chars from index=start to before index=end

    final_str = ' '.join(final_words)

    return final_str

brute_force_caesar_extended(mixed_code,alphabet) #shift by 9 forward
print(nokiaCode_decorder()) # this give message in the poem
print(boardCode_decoder()) #This means Jose Rizal\

"""
The answer is Jose Rizals message in his 1879 poem which is ANG KABATAAN, ANG PAGASA NG BAYAN
"""