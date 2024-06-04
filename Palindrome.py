
# <param:type>
def isPalindrome(word:str) -> bool:
    """
    Checks if word is a palindrome or not
    :param word: input
    :return: True if palindrome, else False
    """
    # first way to create vars
    i = 0
    j = len(word)-1

    # another way to create vars
    #i, j = 0, 0

    # another way to create vars
    #i = j = 0

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True

test_cases = ["kayak","racecar","", "bob"]

for test_case in test_cases:
    print(isPalindrome(test_case))