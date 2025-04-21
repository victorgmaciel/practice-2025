def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    print(f"Input string: {s}")
    print("-" * 40)

    for right in range(len(s)):
        print(f"Step {right + 1}:")
        print(f"  Right pointer at index {right} -> '{s[right]}'")
        print(f"  Current set before: {char_set}")

        while s[right] in char_set:
            print(f"    '{s[right]}' is already in the set.")
            print(f"    Removing '{s[left]}' at index {left} from the set.")
            char_set.remove(s[left])
            left += 1
            print(f"    Moved left pointer to index {left}")

        char_set.add(s[right])
        print(f"  Added '{s[right]}' to the set.")
        print(f"  Current window: '{s[left:right+1]}'")
        print(f"  Window size: {right - left + 1}")
        max_len = max(max_len, right - left + 1)
        print(f"  Max length so far: {max_len}")
        print("-" * 40)

    print(f"Final longest substring without repeating characters has length: {max_len}")
    return max_len


input = "pwwkew"

lengthOfLongestSubstring(input)
