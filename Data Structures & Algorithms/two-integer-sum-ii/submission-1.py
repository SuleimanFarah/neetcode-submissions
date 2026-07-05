class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(numbers)-1
        while start < end:
            print(numbers[start], numbers[end])
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                print(numbers[start], numbers[end])
                return [start+1, end+1]