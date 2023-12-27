            # left_dic = Counter(str(temp))
            # right_dic = Counter(str(i))
    
            left_dic = Counter(str(temp))
            right_dic = Counter(str(i))

            if len(left_dic) > len(right_dic):
                dif = len(left_dic) - len(right_dic)
                right_dic['0'] = dif

            if right_sum == left_sum and left_dic == right_dic:
            elif len(left_dic) < len(right_dic):
                dif =  len(right_dic) - len(left_dic)
                left_dic['0'] = dif
            
            right_sum = sum(int(digit) for digit in str(i))
            left_sum = sum(int(digit) for digit in str(temp))
            temp = num - i
        for i in range(1,num):
                return True

        return False
4
