#Definition of a singly linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class solution(object):
    def hasCycle(self, head):
        #Initialize two pointers , both starting at the head of the list
        slow = head #slow pointer moves one step at a time
        fast = head #fast pointer moves two steps at a time 

        #Traverse the linked list
        while fast and fast.next:
            #move slow pointer one step forward
            slow = slow.next
            #move fast ponter two steps forward
            fast = fast.next.next

            #checking if slow pointerand fast pointer meet
            if slow == fast:
                return True 
            
        #If we exit the loop, the fast pointer reached the end of the list which means there is no cycle
        return False
    

soln = solution()

#usage 
#Creating a linked list with a cycle for testing
#Example: Head=[3, 2, 0, -4], where pos = 1 (cycle)
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

#testing linked list with a cycle
print(soln.hasCycle(node1))

#creating a linked list without a cycle
#Example: Head = [1] , pos = -1
node_1 = ListNode(1)

#Testing
print(soln.hasCycle(node_1))

#Testing linked list with a cycle where pos = 0 
node_1_1 = ListNode(1)
node_1_2 = ListNode(2)

node_1_1.next = node_1_2
node_1_2.next = node_1_1

#test 
print(soln.hasCycle(node_1_1))
