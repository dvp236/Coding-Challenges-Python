
print "Swaminarayan Bhagawan ni jay !!"


#complexity O(nlog(n))
def findMissingElement(a1,a2):
    n1 = len(a1)
    n2 = len(a2)

    if n1 == n2:
        return
    a1.sort()
    a2.sort()


    bigger = []
    smaller = []
    if n1>n2:
        bigger += a1
        smaller += a2
    else:
        bigger +=a2
        smaller +=a1

    for i in range(len(smaller)):
        if bigger[i] != smaller[i]:
            return bigger[i]
    return bigger[-1]


print findMissingElement([1,2,3],[1,2,3,4])


#complexity O(n)
def findMissingElement1(a1,a2):
    #d = collections.defaultdict(int)

    count = {}
    for item in a1:
        if item not in count:
            count[item] =1
        else:
            count[item] += 1

    for item in a2:
        if item not in count:
            count[item] = -1
        else:
            count[item] -= 1

    for key,val in count.items():
        if val != 0:
            return key


print findMissingElement1([1,2,3,4,5,6],[1,5,4,3])



#most efficient solution
#doing ex-or operation
def findMissingElement3(a1,a2):
    result = 0

    for num in a1+a2:
        result ^= num

    return result



print findMissingElement3([1,1,2,2],[1,1,2,2,1])
