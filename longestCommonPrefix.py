
# def longestCommonPrefix(strs):
#   wordIndex = 0
#   charIndex = 0
#   currentChar = ''
#   answer=''
#   while(True):
#     if len(strs) <= wordIndex:
#       wordIndex = 0
#       charIndex += 1
#       answer += currentChar
#       continue
#     currentWord = strs[wordIndex]
#     if len(currentWord) <= charIndex:
#       break
#     if wordIndex == 0:
#       currentChar = currentWord[charIndex]
#     if currentWord[charIndex] != currentChar:
#       break
#     wordIndex += 1
#   return answer;

from functools import reduce

def longestCommonPrefix(strs):
  result = min(strs)
  for word in strs:
    while not word.startswith(result):
      result = result[:-1]
  return result

strs = ["flow", "flower","flight"]
print(longestCommonPrefix(strs))