class Solution:
    def lengthOfLastWord(self, s):

        s = s.strip()

        last_word = s.split()

        return len(last_word[-1])