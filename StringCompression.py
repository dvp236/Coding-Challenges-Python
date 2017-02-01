
print "Swaminarayan!!"


def compress(s):

    if len(s) == 0:
        return ""
    result = ""
    count = 1
    curr_char = s[0]
    #aabbbccd
    for char in s[1:]:
        if char != curr_char:
            result += curr_char+str(count)
            curr_char = char
            count = 1
        else:
            count+=1
    result += curr_char+str(count)

    if len(result) > len(s):
        return s

    return result



compress("aaabbccccd")
