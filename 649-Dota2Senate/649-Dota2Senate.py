        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
        
            dTurn = d.popleft()
            rTurn = r.popleft()

            if rTurn < dTurn:
            else:
                r.append(dTurn + len(senate))
            # dTurn : 2
            # rTurn : 0

        d = deque()
                d.append(rTurn + len(senate))

        if r:
            return  "Radiant"
        else:
