

#check if closing and opening parenthesis match
def is_balanced(s):
    if(len(s)==0):
        return True
    if len(s) % 2 != 0:
        return False

    openbraces = set('{[(');

    pairs = set((('(',')'),('{','}'),('[',']')))

    stack = []

    for i in range(len(s)):
        if s[i] in openbraces:
            stack.append(s[i])
        else:
            #{{ }}
            last = stack.pop()
            if (last,s[i]) not in pairs:
                return False

    return len(stack) == 0


is_balanced('{[]}')
