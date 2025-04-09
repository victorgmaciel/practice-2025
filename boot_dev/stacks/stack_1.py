def isValid(s: str) -> bool:
    stack = []
    mapping = {'(': ')', '{': '}', '[': ']'}

    print(f"Input: {s}")
    print("Starting validation...\n")

    for i, char in enumerate(s):
        print(f"Step {i + 1}: Read '{char}'")

        if char in mapping:
            expected = mapping[char]
            stack.append(expected)
            print(f"  It's an opener. Pushing expected closer '{expected}' onto stack.")
        else:
            if not stack:
                print("  ❌ Stack is empty — no opener for this closer.")
                return False
            top = stack.pop()
            print(f"  It's a closer. Popped '{top}' from stack.")
            if top != char:
                print(f"  ❌ Mismatch! Expected '{top}', but got '{char}'.")
                return False
            else:
                print(f"  ✅ Match! '{char}' closes the correct opener.")

        print(f"  Current stack: {stack}\n")

    if not stack:
        print("✅ All brackets matched. Stack is empty at the end.\n")
        return True
    else:
        print("❌ Unmatched brackets remain in the stack.\n")
        return False


# Test cases
print(isValid("()"))  # True
print(isValid("({[]})"))  # True
print(isValid("([)]"))  # False
print(isValid("((("))  # False
print(isValid("{[()]}"))  # True
