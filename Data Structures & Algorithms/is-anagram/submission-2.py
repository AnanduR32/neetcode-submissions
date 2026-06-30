class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_t = len(t)
        if len(s) != len_t:
            return False
        char_set_s = set([x for x in s])
        char_set_t = set([x for x in t])
        if char_set_s != char_set_t:
            return False
        char_count_s = {}
        char_count_t = {}
        for char in s:
            if char in char_count_s:
                char_count_s[char] += 1
            else:
                char_count_s[char] = 1
        for char in t:
            if char in char_count_t:
                char_count_t[char] += 1
            else:
                char_count_t[char] = 1
        for char in s:
            if char_count_s[char] != char_count_t[char]:
                return False
        return True