class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n,0) + 1
        a = []
        for ke, c in m.items():
            a.append([c, ke])
        a.sort()
        out = []
        while len(out) < k:
            out.append(a.pop()[1])
        return out