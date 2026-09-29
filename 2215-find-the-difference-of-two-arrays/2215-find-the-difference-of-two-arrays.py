class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:


        

        # Brute Force - Har element ko dusre array mein search karo; jo nahi mile usko answer mein add karo. time  o(n*m) and space o(n)


        #Best Approach — Set (time o(n+m),space  o(n+m)) 

        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]

        