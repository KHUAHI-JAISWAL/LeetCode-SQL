class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
        #Brute Force: Har * ke liye uske previous character ko string se remove karte raho → Time: O(n²), Space: O(n)

        #Best: Stack use karo; normal character push karo aur * aane par last character pop karo → Time: O(n), Space: O(n)
        