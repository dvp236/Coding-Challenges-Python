

'''Swaminarayan!!!'''
# get all anagrams of the string
# get permutation of String


# permuteHelper(r,"",abc) -> permuteHelper(r,a,bc),permuteHelper(r,b,ac),permuteHelper(r,c,ab)
# permuteHelper(r,a,bc) -> permuteHelper(r,ab,c), permuteHelper(r,ac,b)
# permuteHelper(r,ab,c) -> permuteHelper(r,abc,"")-> base case.
# Time Complexity: O(2^n +1)
def permuteHelper(pre,s,resultlist):
    if len(s) == 0:
        return resultlist.append(pre)

    for i in range(len(s)):
        #get all possible pre from string
        permuteHelper(pre+s[i],s[:i]+s[i+1:],resultlist)

    return resultlist

def permute(s):
    resultlist = []
    pre = ""
    return permuteHelper(pre,s,resultlist)


final = permute("abcd")
print final
