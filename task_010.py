string_1 = input()
string_2 = input()


def find_common_characters(string_1, string_2):
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    result = ""
    for letter in string_1:
        if letter in string_2:
            result += letter
    return ", ".join(result)


print("Common letters:", find_common_characters(string_1, string_2))
