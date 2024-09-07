def nokiaCode_decorder():
    nokiaCode = [6, 33, 7777, 7777, 2, 4, 33, 0, 444, 66, 8, 44, 33, 7, 666, 33, 6]


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

print(boardCode_decoder)