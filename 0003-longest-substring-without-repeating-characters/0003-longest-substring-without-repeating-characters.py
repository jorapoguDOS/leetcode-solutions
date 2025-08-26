class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = ""
        current = ""
        for i in s:
            if i in current:
                if len(current) > len(long):
                    long = current

                current += i
                index = 1
                for j in current:
                    if j != i:
                        index += 1
                        continue
                    else:
                        current = current[index:]
                        break
            else:
                current += i

        if len(current) > len(long):
            long = current

        return len(long)
