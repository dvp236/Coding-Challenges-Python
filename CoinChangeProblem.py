
# print "Swaminarayan!!"


# Using greedy approach without recursion
# Does not return true minimum always.
def get_min_number_of_coins(target,coins):
    #1,5,10 -- 7
    remaining = target
    count = 0

    #sort in decending order
    coins.sort(reverse = True)

    #loop over in a greedy approach
    for c in coins:
        if remaining/c >= 1:
            count += remaining/c
            remaining = remaining % c
        if remaining == 0:
            return count

    return count


print get_min_number_of_coins(63,[1,5,10,25])

# Greedy approach will fail here
print get_min_number_of_coins(7,[1,3,4,5,10])


#dynamic approach using recursion
#gives true result
def get_min_coins_dyn(target,coins,results):
    #initialize min_change to target
    min_change = target

    #base case
    if target in coins:
        results[target] = 1
        return 1

    #dynamic use
    elif results[target] > 0:
        return results[target]

    #main
    else:
        for i in [c for c in coins if c <= target]:
            change = 1 + get_min_coins_dyn(target-i,coins,results)

            #if change is lesser than min_change at perticular point
            if change < min_change:
                min_change = change
                results[target] = min_change

    #return minimum change required
    return min_change


print get_min_coins_dyn(7,[1,3,4,5],[0,0,0,0,0,0,0,0])


target = 66
coins = [1,5,10,25]
results = [0] * (target+1)
print get_min_coins_dyn(target,coins,results)
