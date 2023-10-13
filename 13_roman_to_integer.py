# def romanToInt(self, s: str) -> int:
# def romanToInt(s):
#   value=0
#   index=0
#   while index < len(s):
#     char = s[index]
#     lookahead = s[index+1] if index + 1 < len(s) else 0
#     if char == 'I':
#       if lookahead == 'V':
#         value+=4
#         index+=2
#         continue
#       if lookahead == 'X':
#         value+=9
#         index+=2
#         continue
#       value+=1
#     if char == 'V':
#       value+=5
#     if char == 'X':
#       if lookahead == 'L':
#         value+=40
#         index+=2
#         continue
#       if lookahead == 'C':
#         value+=90
#         index+=2
#         continue
#       value+=10
#     if char == 'L':
#       value+=50
#     if char == 'C':
#       if lookahead == 'D':
#         value+=400
#         index+=2
#         continue
#       if lookahead == 'M':
#         value+=900
#         index+=2
#         continue
#       value+=100
#     if char == 'D':
#       value+=500
#     if char == 'M':
#       value+=1000
#     index+=1
#   return value

import functools

def romanToInt(s):
  myRomanNumerals = (s
    .replace('IV','IIII').replace('IX','VIIII')
    .replace('XL','XXXX').replace('XC','LXXXX')
    .replace('CD','CCCC').replace('CM','DCCCC'))

  valMap = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  return functools.reduce(lambda acc, cur: acc + valMap[cur], myRomanNumerals, 0)
    

print(romanToInt('MCMXCIV'))