class RecentCounter:
    #Brute Force: Har ping(t) par saari previous calls check karke [t-3000, t] wali calls count karo → O(n²) Time, O(n) Space.
    #Best:  DQueue use karo; t add karo aur jo calls < t-3000 hain unhe remove karo → O(n) Time, O(n) Space

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)