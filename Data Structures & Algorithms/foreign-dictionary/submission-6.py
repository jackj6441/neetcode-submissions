class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        m = {}
        visit = {}
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            check = 0
            for j in range(min(len(w1),len(w2))):
                l1 = w1[j]
                l2 = w2[j]
                if l1 not in m:
                    m[l1] = []
                if l2 not in m:
                    m[l2] = []
                if l1 != l2:
                    check = 1
                    m[l2].append(l1)
                    break
            if not check and len(w1) > len(w2):
                return ''
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in visit:
                    visit[words[i][j]] = 0
        print(m)
        word = ''
        def dfs(l):
            nonlocal word
            print(l, visit, word)
            if visit[l] == 1:
                return False
            if visit[l] == 2:
                return True
            visit[l] = 1
            if l in m:
                for tmp in m[l]:
                    if not dfs(tmp):
                        return False
            word += l
            visit[l] = 2
            return True
        for i in range(len(words)):
            for j in range(len(words[i])):
                if visit[words[i][j]] == 0:
                    if not dfs(words[i][j]):
                        return ''
        return word
            