"""
def accum(s):
    lst = [letter for letter in s]
    result = []
    for i in range(len(lst)):
        result.append(lst[i] * (i+1))
    lstt = '-'.join([ele.capitalize() for ele in result])
    return lstt

print(accum("abcd"))


def accum(s):
    lst = '-'.join([(letter * (i+1)).capitalize() for i, letter in enumerate(s)])
    print(lst)

accum('abcd')
"""

s = "The greatest victory is that which requires no battle"
lst = ' '.join(reversed(s.split()))
print(lst)