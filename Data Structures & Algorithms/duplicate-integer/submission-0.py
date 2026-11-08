class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                pass
            seen.add(x)
        unique_lements = set(nums)
        has_duplicates = len(unique_lements) < len(nums)
        return has_duplicates
