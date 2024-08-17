def is_palindrome_1(word):
    if type(word) == int:
        word = str(word)
    return word == word[::-1]

def is_palindrome_2(word):
    l = len(word)
    for i in range(l//2):
        if word[i] != word[l-i-1]:
            return False
    return True

input_word = "acbnbca"
num = 123321
print("using palindrome_ 1", input_word, is_palindrome_1(input_word))
print(input_word, is_palindrome_1(num))