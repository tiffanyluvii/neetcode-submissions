class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            print(stack)
            if not stack:
                stack.append([temp, i])
            elif (temp <= stack[-1][0]): # double check this
                stack.append([temp, i])
            else:
                stop = False

                while (not stop and stack):
                    peekedValue = stack[-1]
                    if (peekedValue[0] < temp):
                        output[peekedValue[1]] = i - peekedValue[1]
                        stack.pop()
                    else:
                        stop = True
                stack.append([temp,i])


        return output


                

