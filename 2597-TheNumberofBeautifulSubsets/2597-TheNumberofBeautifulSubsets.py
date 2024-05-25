    def beautifulSubsets(self, nums: List[int], k: int) -> int:
class Solution:
        count = 0
        lenNums = len(nums)

        def explore(index):
            if index == lenNums:
                count += 1
                return
            num = nums[index]

            if num - k not in visited and num + k not in visited:
                visited[num] += 1
                explore(index + 1)
                visited[num] -= 1
                if visited[num] == 0:
                    del visited[num]
            explore(index+1)
        visited = defaultdict(int)
        explore(0)
        return count - 1
            nonlocal count 
[
