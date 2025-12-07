def get_num_words(text):
    all_tokens = text.split()
    return len(all_tokens)

def count_characters(text):
    charDict = {}
    for char in text:
        charToTest = char.lower()
        if charToTest == " ":
            continue
        elif charToTest in charDict:
            charDict[charToTest] += 1
        else:
            charDict[charToTest] = 1
    return charDict

def char_dict_sort_on(charDict):
    return charDict["num"]

def sort_char_dict(charDict):
    characters = []
    for key in charDict:
        characters.append({"char": key, "num": charDict[key]})
    characters.sort(reverse=True, key=char_dict_sort_on)

    return characters