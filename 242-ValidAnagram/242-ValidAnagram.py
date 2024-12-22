                    s_con[s[i]] = 1
                else:
                    s_con[s[i]] += 1
            for i in range(len(t)):
                if t[i] not in t_con:
                    t_con[t[i]] = 1
                else:
                    t_con[t[i]] += 1
            for element in s_con:
                if element not in t_con:
                    return False
                if t_con[element] != s_con[element]:
                    return False

            return True
        return False
                if s[i] not in s_con:
