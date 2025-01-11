class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        result = []
        for word in words:
            word1 = word.lower()
            if len(set(word1 + row1)) == len(row1) or len(set(word1 + row2)) == len(row2) or len(
                    set(word1 + row3)) == len(row3):
                result.append(word)

        return result