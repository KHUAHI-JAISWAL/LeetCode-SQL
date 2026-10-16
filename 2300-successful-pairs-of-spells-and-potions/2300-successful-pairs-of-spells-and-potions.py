class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            left, right = 0, m

            while left < right:
                mid = left + (right - left) // 2

                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1

            result.append(m - left)

        return result

        