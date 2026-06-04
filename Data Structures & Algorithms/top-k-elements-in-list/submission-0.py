class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        mapval = {}
        for num in nums:
            if num in mapval:
                mapval[num] += 1
            else:
                mapval[num] = 1

        # Step 2: Sort the elements based on their frequencies in descending order
        # sorted() takes the dictionary keys and sorts them by their value
        def get_frequency(num):
            return mapval[num]

        sorted_keys = sorted(mapval.keys(), key=get_frequency, reverse=True)
        
        # Step 3: Return the first 'k' elements from the sorted keys
        res = sorted_keys[:k]
        
        return res