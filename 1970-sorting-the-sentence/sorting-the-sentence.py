class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split()
        result = [""] * len(word)

        for word in word:
            pos = int(word[-1])
            result[pos-1] = word[:-1]

        return " ".join(result)