class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: Node) -> Node:
    #Dummy node to simplify insertion at the beginning
    dummy_node = Node(None)
    #Pointer to traverse the original list
    current = head
    #Iterate through each node in the original list
    while current:
        #Store the next node before we modify current's next pointer
        next_node = current.next

        #Insert current node at the beginning of the reversed list
        #Point current's next to whatever dummy is pointing to
        current.next = dummy_node.next
        #Make dummy point to the current node (new head of the reversed list)
        dummy_node.next = current

        #Move to the next node in the original list
        current = next_node
    return dummy_node.next

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None:
        return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    res = reverse_linked_list(head)
    print(" ".join(format_list(res)))
