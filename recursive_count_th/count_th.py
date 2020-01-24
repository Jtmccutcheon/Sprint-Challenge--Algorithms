'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # if length of a word is less than or equal to one we know it cant have "th"
    if len(word) <= 1:
        return 0
    # check if the first two characters are "th"
    if word[0] + word[0+1] == 'th':
        # we can add one because theres one instance of "th"
        # recursively call our function to check the remaining string
        # after the frist 2 characters
        return 1 + count_th(word[2:])
    else:
        # if the first two charactesr are not "th"
        # move down the string one posistion and check
        # the next two characters
        return count_th(word[1:])
