import heapq

class Twitter:

    def __init__(self):
        self.following_map = dict()
        self.tweets_map = dict()
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId in self.tweets_map:
            heapq.heappush(self.tweets_map[userId],(self.timestamp, tweetId))
            if len(self.tweets_map[userId]) > 10:
                heapq.heappop(self.tweets_map[userId])
        else:
            self.tweets_map[userId] = [(self.timestamp, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:

        output = []
        if userId in self.tweets_map:
            [heapq.heappush(output, (-x[0], x[1])) for x in self.tweets_map[userId]]

        if userId in self.following_map:
            for followingId in self.following_map[userId]:
                [heapq.heappush(output, (-x[0], x[1])) for x in self.tweets_map[followingId]]
        size = len(output)
        if size > 10:
            return [heapq.heappop(output)[1] for _ in range(10)]
        return [heapq.heappop(output)[1] for _ in range(size)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_map:
            self.following_map[followerId].add(followeeId)
        else:
            self.following_map[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_map and followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
