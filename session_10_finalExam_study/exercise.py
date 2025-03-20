def cipher(map_from, map_to, code):
    key_code = {}
    decoded_word = ""
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for char in code:
        decoded_word += key_code[char]
    return key_code, decoded_word


print(cipher("abcd", "dcba", "dab"))
