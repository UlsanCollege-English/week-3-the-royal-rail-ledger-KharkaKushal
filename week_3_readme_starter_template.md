# README Starter Template

# Week 3: The Royal Rail Ledger

## Summary
Write 3 to 6 lines that explain:
- what this assignment does
- which functions you implemented
- which linked-list types are used
- what part was hardest for you

**Starter prompt:**
This assignment focuses on linked-list operations in a railway story setting. I implemented functions for building and reading a singly linked list, finding the first repeated value, removing banned cargo from a doubly linked list, and checking whether a train is a palindrome. The assignment uses both singly linked lists and doubly linked lists. The hardest part was ________________________.

---

## Approach
Use bullets. For each function, explain your basic strategy.

### `build_sll_from_list(values)`
- I started with ________________________
- I built the list by ________________________
- I made sure the values stayed in the correct order by ________________________

### `sll_to_list(sll)`
- I started at ________________________
- I traversed the list by ________________________
- I collected values in a Python list by ________________________

### `find_first_repeat_sll(sll)`
- I tracked values I had already seen by ________________________
- When I found a repeated value, I ________________________
- If I reached the end with no repeat, I ________________________

### `remove_all_from_dll(dll, target)`
- I traversed the list using ________________________
- When I found the target value, I updated ________________________
- I checked special cases such as ________________________

### `is_train_palindrome(dll)`
- I compared values from ________________________
- I stopped when ________________________
- I returned `True` or `False` based on ________________________

---

## Complexity
For each required function, list:
- **Time complexity:**
- **Space complexity:**
- **Why:**

### `build_sll_from_list(values)`
- **Time complexity:**
- **Space complexity:**
- **Why:**

### `sll_to_list(sll)`
- **Time complexity:**
- **Space complexity:**
- **Why:**

### `find_first_repeat_sll(sll)`
- **Time complexity:**
- **Space complexity:**
- **Why:**

### `remove_all_from_dll(dll, target)`
- **Time complexity:**
- **Space complexity:**
- **Why:**

### `is_train_palindrome(dll)` *(stretch)*
- **Time complexity:**
- **Space complexity:**
- **Why:**

### Complexity notes to think about
You should be ready to explain ideas like:
- linked lists do not give direct indexed access like Python lists
- traversal is usually linear
- pointer updates can be efficient when you already know where to modify the list
- different structures make different tradeoffs

---

## Edge-Case Checklist
Mark each item after you test it.

- [ ] empty SLL
- [ ] empty DLL
- [ ] single-node SLL
- [ ] single-node DLL
- [ ] no repeated values in SLL
- [ ] repeated value appears later in SLL
- [ ] repeated value includes the head value
- [ ] removing from DLL when target is at head
- [ ] removing from DLL when target is at tail
- [ ] removing consecutive target values in DLL
- [ ] removing all nodes from DLL
- [ ] palindrome with odd length
- [ ] palindrome with even length
- [ ] non-palindrome DLL

---

## Assistance & Sources
List any help you used.

### AI use
- I used AI: Yes / No
- If yes, what did it help with?

### Other sources
- Class notes:
- Slides:
- Book:
- Websites:
- Other:

---

## Debugging Notes
Write 2 to 5 bullets about what went wrong and how you fixed it.

- I first got stuck on ________________________
- The failing test that helped me most was ________________________
- I fixed the issue by ________________________
- One mistake I will avoid next time is ________________________

---

## Final Reflection
Write 2 to 4 lines.

Possible prompts:
- What did this assignment teach you about linked lists?
- Which was harder: SLL or DLL, and why?
- What edge case surprised you the most?
- What would you review before the next quiz or assignment?

