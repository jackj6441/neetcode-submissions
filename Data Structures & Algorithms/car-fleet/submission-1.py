class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        tmp = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            tmp.append([position[i], time])
        tmp.sort()
        print(tmp)
        i = len(tmp)-1
        out = 0
        for pos, time in reversed(tmp):
            if not s or time > s[-1]:
                s.append(time)

        return len(s)
