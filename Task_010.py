string_1 = input("word 1:")
string_2 = input("word 2:")


def find_common_characters(string_1, string_2):
    set1 = set(string_1)
    set2 = set(string_2)
    set3 = set1 & set2
    string_final = ",".join(set3)
    print("Common letters:", string_final)


find_common_characters(string_1, string_2)
