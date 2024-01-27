class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one = sum(data)
        cnt_one = max_one = 0

        deque = collections.deque()

        for i in range(len(data)):
            deque.append(data[i])
            cnt_one += data[i]

            if len(deque) > one:
                cnt_one -= deque.popleft()
            max_one = max(cnt_one, max_one)
        return one - max_one

[
