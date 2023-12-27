class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_elements = Counter(nums)
        # elements = collections.OrderedDict(sorted(dict_elements.items()))
        # ans = []
        # for element in elements:
        #     ans.append(element)
        answer = []
        for i in range(0,k):
            answer.append(elements[-1 - i])
        return answer

        elements = dict(sorted(dict_elements.items(), key=lambda item: item[1]))
        elements = list(elements)
[
