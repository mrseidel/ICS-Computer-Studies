import string

ws = string.whitespace
s = 'abc def\tghi\njkl'

for c in s:
    if c not in ws:
        print (c, end='')
    else:
        print ()