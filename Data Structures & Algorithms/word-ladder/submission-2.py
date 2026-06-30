class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n, m = len(wordList), len(wordList[0])
        adj = [[] for _ in range(n)]
        ma = {}
        for i in range(n):
            ma[wordList[i]] = i
        for i in range(n):
            for j in range(i+1, n):
                diff = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                if diff == 1:
                    adj[i].append(wordList[j])
                    adj[j].append(wordList[i])
        print(adj)
        def bfs(begin, target):
            visit = set()
            q = deque()
            count = 1
            for i in range(m):
                for c in range(97, 123):
                    if chr(c) == begin[i]:
                        continue
                    word = begin[:i]+chr(c)+begin[i+1:]
                    if word in ma and ma[word] not in visit:
                        q.append(ma[word])
                        visit.add(ma[word])
            while q:
                print(q)
                count += 1
                for i in range(len(q)):
                    idx = q.popleft()
                    if wordList[idx] == target:
                        return count
                    for nxt in adj[idx]:
                        if ma[nxt] not in visit:
                            q.append(ma[nxt])
                            visit.add(ma[nxt])
            return 0
        return bfs(beginWord, endWord)