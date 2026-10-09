#Implement a function to reverse a linked list iteratively.
#Each node has a value and a next pointer.
#Return the new head of the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Helper to create linked list from input
def create_list():
    values = input("Enter linked list values (space-separated): ").split()
    if not values:
        return None
    head = ListNode(int(values[0]))
    current = head
    for val in values[1:]:
        current.next = ListNode(int(val))
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

head = create_list()
print("Original list:")
print_list(head)
reversed_head = reverse_linked_list(head)
print("Reversed list:")
print_list(reversed_head)