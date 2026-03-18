"""Week 3 homework: The Royal Rail Ledger.

Implement the required functions below.
Use stdlib only.
"""

from __future__ import annotations


class SLLNode:
    """Node for a singly linked list."""

    def __init__(self, value: int, next: "SLLNode | None" = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    """Simple singly linked list with a head reference."""

    def __init__(self) -> None:
        self.head: SLLNode | None = None


class DLLNode:
    """Node for a doubly linked list."""

    def __init__(
        self,
        value: int,
        prev: "DLLNode | None" = None,
        next: "DLLNode | None" = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """Simple doubly linked list with head and tail references."""

    def __init__(self) -> None:
        self.head: DLLNode | None = None
        self.tail: DLLNode | None = None


def build_sll_from_list(values: list[int]) -> SinglyLinkedList:
    """Build and return a singly linked list from a Python list.

    Examples:
        >>> sll_to_list(build_sll_from_list([]))
        []
        >>> sll_to_list(build_sll_from_list([4, 7, 9]))
        [4, 7, 9]
    """
    raise NotImplementedError


def sll_to_list(sll: SinglyLinkedList) -> list[int]:
    """Return all values from a singly linked list as a Python list."""
    raise NotImplementedError


def find_first_repeat_sll(sll: SinglyLinkedList) -> int | None:
    """Return the first repeated value seen from left to right.

    Return None if no value repeats.
    """
    raise NotImplementedError


def remove_all_from_dll(dll: DoublyLinkedList, target: int) -> None:
    """Remove all nodes whose value equals target.

    Update dll.head and dll.tail correctly.
    Return None.
    """
    raise NotImplementedError


def is_train_palindrome(dll: DoublyLinkedList) -> bool:
    """Stretch: return True if the DLL reads the same forward and backward."""
    raise NotImplementedError