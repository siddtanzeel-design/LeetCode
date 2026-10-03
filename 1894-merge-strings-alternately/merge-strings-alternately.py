class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wrd1 = word1.strip()
        wrd2 = word2.strip()

        result = []
        i=j=0

        while i < len(wrd1) and j < len(wrd2):
            result.append(wrd1[i])
            i+=1
            result.append(wrd2[j])
            j+=1

        result.append(wrd1[i:] or wrd2[j:])

        return "".join(result)