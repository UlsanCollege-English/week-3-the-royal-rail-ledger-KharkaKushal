from typing import Optional, List


# ===== Singly Linked List =====
class SinglyLinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


# ===== Doubly Linked List =====
class DLLNode:
    def __init__(self, value: int, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# ===== FUNCTIONS =====

def build_sll_from_list(values: List[int]) -> SinglyLinkedList:
    sll = SinglyLinkedList()

    if not values:
        return sll

    sll.head = SinglyLinkedListNode(values[0])
    current = sll.head

    for val in values[1:]:
        current.next = SinglyLinkedListNode(val)
        current = current.next

    return sll


def sll_to_list(sll: SinglyLinkedList) -> List[int]:
    result = []
    current = sll.head

    while current:
        result.append(current.value)
        current = current.next

    return result


def find_first_repeat_sll(sll: SinglyLinkedList) -> Optional[int]:
    seen = set()
    current = sll.head

    while current:
        if current.value in seen:
            return current.value
        seen.add(current.value)
        current = current.next

    return None


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    current = dll.head

    while current:
        next_node = current.next

        if current.value == target:
            if current.prev:
                current.prev.next = current.next
            else:
                dll.head = current.next

            if current.next:
                current.next.prev = current.prev
            else:
                dll.tail = current.prev

        current = next_node

    if dll.head is None:
        dll.tail = None


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    if dll.head is None:
        return True

    left = dll.head
    right = dll.tail

    while left and right:
        if left.value != right.value:
            return False

        if left == right or left.next == right:
            break

        left = left.next
        right = right.prev

    return True