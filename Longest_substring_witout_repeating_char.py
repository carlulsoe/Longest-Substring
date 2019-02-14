def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 1:
        return 1
    current = set()
    longest, i, j = 0, 0, 0
    while i < len(s) and j < len(s):
        if s[j] not in current:  # checks if char is in the current set and updates the sliding window accordingly
            current.add(s[j])
            j += 1
            longest = max(longest, j - i)
        else:
            current.remove(s[i])
            i += 1
    return longest


# some examples
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("dvdf"))