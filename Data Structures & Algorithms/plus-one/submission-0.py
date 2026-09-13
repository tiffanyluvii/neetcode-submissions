class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        length = len(digits) - 1
        total = 0
        for digit in digits: 
            total += (digit * (10 ** length))
            length -= 1
        
        total += 1
        newDigits = []

        digitStr = str(total)
        for digit in digitStr:
            newDigits.append(int(digit))

        return newDigits


