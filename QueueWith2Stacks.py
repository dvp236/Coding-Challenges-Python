
#Implement a Queue with 2 Stacks

#Here we will use one stack for enque and another for dequeue
class q2s():

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,ele):
        self.instack.append(ele)

    def dequeue(self):
        #if outstack empty
        if not self.outstack:
            if not self.instack:
                return "queue empty"


            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()




q = q2s()



q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(14)
print q.dequeue()
q.enqueue(4444)
print q.dequeue()

print q.dequeue()
