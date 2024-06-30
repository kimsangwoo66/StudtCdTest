class Solution:
    def lengthOfLastWord(s: str) -> int:
        return len(s.split()[-1])


result = Solution.lengthOfLastWord("Hello World")
print(result)