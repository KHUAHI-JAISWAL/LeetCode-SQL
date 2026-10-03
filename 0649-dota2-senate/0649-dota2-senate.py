class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        #Brute Force: Har round mein string scan karke opposite senator ko ban/remove karo → O(n²) Time, O(n) Space.
        #Best: Two Queues mein R aur D ke indices rakho aur smaller index wala senator opponent ko ban kare → O(n) Time, O(n) Space.

        radiant = deque()
        dire = deque()

        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"




        