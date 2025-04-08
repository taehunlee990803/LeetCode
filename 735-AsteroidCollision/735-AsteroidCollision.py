class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        return stack





        for a in asteroids:
            if a < 0: # Negative
            stack.append(a)

                while stack and 0 < stack[-1] < abs(a):
                    stack.pop()

                if stack and stack[-1] == abs(a):
                    stack.pop()
                    continue
                elif stack and abs(a) < stack[-1]:
                    continue

            print(stack)
