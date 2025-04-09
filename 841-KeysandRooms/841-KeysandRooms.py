class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # currentKey = deque([rooms[0]])
        # visited = [0]
        # n = len(rooms)

        # while currentKey:
        #     current = currentKey.popleft()
        #     for i in range(len(current)):
        #         key = current[i]
        #         if key not in visited:
        #             visited.append(key)
        #     print(current)
        # for room in rooms:

        visited = set()
        #     for i in range(len(room)):
        #             visited.append(room[i])
        #         if room[i] not in visited:
        # # print(visited)
        #     # print(room)
        # return check.sort() == visited.sort()
        # check = [i for i in range(len(rooms))]
        # print(visited)
        # print(check)
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited) == len(rooms)
