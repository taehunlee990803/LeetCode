class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        end = max(piles)
        
        while low < end:
            speed = (low+end)//2
            time = 0
            
            for pile in piles:
                time += math.ceil(pile*1.0/speed)
                
                if time > h:
                    low = speed + 1
                    break
            if time <= h:
                end = speed
        return low
      
#     //2. binary search 
#     Arrays.sort(piles);
#     int len = piles.length;
#     int start = 1;
#     int end = piles[len-1];

#     while(start < end){
#         int speed = (start+end) / 2;  // 중간 스피드부터 시작
#         int time = 0;
#         for (int i = 0; i < len; i++) {
#             time += Math.ceil((double)piles[i]/speed);
#             if(time > h){ //다 못먹었는데 시간 초과됨, 속도를 올려야함
#                 start = speed+1;
#                 break;
#             }
#         }
#         if(time <= h){  //시간안에 다 먹었으면 속도를 줄여서 다시 확인
#             end = speed;
#         }
#     }
#     return start;

# }