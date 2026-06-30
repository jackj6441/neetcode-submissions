class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        m = {tickets[i][0]:[] for i in range(len(tickets))}
        for i in range(len(tickets)):
            m[tickets[i][0]].append([tickets[i][1], i])
        print (m)
        
        used = [False for _ in range(len(tickets))]
        path = []
        def dfs(place):
            
            print(place, path, used, len(path), len(tickets))
            if len(path) == len(tickets)+1:
                return path
            if place in m:
                for nxt, idx in m[place]:
                    if not used[idx]:
                        used[idx] = True
                        path.append(nxt)
                        result = dfs(nxt)
                        if result:
                            return result
                        else:
                            used[idx] = False
                            path.pop()
            return None
        path.append('JFK')
        dfs('JFK')
        return path
            