print "Start.."

def isAnagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    return sorted(s1) == sorted(s2)

def isAnagram2(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if not letter in count:
            return False
        count[letter] -=1

    for value in count.values():
        if value != 0:
            return False

    return True

s1 = "patel"
s2 = "leta p"

print isAnagram(s1,s2)


s1=" God"
s2="dog"
print isAnagram2(s1,s2)
print isAnagram(s1,s2)
