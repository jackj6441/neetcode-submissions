class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        m = {}
        if len(hand) % groupSize != 0:
            return False
        headCount = len(hand) // groupSize
        for i in hand:
            if i not in m:
                m[i] = 0
            m[i] += 1
        print(m)
        for i in range(headCount):
            for t in hand:
                if m[t] != 0:
                    head = t
                    break
            for j in range(groupSize):
                curNum = head + j
                # print(curNum, m)
                if curNum not in m or m[curNum] == 0:
                    return False
                m[curNum] -= 1
        return True
                
                