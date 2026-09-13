class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionAndSpeed = []
        numberOfIterations = []
        stack = []

        for i, pos in enumerate(position):
            positionAndSpeed.append([pos, speed[i]])
        
        positionAndSpeed.sort(key = lambda x: x[0])

        for i, combo in enumerate(positionAndSpeed):
            numberOfIterations.append([(target - combo[0]) / combo[1]])

        print(positionAndSpeed)
        print(numberOfIterations)

        for iteration in reversed(numberOfIterations):
            print(iteration[0])
            stack.append(iteration[0])
            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop() #remove the car that just got added stack[-1] because it collides with the car in front of it
            
        

        return len(stack)