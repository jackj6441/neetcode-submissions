class Twitter:

    def __init__(self):
        self.follower = {}
        self.feeds = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.feeds:
            self.feeds[userId] = []
        self.feeds[userId].append([-self.t,tweetId])
        print(self.feeds)
        self.t += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        if userId in self.feeds:
            for f in self.feeds[userId]:
                heapq.heappush(out, (f[0],f[1]))
        
        if userId in self.follower:
            for follower in self.follower[userId]:
                if follower not in self.feeds:
                    break
                for f in self.feeds[follower]:
                    heapq.heappush(out, (f[0],f[1]))
        print(out)
        res = []
        i = 0
        while out and i < 10:
            tmp = heapq.heappop(out)
            res.append(tmp[1])
            i += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        if followerId not in self.follower:
            self.follower[followerId] = set()
        self.follower[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower or followeeId not in self.follower[followerId]:
            return
        self.follower[followerId].remove(followeeId)
