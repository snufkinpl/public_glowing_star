def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for letter in sentence:
        if letter in vowels:
            result += letter
    print(len(result))
    return len(result)


sentence = input("Podaj sentence do zbadania: ")
get_count(sentence)
