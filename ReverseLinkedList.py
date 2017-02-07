
''' "Swaminarayan!" '''


class Node():
    def __init__(self,val = None, nextnode = None):
        self.val = val
        self.nextnode = nextnode

    def setnext(self,node):
        self.nextnode = node

    def getval(self):
        return self.val

    def getnext(self):
        return self.nextnode


#Here we will have head pointer always pointing to
#last node.

class LinkedList():
    def __init__(self, size = 0, head = None):
        self._size = size
        self._head = head


    def insert(self,val):
        self._size += 1
        new_node = Node(val)
        #new_node.setval(val)
        if self._head == None:
            self._head = new_node
            return

        new_node.setnext(self._head)
        self._head = new_node

    def print_list(self):
        self._print_helper(self._head)

    def _print_helper(self,node):
        if node == None:
            return
        self._print_helper(node.getnext())
        print node.getval()

    def size(self):
        return self._size

    def delete(self):
        self._size -= 1
        last_node = self._head.getnext()
        self._head.setnext(None)
        self._head = last_node

    def getval_by_index(self,index):
        if not 0 <= index < self._size:
            print "Not valid. Please insert correct value"
            return None
        #sixe - 4, index - 0, ac = 3
        # 1,2,3,4
        actual_index = self._size - index -1

        i = 0
        node = self._head
        while i != actual_index:
            temp = node.getnext()
            node = temp
            i += 1

        return node.getval()

    def reverse(self):
        # 3 -> 2 -> 1
        curr = self._head.getnext()
        self._head.setnext(None)
        while curr != None:
            nextnode = curr.getnext()
            curr.setnext(self._head)
            self._head = curr
            curr = nextnode




ll = LinkedList()


ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.print_list()


ll.reverse()
ll.print_list()
