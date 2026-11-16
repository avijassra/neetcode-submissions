class User:
    def __init__(self, userId:int):
        self.userId = userId
        self.tweets = []
        self.following = set()


class Twitter:

    def __init__(self):
        self.users = { }
        self.time = 0
        self._feed_limit = 10
        
    def _users(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._users(userId).tweets.append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self._users(userId)
        arr = user.tweets[-self._feed_limit:]

        for k in user.following:
            arr.extend(self._users(k).tweets[-self._feed_limit:])

        arr.sort(key=lambda x: x[0], reverse=True)

        return [t for _, t in arr[:self._feed_limit]]    

    def follow(self, followerId: int, followeeId: int) -> None:
        self._users(followerId).following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self._users(followerId).following:
            self._users(followerId).following.discard(followeeId)