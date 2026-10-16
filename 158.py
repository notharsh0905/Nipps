#Implement a function to check if a linked list has a cycle.
#Use Floyd's cycle-finding algorithm (tortoise and hare).
#Return True if cycle exists, False otherwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Helper to create linked list from input
def create_list():
    values = input("Enter linked list values (space-separated, 'none' for empty): ").split()
    if values == ['none'] or not values:
        return None
    head = ListNode(int(values[0]))
    current = head
    for val in values[1:]:
        current.next = ListNode(int(val))
        current = current.next
    # Create cycle if last value is 'cycle'
    if values and values[-1] == 'cycle':
        current.next = head
    return head

head = create_list()
print(f"Has cycle: {has_cycle(head)}")