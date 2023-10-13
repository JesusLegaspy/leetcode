def twoSum(nums, target):
    compliments = {}
    for index in range(len(nums)):
      currentNumber=nums[index]
      if currentNumber in compliments:
        return [compliments[currentNumber], index]
      compliments[target-currentNumber] = index

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))