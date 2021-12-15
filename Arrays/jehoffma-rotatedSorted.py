class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        shift = 0
        if nums[0] > nums[-1]:
            pivot = self.findPivot(nums)
            shift = pivot - len(nums)
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (right-left)//2 + left
            if nums[mid + shift] == target:
                return self.returnResult(mid+shift, target, nums)
                # return mid+shift
            elif nums[mid+shift] > target:
                right = mid-1
            else:
                left = mid + 1

        return self.returnResult(left+shift, target, nums)

    def returnResult(self, index, target, nums):
        if nums[index] == target:
            if index < 0:
                mult = -index//len(nums)
                if not -index % len(nums) == 0:
                    mult += 1

                return index + (mult*len(nums))
            return index
        return -1

    def findPivot(self, nums):
        left = 0
        right = len(nums)-1

        if nums[right] < nums[right-1]:
            return right

        mid = (right-left)//2 + left

        while nums[mid] > nums[mid-1] or nums[mid] > nums[mid+1]:
            if nums[mid] > nums[right]:  # shift right
                left = mid+1
            else:  # shift left
                right = mid-1
            mid = (right-left)//2 + left
        return mid
