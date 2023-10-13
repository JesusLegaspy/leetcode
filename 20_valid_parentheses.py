
def isValid(s):
  lhsLifo = []
  lhsToRhs = {
    '(':')',
    '[':']',
    '{':'}'
  }
  for char in s:
    if char in ['(','[','{']:
      lhsLifo.append(char)
    if char in [')',']','}']:
      if len(lhsLifo) == 0:
        return False
      lhs = lhsLifo.pop()
      if lhsToRhs[lhs] != char:
        return False
  if len(lhsLifo) != 0:
    return False
  return True

  print(lifo)


print(isValid("["))