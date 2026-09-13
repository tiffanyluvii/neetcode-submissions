class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if (len(s) == 0 or len(s) == 1):
            return len(s)

        longestValue = 0;
        longestString = ""
        l = 0
        r = 1

        longestString += str(s[l])

        while (r < len(s)):
            if (not s[r] in longestString):
                longestString += "" + (s[r])
            else:
                while (s[r] in longestString):
                     longestString = longestString[1:]

                longestString += str(s[r])
                l = r

            print(longestString)

            longestValue = max(longestValue, len(longestString))
            r += 1
        
        return longestValue




        