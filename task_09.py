def vowel(word):
    vowels = "aeiuo"
    word = word.lower()
    result = ""
    for letter in vowels:
        if letter in word:
            result += letter
    return ", ".join(result)


print("Vowels:", vowel("Umuzi"))
