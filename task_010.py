def find_common_characters(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    result = ""
    for letter in string_2:
        if letter in string_1:
            if letter in result:
                continue
            result += letter

    return "Common letters: " + ", ".join(result)


print(find_common_characters("HOUSES", "computerss"))
