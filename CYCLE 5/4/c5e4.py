
from palindrome import is_palindrome

def longest_palindromic_substring(s):

    longest = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring

    return longest    

input_string = input("Enter the string : ")
print(f"Longest Palindromic Substring: {longest_palindromic_substring(input_string)}")


