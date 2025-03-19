        
            if fin_check():
                return ans
            
            # Step3 : append reverse of last list
            ans.extend(matrix[-1][::-1])
            matrix.pop(-1)
            matrix = [item for item in matrix if len(matrix) > 0]

            if fin_check():
                return ans

            # Step4 : append first element of remaining lists in reverse order
            for col in reversed(matrix):
                ans.append(col[0])
                col.pop(0)
                
            if fin_check():
                return ans




