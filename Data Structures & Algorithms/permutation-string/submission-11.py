class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        string_size = len(s2)
        if string_size < window_size:
            return False
        left = 0
        right = window_size
        alpha_count_s1 = [0] * 26
        alpha_count_s2 = [0] * 26
        for char in s1:
            alpha_count_s1[ord(char) - 97] += 1

        for idx in range(window_size):
            alpha_count_s2[ord(s2[idx]) - 97] += 1
        if alpha_count_s1 == alpha_count_s2:
            return True
        while right < string_size:
            alpha_count_s2[ord(s2[left]) - 97] -= 1
            alpha_count_s2[ord(s2[right]) - 97] += 1
            if alpha_count_s1 == alpha_count_s2:
                return True

            left += 1
            right += 1
        return False