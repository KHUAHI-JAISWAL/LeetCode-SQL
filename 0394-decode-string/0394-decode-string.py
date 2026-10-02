class Solution:
    def decodeString(self, s: str) -> str:

        #Brute Force: Repeatedly find the innermost k[substring] and replace it → O(n²) time, O(n) space.
        #Best Approach: Use Stack to store previous strings and repeat counts while traversing → O(n) time, O(n) space.

        stack = []
        num = 0
        curr = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((curr, num))
                curr = ""
                num = 0

            elif ch == ']':
                prev, repeat = stack.pop()
                curr = prev + curr * repeat

            else:
                curr += ch

        return curr
        