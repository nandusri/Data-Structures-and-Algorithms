"""
Find Longest Substring That is Palindrome

"""


def find_longest_palindrome(s):
    longest = ""
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            word = s[i:j]
            if word == word[::-1]:
                if len(word) > len(longest):
                    longest = word
    return longest


s = input("Enter string:\n").strip()
print(s)

print(find_longest_palindrome(s))
