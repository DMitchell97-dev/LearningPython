class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    if head is None or n < 1:
        return head

    # Create dummy node to handle head removal
    dummy = Node(0)
    dummy.next = head

    # Move fast pointer n steps ahead
    fast = dummy
    for _ in range(n):
        if fast.next is None:
            return head  # n is larger than list length
        fast = fast.next

    # Move both pointers until fast reaches the end
    slow = dummy
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # Remove the node
    slow.next = slow.next.next

    return dummy.next

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
    n = int(input())
    res = remove_nth_from_end(head, n)
    print(" ".join(format_list(res)))