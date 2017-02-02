

##check if string has unique characters
print "God is great!"


def is_unq(s):
    st = set()
    for char in s:
        if char in st:
            return False
        st.add(char)
    return True


is_unq("abc")



def is_unq2(s):
    return len(set(s))==len(s)



is_unq2("abbc")
