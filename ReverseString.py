

'''Swaminarayan !!!'''
#there are many ways to reverse string
#we will use recursion to do it
def reverse(s):
    if len(s) <= 1:
    return s

    return reverse(s[1:]) + s[0]


reverse("Patel")
