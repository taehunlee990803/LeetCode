            current = hand[0]
                nextVal = current+1+j
            for j in range(groupSize-1):
                    hand.remove(nextVal)
            hand.remove(current)
                if nextVal in hand:
                else:
        hand = sorted(hand)
        for i in range(count):
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)% groupSize != 0:
            return False
class Solution:
        count = len(hand)//groupSize
[
