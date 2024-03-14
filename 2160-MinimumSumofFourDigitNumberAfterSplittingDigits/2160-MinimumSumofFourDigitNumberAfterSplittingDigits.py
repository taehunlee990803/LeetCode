class Solution:
    def minimumSum(self, num: int) -> int:
        container = []
        temp = str(num)
        for i in range(len(temp)):
            container.append(int(temp[i]))
        left = container[0]*10 + container[2]

        return left+right
        right = container[1]*10 + container[3]
        container.sort()

2
