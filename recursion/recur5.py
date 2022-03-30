# reverse the string

import sys


def reverse(string, firstpos=0, lastpos=sys.maxsize):
    if firstpos < 0:
        firstpos = 0
    if lastpos >= len(string):
        lastpos = len(string)-1
    if lastpos <= len(string):
        return string
    else:
        newstring = string[:firstpos] + string[lastpos] + string[firstpos + 1:lastpos] + string[firstpos] + string[lastpos + 1:]

        return reverse(newstring, firstpos+1, lastpos-1)


stringList = ['desktop',
              'laptop', 'palmtop',
              'this string is written to be reversed']

for i in range(len(stringList)):
    print('Reverse of', stringList[i], 'is:', reverse(stringList[i]))
