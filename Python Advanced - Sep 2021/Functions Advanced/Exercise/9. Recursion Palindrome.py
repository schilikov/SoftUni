# Check if the given word is a palindrome or not
def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)

# Test Codes
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))

