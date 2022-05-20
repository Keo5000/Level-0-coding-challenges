string_1 = input("word 1:")
string_2 = input("word 2:")


def find_common_characters(string_1, string_2):
    result = ""
    for letter in string_1:
        if letter in string_2:
            result += letter
    return ", ".join(result)


print("Common letters:", find_common_characters(string_1, string_2))
