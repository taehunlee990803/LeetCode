····················elif·temp·>·target:
························last·-=1
························third·+=·1
························ans.add((nums[first],·nums[second],·nums[third],·nums[last]))
····················if·temp·==·target:
                ····temp·=·nums[first]·+·nums[second]·+·nums[third]·+·nums[last]
                last = len(nums)-1
                second = j
                third = second + 1

                while third < last:
························last·-=1
····················else:
························third·+=·1
        return ans 


8
[1,0,-1,0,-2,2]
0
