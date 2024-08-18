class Palindrome:
    def is_palindrome(self, word):
        if type(word) == int:
            word = str(word)
        return word == word[::-1]