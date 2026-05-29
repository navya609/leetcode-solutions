class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        word_length = len(words[0])
        total_length = word_length * len(words)

        result = []

        for i in range(len(s) - total_length + 1):

            seen = {}

            for j in range(0, total_length, word_length):

                word = s[i + j:i + j + word_length]

                if word in word_count:

                    seen[word] = seen.get(word, 0) + 1

                    if seen[word] > word_count[word]:
                        break
                else:
                    break

            else:
                result.append(i)

        return result