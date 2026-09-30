class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:



        #Brute Force: Har possible character operation/permutation try karke check karo → Time: O(n!), Space: O(n).
        #Best: Frequency map banao, unique characters aur sorted frequencies compare karo → Time: O(n log n), Space: O(n).













        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in word2:
            freq2[ch] = freq2.get(ch, 0) + 1

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        return sorted(freq1.values()) == sorted(freq2.values())




        