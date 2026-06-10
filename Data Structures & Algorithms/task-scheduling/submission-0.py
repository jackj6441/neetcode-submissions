class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        most = 0
        m = {}
        ta = None
        for t in tasks:
            m[t] = m.get(t, 0) + 1
            if m[t] > most:
                most = m[t]
                ta = t
        idles = (most-1)*n
        print(idles)
        for i in m:
            if i != ta:
                idles -= min(m[i], most-1)
                print(t, idles)
        return len(tasks)+max(0, idles)