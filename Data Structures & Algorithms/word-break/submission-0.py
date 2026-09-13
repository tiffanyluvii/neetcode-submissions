class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = [False] * (len(s) + 1)
        check[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s) and s[i : i + len(word)] == word):
                    check[i] = check[i + len(word)]

                if (check[i]):
                    break
            

        return check[0]


