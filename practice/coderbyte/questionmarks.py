"""
QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
"""


def QuestionsMarks(strParam):

  # code goes here
  num = '0123456789'
  pairs = []

  for i in range(len(strParam)):
      if strParam[i] in num:
          for j in range(i+1, len(strParam)):
              if strParam[j] in num:
                  if int(strParam[i]) + int(strParam[j]) == 10:
                      pairs.append((i, j))
                      break
  if len(pairs) == 0:
        return 'false'
  else:
        for pair in pairs:
            if strParam[pair[0]:pair[1]].count('?') != 3:
                return 'false'
  return 'true'

# keep this function call here 
print(QuestionsMarks('aa6?9'))