"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

def generateParenthesis(N):
  from itertools import combinations

  N = 3
  numbers = [val for val in range(1,N*2)]

  combs = [l for l in combinations(numbers, N)]

  ans = []
  for i in combs:
      check = 0
      index = 1
      for j in range(1, N*2+1):
          if(check < 0):
              check = 404
              break
          if(j in i):
              check += 1
          else:
              check -= 1
      if(check != 404):
          string = ""
          for j in range(1,N*2+1):
              if(j in i):
                  string += "("
              else:
                  string += ")"
  # Alternative method
  #         for j in i:
  #             string += ")"*(j-len(string)-1)
  #             string += "("
  #         string += ")"*(N*2-j)
          ans.append(string)
  print(len(ans))
  ans
