class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        #Brute Force: Har collision ke baad array ko repeatedly scan/remove karke asteroids collide karao → Time: O(n²), Space: O(n)
        #Best: Stack use karke har asteroid ko previous opposite-direction asteroid se collide karao → Time: O(n), Space: O(n)

        stack = []

        for asteroid in asteroids:
            alive = True

            while alive and asteroid < 0 and stack and stack[-1] > 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(asteroid)

        return stack
        