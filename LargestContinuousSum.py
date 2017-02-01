
print "Swaminarayan!"


def count(array):
    if len(array) == 0:
        return
    curr_sum = array[0]
    max_sum = array[0]

    #1 2 -1 4 3 10 10 -10 -5
    for item in array[1:]:
        curr_sum = max(curr_sum+item,item)
        max_sum = max(max_sum,curr_sum)


    return max_sum


print count([-5,-2,-4,-1,3])
print count([1,2,-1,3,4,10,10,-10,-50,10,10,10,10,-10,20,20,20])


def count_index(arr):
    if len(arr) == 0:
        return
    curr_sum = arr[0]
    max_sum = arr[0]
    start = 0
    end = 1
    #1 2 -1 4 3 10 10 -10 -5
    for i in range(len(arr)-1):
        #curr_sum = max(curr_sum+item,item)
        if curr_sum+arr[i+1] < arr[i+1]:
            start = i+1
            curr_sum = arr[i+1]
        else:
            curr_sum += arr[i+1]

        if max_sum < curr_sum:
            max_sum = curr_sum
            end = i+1


    print "Max sum is %d .",max_sum
    return [start,end]


print count_index([-5,-2,-4,-1,3,2])
print count_index([1,2,-1,3,4,10,10,-10,10,10,10,10,-10])
