    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        ans = []
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)

        return ans

            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []

[3,3,3,3,3,1,3]
